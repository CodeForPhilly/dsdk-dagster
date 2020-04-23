'''isort:skip_file'''

import sys

from dagster import RepositoryDefinition
from dagster.utils import script_relative_path

sys.path.append(script_relative_path('.'))

from xgboost_test import demo_pipeline


def define_repo():
    return RepositoryDefinition(
        name='xgboost_test',
        # Note that we can pass a function, rather than pipeline instance.
        # This allows us to construct pipelines lazily, if, e.g.,
        # initializing a pipeline involves any heavy compute
        pipeline_dict={
            'test_predictions': lambda: demo_pipeline,
        },
    )
