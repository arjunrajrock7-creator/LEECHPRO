from ...core.tg_client import TgClient
from ...core.config_manager import Config
from ...helper.ext_utils.bot_utils import new_task
from ...helper.telegram_helper.bot_commands import BotCommands
from ...helper.telegram_helper.filters import CustomFilters
from ...helper.telegram_helper.message_utils import send_message, delete_links
from .mirror_leech import Mirror

@new_task
async def zipmerge(client, message):
    if not Config.ENABLE_ZIP_PIPELINE:
        return await send_message(message, "Zip Pipeline is disabled in Config!")

    obj = Mirror(client, message, is_leech=True, is_zip_pipeline=True)
    obj.extract = True # Zip Pipeline implies extraction
    await obj.new_event()

# No need to register here, it's registered in handlers.py
