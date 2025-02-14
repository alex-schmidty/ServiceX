import os
import sys
from pathlib import Path
import subprocess
instance = os.environ.get('INSTANCE_NAME', 'Unknown')
from pathlib import Path
import shutil

def transform_single_file(file_path: str, output_path: Path, output_format: str):
    # create input.txt file for event loop and insert file_path as only line
    with open("input.txt", "w") as f:
        f.write(file_path)
    
    # move reco file to appropriate loacation
    shutil.move("reco.yml", os.environ.get("CONFIG_LOC"))
    
    subprocess.run(["runTop_el.py", "-i", "input.txt", "-o", "output", "-t", "customConfig", "-e", "1"])
    shutil.move("output.root", output_path)

if __name__ == "__main__":
    transform_single_file(sys.argv[1], Path(sys.argv[2]), sys.argv[3])