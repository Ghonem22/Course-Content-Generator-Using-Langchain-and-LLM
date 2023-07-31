# Author: Mahmoud GHonem: mahmoud.gh2016@gmail.com

from fastapi import FastAPI, Request, BackgroundTasks
from LLM.course_content_generator import *
from pydantic import BaseModel
from typing import Optional
# from simple_token import *


# @app.get("/test")
# def home(token: str = Depends(validate_token)):
#     return {"Data": "API Is Working"}

class CourseInputData(BaseModel):
    course_name: str
    course_level: Optional[str] = "متوسط"
    course_tags: Optional[str] = ""


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
