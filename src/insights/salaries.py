from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:

    data = read(path)
    salaries = []
    for job in data:
        if job["max_salary"].isdigit():
            salaries.append(int(job["max_salary"]))
    return max(salaries)

# print(get_max_salary("data/jobs.csv"))


def get_min_salary(path: str) -> int:

    data = read(path)
    salaries = []
    for job in data:
        if job["min_salary"].isdigit():
            salaries.append(int(job["min_salary"]))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    try:
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        salary = int(salary)
    except Exception:
        raise ValueError

    if min > max:
        raise ValueError

    return salary in range(min, max)


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filter_jobs = []
    for job in jobs:
        try:
            matches_salary = matches_salary_range(job, salary)

            if matches_salary:
                filter_jobs.append(job)
        except ValueError:
            pass
    return filter_jobs
