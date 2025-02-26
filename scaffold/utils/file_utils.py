# File Utils
import shutil
from pathlib import Path

def copy_template(src, dst):
    """Copy a template directory to a target directory."""
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)