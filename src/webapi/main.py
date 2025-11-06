from fastapi import FastAPI
from qa.mcq_db.models import MCQData
from qa.api.api import get_random_question_from_topics
app = FastAPI()


@app.get("/random_question")
def get_random_question() -> MCQData:
    mcq_data = get_random_question_from_topics(["Probatoire AMM"])
    return mcq_data
