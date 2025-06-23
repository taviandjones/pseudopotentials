import os
import itertools
import re

def make_upf_filename(filename):
    match = re.match(r'^([A-Za-z]+)[._]', filename)
    if match:
        return match.group(1) + '.upf'
    else:
        return filename + '.upf'

directory = '/Users/tavianjones/Documents/VSCode/pseudopotentials/pseudos'

files = sorted(f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)))

for i, filename in enumerate(files):
    if i % 2 == 1:  # Every other file (starting from the second)
        old_path = os.path.join(directory, filename)
        new_filename = make_upf_filename(filename)
        new_path = os.path.join(directory, new_filename)
        # Avoid overwriting existing files
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed {filename} -> {new_filename}")
        else:
            print(f"Skipped {filename}: {new_filename} already exists")