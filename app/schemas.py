from pydantic import BaseModel
from typing import List, Optional


class Message(BaseModel):
    role: str
    content: str


class InferPilotConfig(BaseModel):
    cache: bool = True
    routing: bool = True
    budget_priority: str = 'balanced'
    quality_level: str = 'balanced'


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 300
    inferpilot: InferPilotConfig = InferPilotConfig()
