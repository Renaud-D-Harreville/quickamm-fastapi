from qa.steps.gelures import GeluresSteps
from qa import resource_dir_path
import json

fauna_json_path = resource_dir_path / "cold.json"


def get_gelures_steps() -> GeluresSteps:
    with open(fauna_json_path, "r", encoding='utf-8') as f:
        json_data = json.loads(f.read())
    return GeluresSteps(**json_data)


class TestThemes:

    def test_code(self):
        pass

    def test_create(self):
        themes = get_gelures_steps()


