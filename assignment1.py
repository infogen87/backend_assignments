



# The assignment:
# Create a fastapi app exposing an only one endpoint to create users with the following data:
#  First Name
#  Last Name
#  Age
#  Email
#  Height

# Notes:
#  Make sure to use the right payload content type
#  Use the appropriate status codes
#  Use in-memory storage to store responses
#  Add a CORS middleware to allow only http:localhost:8000 (your localhost origin)
#  Add a logger middleware to print to the console the time taken for a request to complete.
#  Put your code in a Github repo and submit using this link



from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from time import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"]
)

user_storage = [] 
class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str
    height: float

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    print(f"Request completed in {process_time:.4f} seconds")
    return response

@app.post("/users", status_code=201)
async def create_user(user: User):
    user_storage.append(user)
    
    return {"message": "User created successfully"}