import asyncio
from time import perf_counter
from random import randint
from typing import AsyncIterable

from utils.req_http import http_get

# The highest Pokemon id
MAX_POKEMON = 898


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


async def main():

    # retrieve the next 10 pokemon names
    time_before = perf_counter()
    async for name in next_pokemon(10):
        print(name)
    print(f"Total time: {perf_counter() - time_before}")

    time_before = perf_counter()
    # asynchronous list comprehensions
    names = [name async for name in next_pokemon(10)]
    print(names)
    print(f"Total time: {perf_counter() - time_before}")



asyncio.run(main())
