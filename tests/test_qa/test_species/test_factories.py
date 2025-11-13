from qa.species.models import AllSpecies
from qa.species.factories import AllSpeciesMCQFactory
from qa import resources_dir_path
import json

fauna_json_path = resources_dir_path / "species.json"


def get_species() -> AllSpecies:
    with open(fauna_json_path, "r", encoding='utf-8') as f:
        json_data = json.loads(f.read())
    return AllSpecies(**json_data)


class TestAllSpeciesMCQFactory:

    def test_factory(self):
        species = get_species()
        factory = AllSpeciesMCQFactory(species)
        # Only 3 have that order
        questions = factory.get_questions_with_topics(["Plant Identification", "order:Asterales"])
        assert len(questions) == 3
        print()
        for question in questions:
            print(question)
        mcq_data = factory.get_whole_mcq_data(questions[0])
        print()
        print(mcq_data)


