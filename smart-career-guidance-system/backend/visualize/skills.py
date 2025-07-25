import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

from backend.API.job_search import get_jobs_for_career  # implement as earlier

def extract_skills_from_jobs(career):
    jobs = get_jobs_for_career(career, location="India")
    skill_list = []
    for job in jobs:
        try:
            resp = requests.get(job['apply_link'], timeout=5)
            soup = BeautifulSoup(resp.text, 'html.parser')
            text = soup.get_text().lower()
            words = re.findall(r'\bpython\b|\breact\b|\bmachine learning\b|\baws\b|\bsql\b|\bexcel\b', text)
            skill_list.extend(words)
        except:
            continue
    return Counter(skill_list).most_common(10)

def get_top_companies(career):
    jobs = get_jobs_for_career(career, location="India")
    return Counter([j['company'] for j in jobs]).most_common(5)
