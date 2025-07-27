import asyncio
from aiogram import Bot, Dispatcher, types
from config import TELEGRAM_TOKEN, OPENAI_API_KEY
import openai
from openai import AsyncOpenAI

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

with open("prompt.txt", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

async def get_yaga_reply(user_message: str) -> str:
    chat = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        temperature=0.9
    )
    return chat.choices[0].message.content.strip()

@dp.message(types.Message)
async def handle_msg(message: types.Message):
    text = message.text.strip()
    if text == "/пинок":
        prompt = "Дай пинок под пятку."
    elif text == "/отвар":
        prompt = "Завари отвар с рефлексией."
    elif text == "/урок":
        prompt = "Дай короткий бабкин урок."
    else:
        prompt = text

    reply = await get_yaga_reply(prompt)
    await message.reply(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
