from elasticsearch import Elasticsearch
import time

es = Elasticsearch("http://localhost:9200")

def wait_for_es():
    print("Waiting for Elasticsearch to be ready...")
    for _ in range(30):
        try:
            if es.ping():
                return True
        except:
            pass
        time.sleep(1)
    return False

def seed_data():
    if not wait_for_es():
        print("Elasticsearch is not available.")
        return

    index_name = "jobs"
    
    # Delete index if it exists
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    
    # Create index with mapping
    mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "integer"},
                "title": {"type": "text"},
                "company": {"type": "text"},
                "location": {"type": "text"},
                "type": {"type": "keyword"},
                "salary": {"type": "text"},
                "postedAt": {"type": "text"}
            }
        }
    }
    es.indices.create(index=index_name, body=mapping)
    
    # Mock data
    jobs = [
        {
            "id": 1,
            "title": "Senior Frontend Engineer",
            "company": "TechFlow",
            "location": "Remote",
            "type": "Full-time",
            "salary": "$120k - $160k",
            "postedAt": "2 days ago",
        },
        {
            "id": 2,
            "title": "Product Designer",
            "company": "CreativeCo",
            "location": "New York, NY",
            "type": "Full-time",
            "salary": "$100k - $140k",
            "postedAt": "1 day ago",
        },
        {
            "id": 3,
            "title": "Backend Developer",
            "company": "DataSys",
            "location": "Austin, TX",
            "type": "Contract",
            "salary": "$80 - $100 / hr",
            "postedAt": "4 hours ago",
        },
        {
            "id": 4,
            "title": "Elasticsearch Specialist",
            "company": "SearchMaster",
            "location": "Remote",
            "type": "Full-time",
            "salary": "$140k - $180k",
            "postedAt": "Just now",
        }
    ]
    
    for job in jobs:
        es.index(index=index_name, id=job['id'], body=job)
    
    es.indices.refresh(index=index_name)
    print(f"Successfully seeded {len(jobs)} jobs into Elasticsearch.")

if __name__ == "__main__":
    seed_data()
