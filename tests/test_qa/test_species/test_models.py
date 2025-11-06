from qa.species.models import AllSpecies
from qa import resource_dir_path
import json

fauna_json_path = resource_dir_path / "species.json"


def get_species() -> AllSpecies:
    with open(fauna_json_path, "r", encoding='utf-8') as f:
        json_data = json.loads(f.read())
    return AllSpecies(**json_data)

class TestThemes:

    def test_create(self):
        species = get_species()
        topics = species.species["Campanula persicifolia"].get_classification_topics()
        print()
        print(topics)