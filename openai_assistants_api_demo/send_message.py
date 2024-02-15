import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
thread_id = os.getenv('ASSISTANTS_THREAD_ID')
assistants_id = os.getenv('ASSISTANTS_ID')
print(thread_id)
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
print(message)

run = client.beta.threads.runs.create(
  thread_id=thread_id,
  assistant_id=assistants_id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

messages = client.beta.threads.messages.list(
  thread_id=thread_id
)
print(messages)