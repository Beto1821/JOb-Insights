from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    for job in jobs:
        assert job.keys() == {"title", "salary", "type"}
