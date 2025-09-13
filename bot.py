from telethon import TelegramClient, events, Button

# ====== Конфиг ======
API_ID = 20700040  # замени на свой
API_HASH = '92b7310b20ec6e0ce258b161b6cb21ab'  # замени на свой
BOT_TOKEN = '8289728540:AAHs_hmyzFSCXRdu56ltAYxDPsW4vD3jpzM'
ADMINS = [6922587576, 2035972933]
AUTHOR = '@unc999'

client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# ====== Стартовое сообщение ======
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        f"Привет! Этот бот создан для покупки ключей для читов Standoff 2 от автора {AUTHOR}",
        buttons=[
            [Button.inline("Купить ключ для читов", b"buy"), Button.inline("Техподдержка", b"support")]
        ]
    )

# ====== Обработка нажатий ======
@client.on(events.CallbackQuery)
async def callback(event):
    if event.data == b'buy':
        await event.edit(
            "Выберите страну и срок ключа:",
            buttons=[
                [Button.inline("Украина 🇺🇦", b"ukraine"), Button.inline("Россия 🇷🇺", b"russia")]
            ]
        )
    elif event.data == b'support':
        await event.edit("Связь с техподдержкой: t.me/grand_soft_so2")

    elif event.data == b'ukraine':
        await event.edit(
            "Цены для Украины:\n7 дней - 120 или 150₴\n30 дней - 280 или 300₴\nНавсегда - 750 или 800₴\n\nОплатить на карту: 4149609027541293"
        )
    elif event.data == b'russia':
        await event.edit(
            "Цены для РФ:\n7 дней - 250₽\n30 дней - 550₽\nНавсегда - 1499₽\n\nОплатить через криптобот: http://t.me/send?start=IVAr0ZG1s4RH"
        )

# ====== Запуск бота ======
print("Бот запущен...")
client.run_until_disconnected()
