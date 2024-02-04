from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message

from config import SUPPORT_CHAT,OWNER_ID


keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="بدا استخراج الجلسة 🖥️", callback_data="gensession")
                    ],
                    [
                    InlineKeyboardButton("سـورس مافيا - Mafia", url="https://t.me/MAZADmafia")
                    ],
                    [
                    InlineKeyboardButton(" الـمـطـور", url="t.me/T_O_Xl"),
                ],
                [
                    InlineKeyboardButton("الـمـطـور🦅", user_id=OWNER_ID),
                    InlineKeyboardButton("جـروب الدعم", url="https://t.me/lajdjda")
                ]
            ]
        )

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="بايروجورام v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايروجورام v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="استخرج مجدداً", callback_data="gensession")]]
)
