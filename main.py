from fastapi import FastAPI, HTTPException
from database import database, metadata, engine
from models import tasks

# Vytvoření tabulek
metadata.create_all(engine)

app = FastAPI(title="Simple Task API")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Vytvoření úkolu
@app.post("/tasks/")
async def create_task(title: str, description: str = ""):
    query = tasks.insert().values(title=title, description=description, completed=False)
    task_id = await database.execute(query)
    return {"id": task_id, "title": title, "description": description, "completed": False}

# Získání všech úkolů
@app.get("/tasks/")
async def get_tasks():
    query = tasks.select()
    return await database.fetch_all(query)

# Získání úkolu podle ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Aktualizace úkolu
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, title: str = None, description: str = None, completed: bool = None):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = {}
    if title is not None: update_data["title"] = title
    if description is not None: update_data["description"] = description
    if completed is not None: update_data["completed"] = completed
    query = tasks.update().where(tasks.c.id == task_id).values(**update_data)
    await database.execute(query)
    return {**task, **update_data}

# Smazání úkolu
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {"message": f"Task {task_id} deleted"}

