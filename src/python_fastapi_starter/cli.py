import os

import uvicorn


def main() -> None:
    uvicorn.run(
        "python_fastapi_starter.main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("RELOAD", "true").lower() == "true",
    )
