import httpx

from config import BASE_URL
from logger import log
async def get_depots(token):

    await log(
        token,
        "info",
        "service",
        "Fetching depots"
    )

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/depots",
            headers=headers
        )

        response.raise_for_status()

        depots = response.json()["depots"]

    await log(
        token,
        "info",
        "service",
        f"Fetched {len(depots)} depots"
    )

    return depots


async def get_vehicles(token):

    await log(
        token,
        "info",
        "service",
        "Fetching vehicles"
    )

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{BASE_URL}/vehicles",
            headers=headers
        )

        response.raise_for_status()

        vehicles = response.json()["vehicles"]

    await log(
        token,
        "info",
        "service",
        f"Fetched {len(vehicles)} vehicles"
    )

    return vehicles