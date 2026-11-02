import os
from roboflow import Roboflow

api_key = os.environ.get("ROBOFLOW_API_KEY") or input("Pega tu API key: ")

rf = Roboflow(api_key=api_key)
project = rf.workspace("pablos-workspace-oda19").project("fruits-by-yolo-jaoco")
version = project.version(3)
dataset = version.download("yolo26")

print("Dataset en:", dataset.location)
print("data.yaml en:", os.path.join(dataset.location, "data.yaml"))