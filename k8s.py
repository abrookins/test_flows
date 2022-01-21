import os

from prefect.run_configs import KubernetesRun
from prefect import task, Flow
from prefect.storage import GCS, GitHub


@task
def nothing() -> None:
    print("hey!")


with Flow("test-k8s") as flow:
    nothing()


# Configure extra environment variables for this flow,
# and set a custom image
flow.run_config = KubernetesRun(
    env={
        "DELETE_FINISHED_JOBS": "False",
    }
)

flow.storage = GitHub(
    repo="abrookins/test_flows",
    path="k8s.py",
)
