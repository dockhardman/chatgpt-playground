from fastapi import APIRouter


router = APIRouter()


@router.post("/conversation")
async def conversation():
    """ChatGPT conversation endpoint."""

    return {"OK"}
