# ChatGPT Telegram Bot Lite

This project is a simple Telegram bot that utilizes GPT-3 from OpenAI to generate responses to user messages. The bot is built using the Aiogram library and communicates with the OpenAI API.

## Files

### main.py

This file contains the main logic of the Telegram bot. It sets up the bot using the Aiogram library, checks if a user is authorized to use the bot, and generates responses to user messages using the GPT-3 model from OpenAI.

### config.py

This file contains configuration settings for the bot, such as the Telegram token, OpenAI API key, and an optional list of authorized users.

## Setup

1. Install the required Python packages: `pip install -r requirements.txt`
2. Replace `YOUR_TELEGRAM_TOKEN_HERE` and `YOUR_OPENAI_API_HERE` in `config.py` with your actual Telegram bot token and OpenAI API key.
3. (Optional) Add user IDs to the `AUTHORIZED_USERS` list in `config.py` if you want to restrict access to specific users.
4. Run the bot: `python main.py`

---

# Чат-бот GPT на Телеграмме (Lite версия)

Этот проект представляет собой простой телеграм-бот, который использует GPT-3 от OpenAI для генерации ответов на сообщения пользователей. Бот создан с использованием библиотеки Aiogram и взаимодействует с API OpenAI.

## Файлы

### main.py

Этот файл содержит основную логику телеграм-бота. В нем настраивается бот с помощью библиотеки Aiogram, проверяется, авторизован ли пользователь для использования бота, и генерируются ответы на сообщения пользователей с помощью модели GPT-3 от OpenAI.

### config.py

Этот файл содержит настройки конфигурации для бота, такие как токен Телеграм, ключ API OpenAI и дополнительный список авторизованных пользователей.

## Настройка

1. Установите необходимые пакеты Python: `pip install -r requirements.txt`
2. Замените `YOUR_TELEGRAM_TOKEN_HERE` и `YOUR_OPENAI_API_HERE` в `config.py` на ваш действительный токен телеграм-бота и ключ API OpenAI.
3. (Необязательно) Добавьте идентификаторы пользователей в список `AUTHORIZED_USERS` в `config.py`, если вы хотите ограничить доступ к определенным пользователям.
4. Запустите бот: `python main.py`