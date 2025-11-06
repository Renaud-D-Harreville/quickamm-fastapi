import random
from abc import ABC, abstractmethod
from pathlib import Path

from qa.mcq_db.models import MCQAnswer, MCQData, Reference
from typing import TypeVar

SurroundingMCQObjectClass: TypeVar = TypeVar("SurroundingMCQObjectClass")


class AbstractMCQFactory(ABC):
    """
        Abstract base class for creating multiple-choice question factories.

        This class defines the interface for any specific MCQ factory implementation,
        ensuring that all derived classes provide the necessary methods for generating
        questions, answers, and related data.
    """

    @abstractmethod
    def get_questions_with_topics(self, topics: list[str]) -> list[SurroundingMCQObjectClass]:
        pass

    def calculate_weight(self, topics: list[str]) -> float:
        result_list = self.get_questions_with_topics(topics)
        weight = len(result_list)
        return weight

    def get_image_path(self, surrounding_mcq_object: SurroundingMCQObjectClass) -> Path | str | None:
        return None

    @abstractmethod
    def get_answers(self, surrounding_mcq_object: SurroundingMCQObjectClass) -> list[MCQAnswer]:
        pass

    @abstractmethod
    def get_explanation(self, surrounding_mcq_object: SurroundingMCQObjectClass) -> str | None:
        pass

    def get_references(self, surrounding_mcq_object: SurroundingMCQObjectClass) -> list[Reference] | None:
        return None

    @abstractmethod
    def get_question(self, surrounding_mcq_object: SurroundingMCQObjectClass) -> str:
        pass

    def get_whole_mcq_data(self, topics: list[str], seed: int | float | str = None) -> MCQData:
        seed_random = random.Random(seed)
        surrounding_mcq_object_list = self.get_questions_with_topics(topics)
        surrounding_mcq_object = seed_random.choice(surrounding_mcq_object_list)

        # Create MCQData object
        return MCQData(
            topics=topics,
            question=self.get_question(surrounding_mcq_object),
            image_path=self.get_image_path(surrounding_mcq_object),
            answers=self.get_answers(surrounding_mcq_object),
            description=self.get_explanation(surrounding_mcq_object),
            references=self.get_references(surrounding_mcq_object)
        )

