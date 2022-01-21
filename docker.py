import os

from prefect import task, Flow
from prefect.storage import GitHub


@task
def nothing() -> None:
    print("hey!")


with Flow("test-docker") as flow:
    nothing()


flow.storage = GitHub(
    repo="abrookins/test_flows",
    path="docker.py",
)
