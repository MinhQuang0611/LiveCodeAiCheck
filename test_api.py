import sys
import os
import asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.srv_chatbot import fetch_unit_info

async def test():
    print("Testing external API fetch...")
    res = await fetch_unit_info("string")
    print("RESULT:")
    print(repr(res))

if __name__ == "__main__":
    asyncio.run(test())
