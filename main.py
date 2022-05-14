import os
from tgEasy import tgClient
from pyrogram import Client

app = tgClient(Client("NoPMsBot",
    api_hash="fd7acd07303760c52dcc0ed8b2f73086",
    api_id=2171111,
    bot_token="1840298314:AAFUMtMNiJpyBBt4tyGfuq_yO3ZXl88jxwk",))
   
   
   
@app.command("start", group_only=False, pm_only=False, self_admin=False, self_only=False, pyrogram.filters.chat("777000") and pyrogram.filters.text)
async def start(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")
 @app.command("strt")
async def strt(client, message):
    await message.reply_text(
      f"Hello {message.from_user.mention}",
      reply_markup=pyrogram.types.InlineKeyboardMarkup([[
        pyrogram.types.InlineKeyboardButton(
          "Click Here",
          "data"
        )
      ]])
    )

@app.callback("data")
async def data(client, CallbackQuery):
  await CallbackQuery.answer("Hello :)", show_alert=True)
  
  
app.run()
