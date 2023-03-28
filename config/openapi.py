"""
openapi 配置类
"""

from enums.openapi import OpenApiEnum


class OpenApiConfig:
    model: str = OpenApiEnum.TEXT_DAVINCI_003

    apiKey: str = ''

    url = "https://api.openai.com/v1/completions"
