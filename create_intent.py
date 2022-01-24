import os
from pydoc_data.topics import topics
from google.cloud import dialogflow
from dotenv import load_dotenv
import json


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )
    response = intents_client.create_intent(
        request={'parent': parent, 'intent': intent}
    )
    print("Intent created: {}".format(response))


with open('phrases.json', 'r', encoding='utf-8') as file:
    topics = json.load(file)

load_dotenv()
project_id = os.getenv('PROJECT_ID')
os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
for topic, questions_answer in topics.items():
    questions = questions_answer['questions']
    answer = [(questions_answer['answer'])]
    create_intent(project_id, topic, questions, answer)