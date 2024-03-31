import os
import random
import string
import csv

def generate_random_name(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def rename_csv_files_with_random_names(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            old_file_path = os.path.join(input_folder, file_name)
            new_file_name = generate_random_name() + '.csv'
            new_file_path = os.path.join(output_folder, new_file_name)

            with open(old_file_path, 'r', encoding='utf-8-sig') as source_file:
                reader = csv.reader(source_file)
                data = list(reader)

                with open(new_file_path, 'w', newline='', encoding='utf-8-sig') as new_file:
                    writer = csv.writer(new_file)
                    writer.writerows(data)

            print(f"The file {file_name} has been renamed to {new_file_name} and saved in {output_folder}")

input_folder = "source"
output_folder = "out"

if not os.path.exists(input_folder):
    print(f"Input folder '{input_folder}' does not exist.")
    exit()

os.makedirs(output_folder, exist_ok=True)

try:
    import csv
except ImportError:
    print("The 'csv' module is not available. Please install it before running this script.")
    exit()

rename_csv_files_with_random_names(input_folder, output_folder)