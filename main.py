from fastapi import FastAPI, Request 
from db_config import engine
import pandas as pd
from utils import summarize
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def run_query(request: Request):
    body = await request.json()
    query = body.get("query", "")

    try:
        df = pd.read_sql(query, engine)
        summary = summarize(df)

        return {
            "status": "success",
            "columns": list(df.columns),
            "rows": df.to_dict(orient="records"),
            "summary": summary
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

