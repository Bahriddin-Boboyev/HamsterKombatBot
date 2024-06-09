import aiohttp
from typing import Any

from bot.api.http import handle_error, make_post_request
from bot.utils.scripts import get_fingerprint


async def login(
    http_client: aiohttp.ClientSession, tg_web_data: str, session_name: str
) -> Any | None:
    try:
        fingerprint = get_fingerprint(name=session_name)
        response_json = await make_post_request(
            http_client,
            'https://api.hamsterkombat.io/auth/auth-by-telegram-webapp',
            {'initDataRaw': tg_web_data, 'fingerprint': fingerprint},
            'getting Access Token',
        )
        access_token = response_json.get('authToken')
        return access_token
    except Exception as error:
        await handle_error(error, '', 'getting Access Token')
        return None
