#!/usr/bin/env python3

import dataclasses
from typing import List
from rich import print


@dataclasses.dataclass
class Message:
    role: str
    content: str


@dataclasses.dataclass
class Choose:
    index: int
    message: Message
    finish_reason: str


@dataclasses.dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclasses.dataclass
class ChatResponse:
    id: str
    object: str
    created: int
    model: str
    choices: List[Choose]
    usage: Usage
    system_fingerprint: str


def purse_chat_response(purse_target: dict) -> ChatResponse:
    res = ChatResponse(**purse_target)
    res.choices[0] = Choose(**res.choices[0])
    res.choices[0].message = Message(**res.choices[0].message)
    res.usage = Usage(**res.usage)
    return res


if __name__ == "__main__":
    response = {
        "id": "chatcmpl-8UsGlXRFI9qlNTQj9J1prKllyPZKG",
        "object": "chat.completion",
        "created": 1702369143,
        "model": "gpt-3.5-turbo-0613",
        "choices": [{"index": 0, "message": {"role": "assistant", "content": "Hello John! How can I assist you today?"}, "finish_reason": "stop"}],
        "usage": {"prompt_tokens": 23, "completion_tokens": 10, "total_tokens": 33},
        "system_fingerprint": None,
    }

    print(response)
    res = purse_chat_response(response)

    print(res.choices[0].message.content)
