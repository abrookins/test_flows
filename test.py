import os

from prefect.run_configs import KubernetesRun
from prefect import task, Flow
from prefect.storage import GCS



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
        "PREFECT__CLOUD__API_KEY": os.environ["CLOUD_API_KEY"],
        "IMAGE_PULL_SECRETS": ""
    }
)

flow.storage = GitHub(
    repo="abrookins/test_flows",
    path="k8s.py"
)
