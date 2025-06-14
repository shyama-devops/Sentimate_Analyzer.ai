from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()



@app.post("/webhook")
async def webhook(request: Request):
    try:
        payload = await request.json()  # Get the JSON body
        print(payload)  # For debugging
        return JSONResponse(content={"status": "success"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
