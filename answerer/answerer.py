"""
answerer 回答者 抽象类
"""


from abc import ABC, abstractmethod


class Answerer(ABC):

    @abstractmethod
    def do_answer(self, prompt: str):
        pass
