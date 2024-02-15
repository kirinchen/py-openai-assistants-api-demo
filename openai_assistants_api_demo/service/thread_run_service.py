import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.beta import Thread

load_dotenv()

client = OpenAI()

THREAD_ID = os.getenv('ASSISTANTS_THREAD_ID')
ASSISTANTS_ID = os.getenv('ASSISTANTS_ID')


def create_thread() -> Thread:
    thread = client.beta.threads.create()
    return thread


def delete_thread():
    client.beta.threads.delete(thread_id=THREAD_ID)


def create_message() -> tuple:
    message = client.beta.threads.messages.create(
        thread_id=THREAD_ID,
        role="user",
        content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    )
    run = client.beta.threads.runs.create(
        thread_id=THREAD_ID,
        assistant_id=ASSISTANTS_ID,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )
    return message, run


def get_run_status(run_id: str):
    run = client.beta.threads.runs.retrieve(
        thread_id=THREAD_ID,
        run_id=run_id
    )
    return run


def list_messages():
    messages = client.beta.threads.messages.list(
        thread_id=THREAD_ID
    )
    return messages


if __name__ == '__main__':
    # resp = create_message()
    # print(resp)
    # run_id = 'run_Ypu7BxRrgJNc2nmuLZvQyuzv'  msg_id= 'msg_Ex1KpuPEseIqEa416C5r5vnd'
    # run_resp = get_run_status('run_Ypu7BxRrgJNc2nmuLZvQyuzv')
    # print(run_resp)
    messages = list_messages()
    print(messages)
