import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
thread_id = os.getenv('ASSISTANTS_THREAD_ID')
assistants_id = os.getenv('ASSISTANTS_ID')
print(thread_id)

if __name__ == '__main__':
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )
    print(messages)
