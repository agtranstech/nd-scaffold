# Module Generator
import os
from pathlib import Path
from scaffold.utils.file_utils import copy_template

def generate_module(module_name):
    # Define paths
    template_dir = Path(__file__).parent.parent / 'templates' / 'module_template'
    target_dir = Path.cwd() / 'src' / 'modules' / module_name

    # Copy template to target directory
    copy_template(template_dir, target_dir)

    # Update module-specific files (e.g., replace placeholders)
    replace_placeholders(target_dir, {'MODULE_NAME': module_name})

def replace_placeholders(target_dir, replacements):
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = Path(root) / file
            with open(file_path, 'r') as f:
                content = f.read()
            for key, value in replacements.items():
                content = content.replace(f'{{{{{key}}}}}', value)
            with open(file_path, 'w') as f:
                f.write(content)
