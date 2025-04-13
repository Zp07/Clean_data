from fastapi import APIRouter

router = APIRouter()

@router.get("/clean")
def health_check():
    return {"status": "ok"}