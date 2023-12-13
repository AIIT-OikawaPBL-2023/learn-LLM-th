#!/usr/bin/env python3

import sys
import os
from dotenv import load_dotenv

import openai

# add import path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


if __name__ == "__main__":
    from openai_st import purse_chat_response

    load_dotenv()
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello! I'm John."}],
    )

    response = purse_chat_response(response)
