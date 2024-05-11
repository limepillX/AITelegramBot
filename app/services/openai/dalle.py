from typing import Literal

from app.core.config import config
from app.core.loader import openai_client


def _get_size(size: int) -> Literal["256x256"] | Literal["512x512"] | Literal["1024x1024"]:
    if size < 256:
        return "256x256"
    elif size < 512:
        return "512x512"
    elif size < 1024:
        return "1024x1024"
    else:
        return "256x256"


async def get_dalle_response(prompt: str) -> list[str]:
    response = await openai_client.images.generate(
        model=config.openai.dalle.model,
        prompt=prompt,
        n=config.openai.dalle.amount_of_images,
        response_format="url",
        size=_get_size(config.openai.dalle.size),
    )
    urls = [image.url for image in response.data if image.url]
    return urls
