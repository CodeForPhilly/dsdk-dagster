import dagstermill as dm
from dagster_examples.util import download_file
from dagster import execute_pipeline, pipeline, solid

from dagster import DependencyDefinition, InputDefinition, Path, PipelineDefinition
from dagster.utils import script_relative_path

k_means_iris_solid = dm.define_dagstermill_solid(
    "k_means_iris",
    script_relative_path("dagster_examples/iris-kmeans.ipynb"),
    input_defs=[
        InputDefinition("path", Path, description="Local path to the Iris dataset")
    ],
)


@pipeline
def iris_pipeline():
    return PipelineDefinition(
        name="iris_pipeline",
        solid_defs=[download_file, k_means_iris_solid],
        dependencies={
            "k_means_iris": {"path": DependencyDefinition("download_file", "path")}
        },
    )
