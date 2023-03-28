from pydantic import BaseModel


class OpenApiForm(BaseModel):
    model: str
    prompt: str
    max_tokens: int
    temperature: int
    top_p: int
    n: int
    stream: bool
    logprobs: int
    stop: str
