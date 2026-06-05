import httpx

from config import (
    EMAIL,
    NAME,
    ROLL_NO,
    ACCESS_CODE,
    CLIENT_ID,
    CLIENT_SECRET
)

AUTH_URL = "http://4.224.186.213/evaluation-service/auth"


async def get_token():

    payload = {
        "email": EMAIL,
        "name": NAME,
        "rollNo": ROLL_NO,
        "accessCode": ACCESS_CODE,
        "clientID": CLIENT_ID,
        "clientSecret": CLIENT_SECRET
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            AUTH_URL,
            json=payload
        )

        response.raise_for_status()

        data = response.json()

        return data["access_token"]