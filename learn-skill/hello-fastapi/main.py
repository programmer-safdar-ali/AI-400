"""FastAPI Hello World Application."""

from fastapi import FastAPI

app = FastAPI(
    title="Hello FastAPI",
    description="A simple hello world FastAPI application",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint returning a hello world message."""
    return {"message": "Hello, World!"}

@app.get("/t/todos")
def todo() -> list[dict[str,int|str]]:
    return [{"id":1,"task":"buy the book"},
            {"id":2,"task":"Now read the book"}]
@app.get("/t/todos/{task_id}")
async def todo_by_id(task_id:int,include_details: bool = False):
    if task_id<0:
        return{"error":"Task_Id must be greater than 0"}
    if include_details:
        return[
            {"id":task_id,
             "todos":"Do Something meaningful",
             "details":"Like Prgramming"}
        ]
    return [
        {
            "id":task_id,
             "todos":"Do Something meaningful",
        }
    ]

@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
