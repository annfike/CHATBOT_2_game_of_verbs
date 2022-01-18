import os
from pydoc_data.topics import topics
from google.cloud import dialogflow
from dotenv import load_dotenv
import json


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))

# topics = {
#     "Устройство на работу": {
#         "questions": [
#             "Как устроиться к вам на работу?",
#             "Как устроиться к вам?",
#             "Хочу работать редактором у вас"
#         ],
#         "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
#     },
#     "Забыл пароль": {
#         "questions": [
#             "Не помню пароль",
#             "Не могу войти",
#             "Не могу войти в аккаунт"
#         ],
#         "answer": "Если вы не можете войти на сайт, воспользуйтесь кнопкой «Забыли пароль?» под формой входа. Вам на почту прийдёт письмо с дальнейшими инструкциями. Проверьте папку «Спам», иногда письма попадают в неё."
#     }
# }

# for topic, questions_answer in topics.items():
#     print(topic)
#     print(questions_answer["questions"])
#     print(questions_answer["answer"])
#     questions = questions_answer["questions"]
#     answer = [(questions_answer["answer"])]
#     create_intent('annfike-nthn', topic, questions, answer)

with open("phrases.json", "r", encoding='utf-8') as file:
    topics = json.load(file)

load_dotenv()
os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
for topic, questions_answer in topics.items():
    questions = questions_answer["questions"]
    answer = [(questions_answer["answer"])]
    create_intent('annfike-nthn', topic, questions, answer)