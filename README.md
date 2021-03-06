# Боты техподдержки - в Телеграм и Вконтакте

Сервис для технической поддержки в чат-ботах в Телеграм и в группе Вконтакте на основе сервиса [DialogFlow](https://dialogflow.cloud.google.com).

Чат бот в Телеграм, [пример](https://t.me/annfikeBot).

![Чат бот в Телеграм](https://github.com/annfike/CHATBOT_2_game_of_verbs/blob/main/tg.gif)

Чат бот Вконтакте, [пример](https://vk.com/gim209206220?sel=95751465). 

![Чат бот Вконтакте](https://github.com/annfike/CHATBOT_2_game_of_verbs/blob/main/vk.gif)

## Как установить
### 1. Скрипт для обучения DialogFlow

 - Для использования сервиса DialogFlow необходимо:
    - [создать проект в DialogFlow](https://cloud.google.com/dialogflow/es/docs/quick/setup)
    - получить идентификатор проекта и присвоить его переменной окружения в файле '.env':
    ```python
   PROJECT_ID=Ваш идентификатор проекта
   ```
    - [создать агента](https://cloud.google.com/dialogflow/es/docs/quick/build-agent)
    - [создать JSON-ключ](https://cloud.google.com/docs/authentication/getting-started) и сохранить его в     папку с проектом
    - путь до файла с ключами присвоить переменной окружения в файле '.env':
    ```python
   GOOGLE_APPLICATION_CREDENTIALS='Ваш_файл.json'
   ```
    - создать файл в папке проекта phrases.json с вопросами и ответом на них в формате:
    ```
    {
    'Тема 1': {
        'questions': [
            'вопрос 1',
            'вопрос 2',
            ...
        ],
        'answer': 'ответ'
    },
   }
   ```
 - Python3 должен быть уже установлен.
 - Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```python
   pip install -r requirements.txt
   ```
   - Для запуска скрипта используйте команду:
```python
   python create_intent.py
```

### 2. Скрипт для чат-бота в Телеграм
- Для использования скрипта необходимо [создать Телеграм-бота](https://telegram.me/BotFather) для чата техподдержки и Телеграм-бота для администрирования и получить от них токены, а также узнать ваш chat_id в Телеграме.
 - Полученные данные присвоить переменным окружения в файле '.env':
```python
   TG_BOT_TOKEN=Ваш Токен
   TG_BOT_ADMIN_TOKEN=Ваш Токен
   CHAT_ID=ваш chat_id в Телеграме
```
 - Python3 должен быть уже установлен.
 - Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```python
   pip install -r requirements.txt
   ```
 - Для запуска скрипта используйте команду:
```python
   python tg.py
```

### 3. Скрипт для чат-бота Вконтакте

 - Для использования скрипта необходимо:
    - [создать Телеграм-бота](https://telegram.me/BotFather) для администрирования и получить от него токен, а также узнать ваш chat_id в Телеграме.
    - зарегистрироваться на сайте [Вконтакте](https://vk.com/)
    - создать группу в разделе [Управление группами](https://vk.com/groups?tab=admin)
    - В меню 'Работа с API' создать токен
    - полученные данные присвоить переменным окружения в файле '.env':
```python
   VK_TOKEN=Ваш Токен
   TG_BOT_ADMIN_TOKEN=Ваш Токен
   CHAT_ID=ваш chat_id в Телеграме
```
 - Python3 должен быть уже установлен.
 - Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```python
   pip install -r requirements.txt
   ```
 - Для запуска скрипта используйте команду:
```python
   python vk.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
