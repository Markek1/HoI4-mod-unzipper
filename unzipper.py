import zipfile
import os

import paths

DOWNLOADS_PATH = paths.DOWNLOADS_PATH
WORKING_DIR = DOWNLOADS_PATH + "/mods"


def renamer():
    for file in os.listdir(WORKING_DIR):
        if file.endswith(".zip"):
            print(file)
            mod_id = file.split(".")[0]
            print(mod_id)

            with zipfile.ZipFile(f"{WORKING_DIR}/{file}", "r") as zip_ref:
                print(zip_ref)
                zip_ref.extractall(f"{WORKING_DIR}/{mod_id}")

            os.remove(f"{WORKING_DIR}/{file}")
            for inside_file in os.listdir(f"{WORKING_DIR}/{mod_id}"):
                if inside_file.endswith(".zip"):
                    with zipfile.ZipFile(
                        f"{WORKING_DIR}/{mod_id}/{inside_file}", "r"
                    ) as zip_ref:
                        print(zip_ref)
                        zip_ref.extractall(f"{WORKING_DIR}/{mod_id}")
                    os.remove(f"{WORKING_DIR}/{mod_id}/{inside_file}")

            with open(f"{WORKING_DIR}/{mod_id}/descriptor.mod", "r") as mod_file:
                lines = mod_file.read().splitlines()
            for i, line in enumerate(lines):
                if "name=" in line:
                    mod_name = line[6:-1]
                elif "path=" in line:
                    lines[i] = f""

            lines.append(f'path = "mod/{mod_name}"')

            with open(f"{WORKING_DIR}/{mod_name}.mod", "w") as future_mod_file:
                for line in lines:
                    if 'archive="' not in line:
                        future_mod_file.write(line + "\n")
            try:
                os.rename(f"{WORKING_DIR}/{mod_id}", f"{WORKING_DIR}/{mod_name}")
            except:
                print(f"Folder {mod_name} already exists")


if __name__ == "__main__":
    renamer()
