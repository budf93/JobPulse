from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch import AsyncElasticsearch
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
ES_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
es = AsyncElasticsearch(ES_URL)

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
        # ADD AWAIT HERE:
        response = await es.search(index=index_name, body=body) 
        hits = response['hits']['hits']
        return [hit['_source'] for hit in hits]
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    is_connected = await es.ping() 
    return {"status": "ok", "elasticsearch": is_connected}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
