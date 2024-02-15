import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
thread_id = os.getenv('ASSISTANTS_THREAD_ID')
assistants_id = os.getenv('ASSISTANTS_ID')
runs= client.beta.threads.runs.list(thread_id=thread_id)
print(runs)

run_steps = client.beta.threads.runs.steps.list(
    thread_id=thread_id,
    run_id=runs.data[0].id
)
print(run_steps)
