import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def get_jobs_for_career(career: str, location="India"):
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    querystring = {
        "query": career,
        "page": "1",
        "num_pages": "1",
        "location": location
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()

        jobs = []
        for job in data.get("data", [])[:7]:
            jobs.append({
                "title": job.get("job_title", "Unknown Job"),
                "company": job.get("employer_name", "Unknown Company"),
                "location": job.get("job_city") or job.get("job_country", "Unknown Location"),
                "link": job.get("job_apply_link", "#")
            })

        return jobs

    except Exception as e:
        return [{"title": "Failed to fetch jobs", "company": "", "location": "", "link": "#", "error": str(e)}]
