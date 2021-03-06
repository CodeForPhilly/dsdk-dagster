"""isort:skip_file"""

import sys

from dagster import RepositoryDefinition
from dagster.utils import script_relative_path

sys.path.append(script_relative_path("."))

from hello_cereal import hello_cereal_pipeline
from complex_pipeline import complex_pipeline
from xgboost_test import demo_pipeline
from iris_pipeline import iris_pipeline


def define_repo():
    return RepositoryDefinition(
        name="hello_cereal_pipeline",
        # Note that we can pass a function, rather than pipeline instance.
        # This allows us to construct pipelines lazily, if, e.g.,
        # initializing a pipeline involves any heavy compute
        pipeline_dict={
            "hello_cereal_pipeline": lambda: hello_cereal_pipeline,
            "complex_pipeline": lambda: complex_pipeline,
            "demo_pipeline": lambda: demo_pipeline,
            "iris_pipeline": lambda: iris_pipeline,
        },
    )
