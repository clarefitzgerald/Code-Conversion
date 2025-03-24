import csv
#import os
import re
def get_replacement_values(csv_file):
    """Reads CSV and returns a list of (old_value, new_value) pairs."""
    replacements = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:  # Ensure at least two columns exist
                replacements.append((row[0], row[1]))
    return replacements

def replace_in_l5k(l5k_file, replacements):
    """Replaces all occurrences of old values with new values in an L5K file."""
    with open(l5k_file, 'r', encoding='utf-8') as file:
        data = file.read()

     # Replace only exact matches of the tags
    for old_value, new_value in replacements:
        pattern = r'\b' + re.escape(old_value) + r'\b'  # Match exact word boundary
        data = re.sub(pattern, new_value, data)

    # Write back modified data
    with open(l5k_file, 'w', encoding='utf-8') as file:
        file.write(data)

# Example usage

csv_file = 'newNames.csv'   # CSV containing old and new values, old values in left column, new values in right
l5k_file = 'FILENAME.L5K'  # L5K file to modify
#os.chdir("c:/Users/BillVorac/OneDrive - Automation Solutions/Desktop/Water Reclamation/Add New Alias/")
replacements = get_replacement_values(csv_file)
if replacements:
    replace_in_l5k(l5k_file, replacements)
    print(f"Replaced {len(replacements)} values in {l5k_file}.")
else:
    print("Invalid CSV format. Ensure it has at least two values per row.")

