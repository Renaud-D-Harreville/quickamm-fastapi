from fastapi import FastAPI
from qa.mcq_db.models import MCQData
from qa.api.api import get_random_question_from_topics
from fastapi.middleware.cors import CORSMiddleware  # 1. Import this
from qa import resource_dir_path
from fastapi.staticfiles import StaticFiles
app = FastAPI()

# 2. Define the "origins" (domains) that are allowed to make requests.
#    For development, you might just allow your Vue dev server.
#    For production, you'll add your live website's domain.
#    Using ["*"] allows everyone, but be careful with this.

origins = [
    "*",
]

# 3. Add the middleware to your app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


app.mount("/images", StaticFiles(directory=resource_dir_path), name="images")

@app.get("/random_question")
def get_random_question() -> MCQData:
    mcq_data = get_random_question_from_topics(["Probatoire AMM"])
    return mcq_data
