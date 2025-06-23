import os
import re

def make_upf_filename(filename):
    match = re.match(r'^([A-Za-z]+)[._]', filename)
    if match:
        return match.group(1) + '.upf'
    else:
        return filename + '.upf'

directory = '/Users/tavianjones/Documents/VSCode/pseudopotentials/pseudos'

files = sorted(f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)))

for filename in files:
    if filename != "script.py":  # Every other file (starting from the second)
        old_path = os.path.join(directory, filename)
        new_filename = make_upf_filename(filename)
        new_path = os.path.join(directory, new_filename)
        
        os.rename(old_path, new_path)

# Make sure the first character of every filename is capitalized
files = sorted(f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)))
for filename in files:
    if filename != "script.py":  # Skip the script itself
        old_path = os.path.join(directory, filename)
        new_filename = filename.capitalize()
        new_path = os.path.join(directory, new_filename)
        
        os.rename(old_path, new_path)
