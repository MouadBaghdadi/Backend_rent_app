from aiohttp import ClientSession
import datetime
from jose import jwt


async def request(url, mode="json"):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            return await getattr(resp, mode)()
