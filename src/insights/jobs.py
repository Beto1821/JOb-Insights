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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
