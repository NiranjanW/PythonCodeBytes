import asyncio
import aiohttp
import timeit

async def async_func(N, func , *args){
    coros = [func(*args) for _ in range(N)]
    # run awaitable objects concurrently
    await asyncio.gather(*coros)
}

async def a_cpu_bound(a, b):
    result = await loop.run_in_executor(None, cpu_bound, a, b)
    return result


async def a_io_bound(urls):
    # create a coroutine function where we will download from individual url
    async def download_coroutine(session, url):
        async with session.get(url, timeout=10) as response:
            await response.text()

    # set an aiohttp session and download all our urls
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            await download_coroutine(session, url)


if __name__ == '__main__':
    ...
    loop = asyncio.get_event_loop()
    with timeit():
        loop.run_until_complete(async_func(10, a_cpu_bound, a, b))

    with timeit():
        loop.run_until_complete(async_func(10, a_io_bound, urls))