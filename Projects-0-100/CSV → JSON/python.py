# import csv
# import json

# INPUT_CSV = "Amazon.csv"
# TEMP_JSON = "raw.json"
# FINAL_JSON = "final.json"

# COLUMN_MAPPING = {
#     "id": "user_id",
#     "full_name": "name",
#     "age": "user_age",
#     "city": "location"
# }

# # -------------------------------
# # Step 1: CSV → JSON
# # -------------------------------
# def csv_to_json(csv_file, json_file):
#     with open(csv_file, "r", newline="", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         data = list(reader)

#     with open(json_file, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4)

#     print("✅ CSV converted to JSON")


# # -------------------------------
# # Step 2: Rename columns
# # -------------------------------
# def rename_columns(input_json, output_json, mapping):
#     with open(input_json, "r", encoding="utf-8") as f:
#         data = json.load(f)

#     transformed_data = []
#     for row in data:
#         new_row = {}
#         for old_key, value in row.items():
#             new_key = mapping.get(old_key, old_key)
#             new_row[new_key] = value
#         transformed_data.append(new_row)

#     with open(output_json, "w", encoding="utf-8") as f:
#         json.dump(transformed_data, f, indent=4)

#     print("✅ Columns renamed and final JSON created")


# # -------------------------------
# # Run pipeline
# # -------------------------------
# if __name__ == "__main__":
#     csv_to_json(INPUT_CSV, TEMP_JSON)
#     rename_columns(TEMP_JSON, FINAL_JSON, COLUMN_MAPPING)


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_DIR = os.path.dirname(BASE_DIR)  # go up one level
folders = os.listdir(PROJECTS_DIR)

for folder in folders:
    folder_path = os.path.join(PROJECTS_DIR, folder)

    # Ensure it's actually a directory
    if not os.path.isdir(folder_path):
        continue

    readme_path = os.path.join(folder_path, "README.md")

    # Do not overwrite existing README
    if os.path.exists(readme_path):
        continue

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(
            f"# {folder}\n\n"
            "## Description\n"
            "Data engineering practice project.\n"
        )

    print(f"✅ README created in {folder}")