# Author: Mahmoud GHonem: mahmoud.gh2016@gmail.com

from fastapi import FastAPI, Request, BackgroundTasks
from LLM.course_content_generator import *
from pydantic import BaseModel
from typing import Optional
# from simple_token import *
# import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open('pricing_model.pkl', 'rb'))


# @app.get("/test")
# def home(token: str = Depends(validate_token)):
#     return {"Data": "API Is Working"}

class CourseInputData(BaseModel):
    course_name: str
    course_level: Optional[str] = "متوسط"
    course_tags: Optional[str] = ""


class PricingInputData(BaseModel):
    Duration: float
    Level: int
    Country: int
    Category: int


app = FastAPI()


@app.get("/")
def home():
    return {"Data": "API Is Working"}


@app.post("/generate")
async def generate_course_info(data: CourseInputData):
    # extract info required to trigger the job
    course_name = data.course_name
    course_level = data.course_level
    course_tags = data.course_tags

    text = f"""

            course = {course_name}
            level = {course_level}
            keywords = {course_tags}
        
            """
    course_info = llm(similar_prompt.format(input_text=text)).strip()

    return {
        'statusCode': 200,
        'body': course_info
    }


@app.post('/predict_price')
async def predict(data: PricingInputData):
    Duration = data.Duration
    Level = data.Level
    Country = data.Country
    Category = data.Category

    lov = [Duration, Level, Country, Category]
    input_data = np.array([lov])

    print("data", input_data)
    # return data

    # query = pd.DataFrame(input_data)
    # print("query \n", query)
    prediction = model.predict(input_data)


    print("prediction", prediction)
    return {'prediction': prediction[0]}