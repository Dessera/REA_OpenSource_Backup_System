from tortoise import Tortoise

from config import database


async def init():
    await Tortoise.init(db_url=database.url, modules={"models": ["rea_db.models.user"]})
    # await Tortoise.generate_schemas()


async def generate_schemas():
    await Tortoise.generate_schemas()
