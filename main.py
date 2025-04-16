from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/jobs/{job_id}")
def jobs(job_id: int):
    return {"job_id": job_id}