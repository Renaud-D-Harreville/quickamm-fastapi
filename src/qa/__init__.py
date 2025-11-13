# from importlib import resources
# resource_dir_path = resources.files("resources")

from pathlib import Path

resources_dir_path = Path("/code/src/resources")  # Path(__file__).parent.parent / "resources"

print("resources_dir_path : ", resources_dir_path, flush=True)
