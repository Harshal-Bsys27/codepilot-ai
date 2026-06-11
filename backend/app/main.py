from fastapi import FastAPI

app = FastAPI(title="CodePilot AI")

@app.get("/")
def root():
    return {"message": "CodePilot AI Backend Running"}