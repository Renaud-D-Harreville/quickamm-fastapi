import json
from qa import resources_dir_path
from qa.mcq_db.models import MCQModelsDB
import os

# questions_json_path = resource_dir_path / "data-annotation" / "data-annotation.json"
questions_json_path = resources_dir_path / "mcq_explanation.json"
mcq_models_directory_path = resources_dir_path / "mcq_models"


class _SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



def __load_question_db() -> MCQModelsDB:
    question_db: MCQModelsDB = MCQModelsDB(mcq_models=list())  # empty object
    for root, _, files in os.walk(mcq_models_directory_path):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file), "r", encoding='utf-8') as f:
                    json_data = json.loads(f.read())
                    tmp_db = MCQModelsDB(**json_data)
                    question_db.mcq_models.extend(tmp_db.mcq_models)
    return question_db

__question_db: MCQModelsDB = __load_question_db()
print(f"Loaded {len(__question_db.mcq_models)} questions")


def get_questions_db() -> MCQModelsDB:
    return __question_db
