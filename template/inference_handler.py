import os

class ModelLoadError(Exception):
    pass

def load_model(models_dir, model_name):
    """Loads a model. This function should fetch the packaged model file and save into memory
    as an object of the trained model.
    Args:
        models_dir: a directory where model is saved.
        model_name: name of the model file.
    Returns: A model object.
    """
    model_path = os.path.join(models_dir, model_name)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Failed to load model with default model_fn: missing file {model_name}.")

    try:
        # Change the code here to load the model from a packaged file
        model = f"load model from {models_dir}/{model_name}"
        return model
    except RuntimeError as e:
        raise ModelLoadError(f"Failed to load {model_path}. Encountered error {e}") from e

def preprocess_input(input_data, models_dir):
    """Handle structured input of any format and restructure into a format that fits the model.
    Args:
        input_data: structured input data in any format.
        models_dir (optional): a directory where model is saved. Packaged preprocessing functions can be saved here.
    Returns: Restructured input into a format that can be used by the model to run inference.
    """
    return None

def infer(model, input_data):
    """Run inference on restructured input data.
    Args:
        model: model object.
        input_data: data for the model to be used to run inference.
    Returns: Inference results
    """
    return None

def output(inference_result):
    """Convert inference results into a format that can be sent for analysis (e.g. JSON)
    Args:
        inference_result: result obtained from model inference
    Returns: converted inference result formar
    """
    return None
