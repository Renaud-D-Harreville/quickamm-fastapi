from qa.api.mcq_factories import AllQuestionsFactory


class TestAllQuestionsFactory:

    def test_get_random_factory_from_topics(self):
        all_factory = AllQuestionsFactory()
        topic_factory = all_factory.get_random_factory_from_topics([
                "Probatoire AMM",
                "Le milieu montagnard",
                "Écologie générale"
              ])

    def test_get_random_question_from_topics(self):
        all_factory = AllQuestionsFactory()
        question = all_factory.get_random_question_from_topics([
                "Probatoire AMM",
                "Le milieu montagnard",
                "Écologie générale"
              ])
        assert "Écologie générale" in question.topics