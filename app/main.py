from fastapi import FastAPI

app = FastAPI(title="PhishSim")


@app.get("/")
def inicio():
    return {"mensaje": "PhishSim funcionando"}