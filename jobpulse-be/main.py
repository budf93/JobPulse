from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import Elasticsearch
import os

app = FastAPI(title="JobPulse API")

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Default Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Elasticsearch client
es = Elasticsearch("http://localhost:9200")

@app.get("/search")
async def search_jobs(q: str = Query(None)):
    index_name = "jobs"
    
    if not q:
        # Match all if no query
        body = {"query": {"match_all": {}}}
    else:
        # Multi-match query across title, company, and location
        body = {
            "query": {
                "multi_match": {
                    "query": q,
                    "fields": ["title^3", "company^2", "location", "type", "description"]
                }
            }
        }
    
    try:
        response = es.search(index=index_name, body=body)
        hits = response['hits']['hits']
        return [hit['_source'] for hit in hits]
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
async def health_check():
    return {"status": "ok", "elasticsearch": es.ping()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
