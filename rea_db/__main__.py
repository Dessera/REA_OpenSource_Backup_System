import asyncio

from . import init, generate_schemas


async def main():
    await init()
    await generate_schemas()

    # if __name__ == "__main__":


asyncio.run(main())
