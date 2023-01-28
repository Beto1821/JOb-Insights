from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path) as file:
        return list(csv.DictReader(file))


def get_unique_job_types(path: str) -> List[str]:

    data = read(path)
    job_types = []
    for job in data:
        if job["job_type"] != "" and job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


# print(get_unique_job_types("data/jobs.csv"))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:

    jobinho = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobinho.append(job)
    return jobinho
