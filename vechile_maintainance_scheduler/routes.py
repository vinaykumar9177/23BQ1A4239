from fastapi import APIRouter
from fastapi import HTTPException

from auth import get_token
from services import get_depots
from services import get_vehicles
from scheduler import optimize_tasks

from logger import log
router = APIRouter()


@router.get("/")
async def home():

    return {
        "message": "Vehicle Maintenance Scheduler Running"
    }


@router.get("/schedule")
async def schedule():

    try:

        token = await get_token()

        await log(
            token,
            "info",
            "route",
            "Schedule generation started"
        )

        depots = await get_depots(token)

        vehicles = await get_vehicles(token)

        result = []

        for depot in depots:

            await log(
                token,
                "info",
                "service",
                f"Optimizing depot {depot['ID']}"
            )

            selected_tasks = optimize_tasks(
                vehicles,
                depot["MechanicHours"]
            )

            result.append(
                {
                    "depotId": depot["ID"],
                    "mechanicHours":
                    depot["MechanicHours"],

                    "selectedTasks":
                    [
                        task["TaskID"]
                        for task in selected_tasks
                    ]
                }
            )

        await log(
            token,
            "info",
            "route",
            "Schedule generation completed"
        )

        return result

    except Exception as e:

        try:
            token = await get_token()

            await log(
                token,
                "error",
                "handler",
                str(e)
            )

        except:
            pass

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )