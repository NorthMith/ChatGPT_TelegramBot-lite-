import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TELEGRAM_TOKEN, OPENAI_API_KEY, AUTHORIZED_USERS

token = TELEGRAM_TOKEN
openai.api_key = OPENAI_API_KEY

bot = Bot(token)
dp = Dispatcher(bot)

async def is_authorized(user_id):
    if not AUTHORIZED_USERS or user_id in AUTHORIZED_USERS:
        return True
    return False

async def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=0.9,
        frequency_penalty=0.5,
        presence_penalty=0.6,
        stop=["You:"]
    )
    return response['choices'][0]['text']

@dp.message_handler()
async def send(message: types.Message):
    if not await is_authorized(message.from_user.id):
        await message.answer("Sorry, you don't have permission to use this bot.")
        return

    conversation_history = f"User: {message.text}\nAI:"
    response = await generate_response(conversation_history)
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
