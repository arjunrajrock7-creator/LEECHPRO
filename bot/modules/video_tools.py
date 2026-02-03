from pyrogram.handlers import CallbackQueryHandler
from pyrogram.filters import regex

from ..core.tg_client import TgClient
from ..helper.telegram_helper.message_utils import edit_message
from ..helper.ext_utils.bot_utils import new_task

@new_task
async def vt_callback(_, query):
    data = query.data.split()
    mid = data[1]
    action = data[2]

    if action == "done":
        await edit_message(query.message, "✅ <b>Video processing complete (or skipped). Starting upload...</b>")
        # In a real bot, we would signal the task to continue.
    elif action == "cancel":
        await edit_message(query.message, "❌ <b>Video processing cancelled.</b>")
    else:
        await query.answer(f"Action {action} selected. This is a premium ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ feature!", show_alert=True)

TgClient.bot.add_handler(CallbackQueryHandler(vt_callback, filters=regex("^vt")))
