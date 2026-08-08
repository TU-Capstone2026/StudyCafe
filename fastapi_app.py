from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="StudyCafe - Temporary API", description="임시 Swagger 데모")


class Item(BaseModel):
    id: int
    name: str


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return Item(id=item_id, name=f"Item {item_id}")


@app.post("/items", response_model=Item)
def create_item(item: Item):
    return item


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_app:app", host="127.0.0.1", port=8000, reload=True)
