import os
import json

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(THIS_FOLDER, "..", "config.json")
with open(config_path) as f:
    config = json.load(f)
