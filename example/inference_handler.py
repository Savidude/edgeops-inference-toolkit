import os
import pickle
import pandas as pd
import numpy as np
import json

class ModelLoadError(Exception):
    pass

def load_model(models_dir, model_name):
    model_path = os.path.join(models_dir, model_name)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Failed to load model with default model_fn: missing file {model_name}.")

    try:
        with open(f"{models_dir}/{model_name}", 'rb') as f:
            model = pickle.load(f)
        return model
    except RuntimeError as e:
        raise ModelLoadError(f"Failed to load {model_path}. Encountered error {e}") from e

def preprocess_input(input_data, models_dir):
    removed_features = ['br_000', 'bq_000', 'bp_000', 'bo_000', 'ab_000', 'cr_000', 'bn_000', 'cd_000']
    median_imputed_features = ['ak_000', 'ca_000', 'dm_000', 'df_000', 'dg_000', 'dh_000', 'dl_000', 'dj_000', 'dk_000', 'eb_000', 'di_000', 'ac_000', 'bx_000', 'cc_000']

    with open(f"{models_dir}/median_imputer.pkl", 'rb') as f:
        median_imputer = pickle.load(f)
        
    with open(f"{models_dir}/mice_imputer.pkl", 'rb') as f:
        mice_imputer = pickle.load(f)

    json_data = json.loads(input_data)
    data = pd.json_normalize(json_data)
    data = data.replace('na', np.nan)

    data = data.drop(removed_features, axis=1)
    data[median_imputed_features] = median_imputer.transform(data[median_imputed_features])
    data = pd.DataFrame(data = mice_imputer.transform(data) , columns= data.columns)
    return data

def infer(model, input_data):
    result = model.predict(input_data)
    if len(result) == 0:
        raise ValueError("Inference did not produce any results")
    return result

def output(inference_result):
    result = inference_result[0]
    response = {}
    if result == 0:
        response['result'] = "safe"
    else:
        response['result'] = "unsafe"
    return json.dumps(response)
