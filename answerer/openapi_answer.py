import requests

from .answerer import Answerer
from config.openapi import OpenApiConfig
from schema.openapi import OpenApiForm
from exception.exception import BusinessException
from enums.error_code import ErrorCode


class OpenAiAnswerer(Answerer):

    def do_answer(self, prompt: str):
        """
        openapi 回答
        :param prompt: 提示语
        :return:
        """
        if not OpenApiConfig.apiKey:
            raise BusinessException("未传 openAiApiKey")

        openapi_form = OpenApiForm(model=OpenApiConfig.model, prompt=prompt, max_tokens=1024, temperature=0)
        headers = {
            "Authorization": "Bearer " + OpenApiConfig.apiKey
        }
        response = requests.post(url=OpenApiConfig.url, json=openapi_form.json(), headers=headers)
        return response.json()
