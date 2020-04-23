from xgboost import XGBClassifier
import dill
import csv
import os

from dagster import execute_pipeline, pipeline, solid


@solid
def load_data(_):
    dataset_path = os.path.join(os.path.abspath("."), "test_data.csv")
    with open(dataset_path, "r") as fd:
        data = [row for row in csv.DictReader(fd)]
    return data


@solid
def apply_model(_, data):
    with open(f'model_dill.dat', 'rb') as f:
        model = dill.load(f)
    pred = model.predict(data)
    predictions = [round(value) for value in pred]
    return predictions

#need to add actuals to build solid for showing model accuracy to test results display
# @solid
# def success_rate
#     dataset_path = os.path.join(os.path.abspath("."), "dsdk_models/")

@pipeline
def demo_pipeline():
    data = load_data()
    apply_model(data)

# if __name__ == "__main__":
#     result = execute_pipeline(demo_pipeline)
#     assert result.success

# def test_pipeline():
#     res = execute_pipeline(demo_pipeline)
#     assert res.success
#     assert len(res.solid_result_list) == len(data)
#     for solid_res in res.solid_result_list:
#         assert solid_res.success