from http.client import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Depends, HTTPException, status, Path


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    if token != "my-secret-api-key-123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return "authorized_user"

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/jobs/{job_id}", dependencies=[Depends(verify_token)])
def jobs(job_id: int):
    return {"job_id": job_id}

@app.get("/search", dependencies=[Depends(verify_token)])
def clusters(name: str, tag: str):
    return {"name": name, "tag": tag}

@app.get("/list/{entity}", dependencies=[Depends(verify_token)])
def list_profiles(entity: str = Path(..., regex="^(users|profiles)$")):
    data = {
        "users": {
            "sudhir_singh": {"place": "Mumbai"},
            "navin": {"place": "Andhra Pradesh"},
        },
        "profiles": {
            "navin_singh": {"place": "Mumbai"},
            "navin": {"place": "Andhra Pradesh"},
        }
    }
    return {entity: data[entity]}
