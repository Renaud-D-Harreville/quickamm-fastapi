import random

from qa.fauna import AnimalsMCQFactory, get_animals
from qa.flora import FlowersMCQFactory, get_flowers
from qa.toponymy import ToponymyToWordMCQFactory, WordToToponymyMCQFactory, get_toponymy
from qa.mcq_db.factories import MCQDBMCQFactory
from qa.mcq_db.db import get_questions_db
from qa.common.base_factory import AbstractMCQFactory
from qa.mcq_db.models import MCQData
from qa.api.builders import MCQBuilder


class AllQuestionsFactory:

    def __init__(self):
        self.questions_factories: list[AbstractMCQFactory] = list()
        self.__fulfill_questions_factories()

    def __fulfill_questions_factories(self):
        self.questions_factories.append(MCQDBMCQFactory(get_questions_db()))
        # self.questions_factories.append(ToponymyToWordMCQFactory(get_toponymy()))
        # self.questions_factories.append(WordToToponymyMCQFactory(get_toponymy()))
        self.questions_factories.append(AnimalsMCQFactory(get_animals()))
        self.questions_factories.append(FlowersMCQFactory(get_flowers()))

    def get_random_factory_from_topics(self, topics: list[str], seed: int | float | str = None) -> AbstractMCQFactory:
        seed_random = random.Random(seed)
        weighted_factories = [factory.calculate_weight(topics) for factory in self.questions_factories]
        factory: AbstractMCQFactory = seed_random.choices(self.questions_factories, weights=weighted_factories, k=1)[0]
        return factory

    def make_user_mcq_object(self, whole_mcq_object: MCQData) -> MCQData:
        builder = MCQBuilder(whole_mcq_object, max_nb_correct_answers=2, probs=[1, 1/6])
        mcq = builder.build_mcq()
        return mcq

    def get_random_question_from_topics(self, topics: list[str], seed: int | float | str = None) -> MCQData:
        factory = self.get_random_factory_from_topics(topics, seed)
        question_data = factory.get_whole_mcq_data(topics)
        user_question = self.make_user_mcq_object(question_data)
        return user_question

