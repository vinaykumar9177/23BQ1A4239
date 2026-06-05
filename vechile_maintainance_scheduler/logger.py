import httpx

LOG_URL = "http://4.224.186.213/evaluation-service/logs"


async def log(token, level, package, message):
    payload = {
        "stack": "backend",
        "level": level,
        "package": package,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                LOG_URL,
                json=payload,
                headers=headers
            )
    except Exception as e:
        print("Logging failed:", e)