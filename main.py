# chal ab httpx seekhtey hain yeah actually mein woh hai so async ke sath me rehke urls resquests handle karta 


import asyncio
import httpx

async def fetch_post(client: httpx.AsyncClient, post_id: int) -> dict:
    response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    response.raise_for_status()  # Raises on 4xx/5xx
    return response.json()

async def main():

    async with httpx.AsyncClient(timeout = 10.0) as client :
        async with asyncio.TaskGroup() as tg :
            tasks = [
                tg.create_task(fetch_post(client, i ) )
                for i in range (1,6)
            ]

    results = [t.result() for t in tasks]
    print(f"fetched {len(results)} posts concurrently")


asyncio.run(main())