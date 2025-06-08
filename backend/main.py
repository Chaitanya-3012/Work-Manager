from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from app.api.routes import router
app = FastAPI()
app.include_router(router)
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Work Manager API"}


@app.get("/item")
async def root_item():
    return [{"id":"1", "name": "Item-1"}, {"id":"2", "name": "Item-2"}]