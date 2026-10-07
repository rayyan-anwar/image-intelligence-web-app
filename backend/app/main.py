from fastapi import FastAPI
app=FastAPI(title="Rayyan Anwar | Image Intelligence API")
@app.get("/health")
def health(): return {"status":"ok","author":"Rayyan Anwar"}
