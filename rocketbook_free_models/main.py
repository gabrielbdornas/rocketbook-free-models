from pathlib import Path
import os

# Paths setup
home_path = Path.cwd()
input_paths = home_path / 'sources/'
output_path = home_path / 'prints/'

output_path.mkdir(exist_ok=True)  # Ensure output directory exists

for file_path in input_paths.glob('*'):
    output_file_name = output_path / file_path.name
    command = f'pdfjam {file_path} {file_path} {file_path} {file_path} --nup 2x1 --landscape --outfile {output_file_name}'
    os.system(command)
    print(f"✅ File saved in {output_file_name}!")
