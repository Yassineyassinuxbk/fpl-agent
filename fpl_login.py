import aiohttp
from fpl import FPL
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

EMAIL = os.getenv("FPL_EMAIL")
PASSWORD = os.getenv("FPL_PASSWORD")

def login():
    async def main():
        session = aiohttp.ClientSession()
        fpl = FPL(session)
        await fpl.login(EMAIL, PASSWORD)
        return fpl

    return asyncio.get_event_loop().run_until_complete(main())
