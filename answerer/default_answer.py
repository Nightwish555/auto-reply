from .answerer import Answerer


class DefaultAnswer(Answerer):

    def do_answer(self, prompt: str):
        """
        默认回答
        :param prompt:  提示语
        :return:
        """
        return "抱歉，我无法理解您的问题" + prompt
