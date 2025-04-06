import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties

logging.basicConfig(level=logging.INFO)

# Вставь сюда свой токен
TOKEN = "8094199490:AAFDXH48wy23NXnlxM7lm9AktdzSadcOevw"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

# Данные поддержки
support_data = {
    "sad": {
        "phrases": [
            "💙 Всё пройдёт. Даже это.",
            "🫂 Ты не один, и твои чувства важны.",
            "😌 Мы никогда не испытываем идеальной радости; наши самые счастливые достижения смешиваются с грустью",
            "💔 Знаешь, у тебя в голове всего один стакан со слезами. Если будешь лить их по пустякам, когда по-настоящему понадобится, слез не останется."
        ],
        "tips": [
            "• Напиши, что ты чувствуешь — это разгрузит ум.",
            "• Погуляй на свежем воздухе хотя бы 10 минут.",
            "• Включи любимую музыку или обними что-то мягкое."
        ],
        "video": "https://youtu.be/yhjDHngUmkE"  # Ссылка на видео для этой темы
    },
    "tired": {
        "phrases": [
            "🛏 Ты не обязан быть продуктивным всё время.",
            "😌 Отдых — это тоже часть прогресса.",
            "⚡🌟 Отдых необходим, чтобы перезарядить свои батарейки, чтобы в дальнейшем вы могли прыгать выше и сиять ярче.",
            "🌿💭 Иногда лучше всего сделать шаг назад, дышать, дать отдых разуму и подойти к делу со свежей точки зрения."
        ],
        "tips": [
            "• Сделай перерыв от экрана и выпей воды.",
            "• Ляг, закрой глаза на 5 минут и просто дыши.",
            "• Раздели дела на маленькие шаги — не нужно всё сразу."
        ],
        "video": "https://youtu.be/iVDmCvG5kg8"  # Ссылка на видео для этой темы
    },
    "anxiety": {
        "phrases": [
            "🧘 Ты дышишь — ты жив, и это уже победа.",
            "🫀 Всё хорошо. Ты в безопасности прямо сейчас.",
            "🌸🌱 Тревога — это всего лишь момент в тебе. Сделай паузу, вдохни глубоко и помни, что всё пройдёт.",
            "💧💭 Когда тревога переполняет, остановись и напомни себе: ты сильнее своих мыслей. Всё будет хорошо."
        ],
        "tips": [
            "• Попробуй технику 5-4-3-2-1 (что вижу, слышу и т.д.).",
            "• Сделай дыхание: вдох на 4, задержка на 4, выдох на 4.",
            "• Опиши тревожные мысли на бумаге."
        ],
        "video": "https://youtu.be/teuQGZQ3SQU"  # Ссылка на видео для этой темы
    },
    "motivation": {
        "phrases": [
            "🚀 Маленький шаг лучше, чем стояние на месте.",
            "🌟 Ты можешь больше, чем тебе кажется.",
            "🚀🔥 Маленький шаг сегодня — это гигантский прыжок завтра.",
            "💪🌟 Ты способен на большее, чем думаешь. Каждый день — это шанс стать лучше."
        ],
        "tips": [
            "• Напиши 3 цели на день и начни с самой простой.",
            "• Перестань ждать вдохновения — начни делать.",
            "• Подумай, почему ты начал. Это вернёт фокус."
        ],
        "video": "https://youtu.be/08AxYAerX5k"  # Ссылка на видео для этой темы
    },
    "confidence": {
        "phrases": [
            "💪 Ты — сила. Даже если пока в это не веришь.",
            "🔊 Твой голос важен. Не молчи о своих идеях.",
            "💪✨ Верь в себя, даже когда другие сомневаются. Ты уже сильнее, чем ты думаешь.",
            "🌟🔊 Твоя уверенность начинается с принятия себя таким, какой ты есть. Ты достоин быть услышанным."
        ],
        "tips": [
            "• Прими позу уверенности: расправь плечи, выпрями спину.",
            "• Запиши 5 своих сильных сторон.",
            "• Представь себя через год — и действуй уже сегодня."
        ],
        "video": "https://youtu.be/kGHjwKbfYWs"  # Ссылка на видео для этой темы
    }
}

# Кнопки
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="😢 Мне грустно", callback_data="sad")],
    [InlineKeyboardButton(text="😴 Я устал(а)", callback_data="tired")],
    [InlineKeyboardButton(text="🧠 У меня тревога", callback_data="anxiety")],
    [InlineKeyboardButton(text="🚀 Хочу вдохновение", callback_data="motivation")],
    [InlineKeyboardButton(text="💪 Хочу стать увереннее", callback_data="confidence")],
])

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! 💬 Я бот поддержки и мотивации.\n\n"
        f"Выбери, как ты себя чувствуешь:",
        reply_markup=keyboard
    )

@dp.callback_query()
async def handle(callback: types.CallbackQuery):
    key = callback.data
    if key in support_data:
        data = support_data[key]
        text = (
            f"<b>✨ Цитаты поддержки:</b>\n" +
            "\n".join(data["phrases"]) +
            "\n\n<b>🛠 Пути решения:</b>\n" +
            "\n".join(data["tips"]) +
            f"\n\n🎥 <i>Смотри видео для дополнительной мотивации:</i> {data['video']}"
        )
        await callback.message.answer(text, reply_markup=keyboard)
        await callback.answer()

    

@dp.message()
async def fallback(message: Message):
    await message.answer("Пожалуйста, выбери вариант из меню или напиши /start 🌟")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
