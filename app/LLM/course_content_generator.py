import os
from dotenv import load_dotenv
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.llms import OpenAI

from .data import *

from langchain import PromptTemplate
import time
import yaml
load_dotenv()


with open(r'utilities/config.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    config = yaml.load(file, Loader=yaml.FullLoader)


openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(model_name=config["model_name"], openai_api_key=openai_api_key, temperature=0.5)


example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Example Input: {input}\nExample Output: {output}",
)

# Examples of locations that nouns are found
examples = [
    {"input": sys_input0, "output": sys_output0},
    {"input": sys_input1, "output": sys_output1},
    {"input": sys_input2, "output": sys_output2},

]

# SemanticSimilarityExampleSelector will select examples that are similar to your input by semantic meaning

example_selector = SemanticSimilarityExampleSelector.from_examples(
    # This is the list of examples available to select from.
    examples,

    # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
    OpenAIEmbeddings(openai_api_key=openai_api_key),

    # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
    FAISS,

    # This is the number of examples to produce.
    k=2
)

prompt_perfix = """Given some information about the course, return organized information about 
                the course with Udemy Structre written in Arabic as follow:
                العنوان: write here the title of the course
                العنوان الفرعي: write here the subtitle of the course
                الأهداف: write here the objectives of the course as bullet points, each point starts with "-"
                المتطلبات: write here the requirements of the course as bullet points, , each point starts with "-"
                الوصف: write here the description of the course
                محتوى الدورة: write here the course content of the course as  a two levels bullet points, first level is main title start with '*', and under it, there are some  sub titles, each start with '-'. 
                Make sure that course content is two levels bullet points

                Start with your answer dilrectly in Arabic and include only these sections. 
                Write technical words in English
                use the keywords in your answers and make the answer according to the course level

                """

similar_prompt = FewShotPromptTemplate(
    # The object that will help select examples
    example_selector=example_selector,

    # Your prompt
    example_prompt=example_prompt,

    # Customizations that will be added to the top and bottom of your prompt
    prefix=prompt_perfix,
    suffix="Input: {input_text}\nOutput:",

    # What inputs your prompt will receive
    input_variables=["input_text"],
)
