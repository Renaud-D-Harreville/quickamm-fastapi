from qa.mcq_db.models import MCQAnswer, Reference
from qa.species.models import AllSpecies, OneSpecies
from qa.common.base_factory import AbstractMCQFactory
import random

class AllSpeciesMCQFactory(AbstractMCQFactory):
    """
        Factory class to generate multiple-choice questions related to plant species.
        This class handles the creation of questions, answers, images, explanations, and references
        for a given set of plant species, based on specified topics.
    """
    TOPICS = ["Plant Identification"]
    TEXT_QUESTION = "What is that plant?"  # Here, we now have a better view of 'hard coded' things, so that we do not have to read the whole code.

    def __init__(self, all_species: AllSpecies):
        self.all_species = all_species

    def get_questions_with_topics(self, topics: list[str]) -> list[OneSpecies]:
        """Retrieve questions based on specified topics."""
        questions = []
        for species in self.all_species.species.values():
            # Combine factory topics and species classification topics
            combined_topics = set(self.TOPICS) | set(species.classification.topics())

            if all(topic in combined_topics for topic in topics):
                questions.append(species)
        return questions

    def get_question(self, surrounding_mcq_object: OneSpecies) -> str:
        """Retrieve text question to use for the MCQ."""
        return self.TEXT_QUESTION

    def get_image_path(self, surrounding_mcq_object: OneSpecies) -> str | None:
        """Get a random image path for the specified species."""
        if surrounding_mcq_object.images:
            return random.choice(surrounding_mcq_object.images).static_path  # Randomly choose an image
        return None

    def get_explanation(self, surrounding_mcq_object: OneSpecies) -> str:
        """Retrieve the explanation for the specified species."""
        return surrounding_mcq_object.description

    # This function allows to use the same code while retrieving an MCQAnswer from a OneSpecies object.
    # It will be helpful in the future, when you would like to modify it, so that you now have only one method to modify
    @staticmethod
    def _get_answer(species: OneSpecies, is_true: bool) -> MCQAnswer:
        """Retrieve an MCQAnswer object for the specified species."""
        return MCQAnswer(text=species.french_name, is_true=is_true, explanation=species.description)

    def get_answers(self, surrounding_mcq_object: OneSpecies) -> list[MCQAnswer]:
        """Get the correct answer and possible false answers."""
        correct_answer = self._get_answer(surrounding_mcq_object, True)
        wrong_answers = self.get_possible_false_answers(surrounding_mcq_object)
        return [correct_answer] + wrong_answers

    def get_possible_false_answers(self, surrounding_mcq_object: OneSpecies) -> list[MCQAnswer]:
        """Retrieve false answers for the specified species."""
        wrong_answers = []
        for species in self.all_species.species.values():
            if species != surrounding_mcq_object:  # Avoid using the same plant
                wrong_answer = self._get_answer(species, False)
                wrong_answers.append(wrong_answer)
        return wrong_answers

    def get_references(self, surrounding_mcq_object: OneSpecies) -> list[Reference]:
        """Retrieve references for the specified species."""
        return surrounding_mcq_object.references if surrounding_mcq_object.references else []

