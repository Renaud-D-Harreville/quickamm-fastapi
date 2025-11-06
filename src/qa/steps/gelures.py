from pydantic import BaseModel
from qa.common.models import Reference


class Sign(BaseModel):
    sign: str


class GelureStep(BaseModel):
    name: str
    signs: list[Sign]
    description: str | None = None
    references: list[Reference] | None = None


class GeluresSteps(BaseModel):
    gelure_steps: list[GelureStep]

