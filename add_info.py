#!/usr/bin/env python3

# This script automatically adds information to the original english ini file for Star Citizen.
# It uses a json file containing the information to be added and add the information to the ini file.

import os
import json
import subprocess

class AutoAddInfo:
    def __init__(self):
        self.ini_file = "Data/Localization/english/global.ini"
        self.json_file = "components.json"
        self.game_path = r"C:\Program Files\Roberts Space Industries\StarCitizen\LIVE"

    def load_json(self):
        with open(self.json_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def unpak_data(self):
        # Check if the p4k file exists
        pak_file = os.path.join(self.game_path, "Data.p4k")
        if not os.path.exists(pak_file):
            raise FileNotFoundError(f"P4K file '{pak_file}' does not exist.")

        # Check if the unpak tool exists
        unp4k_tool = "unp4k.exe"
        if not os.path.exists(unp4k_tool):
            raise FileNotFoundError(f"Unp4k tool '{unp4k_tool}' does not exist. Please ensure it is in the current directory.")

        # Run the unp4k tool to extract the data
        print(f"Extracting data from {pak_file} using {unp4k_tool}...")
        try:
            subprocess.run([unp4k_tool, pak_file, "Localization/english/global.ini"], check=True)
            print("Data extraction completed successfully.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"An error occurred while extracting data: {e}")

    def cleanup_old_ini_file(self):
        # Check if the ini file exists
        if os.path.exists(self.ini_file):
            print(f"Removing old INI file: {self.ini_file}")
            os.remove(self.ini_file)
        else:
            print(f"No old INI file found at: {self.ini_file}")

    def add_power_plant_information(self, data, ini_content):
        if "power_plants" not in data:
            print("No power plants found in the JSON data.")
            return 0

        power_plants = data["power_plants"]

        # Search for the key from the ini content and add the information to the ini content
        for key, plant in power_plants.items():
            name = plant.get("name", "bespoke")
            size = plant.get("size", "bespoke")
            grade = plant.get("grade", "bespoke")
            type_ = plant.get("type", "bespoke")
            if name == "":
                name = "bespoke"
            if size == "":
                size = "bespoke"
            if grade == "":
                grade = "bespoke"
            if type_ == "":
                type_ = "bespoke"
            if key in ini_content:
                ini_content[key] = f"{name} ({size} Grade {grade} {type_})"

    def add_shield_information(self, data, ini_content):
        if "shields" not in data:
            print("No shields found in the JSON data.")
            return 0

        shields = data["shields"]

        # Search for the key from the ini content and add the information to the ini content
        for key, shield in shields.items():
            name = shield.get("name", "bespoke")
            size = shield.get("size", "bespoke")
            grade = shield.get("grade", "bespoke")
            type_ = shield.get("type", "bespoke")
            if name == "":
                name = "bespoke"
            if size == "":
                size = "bespoke"
            if grade == "":
                grade = "bespoke"
            if type_ == "":
                type_ = "bespoke"
            if key in ini_content:
                ini_content[key] = f"{name} ({size} Grade {grade} {type_})"

    def add_quantum_drive_information(self, data, ini_content):
        if "quantum_drives" not in data:
            print("No quantum drives found in the JSON data.")
            return 0

        quantum_drives = data["quantum_drives"]

        # Search for the key from the ini content and add the information to the ini content
        for key, drive in quantum_drives.items():
            name = drive.get("name", "bespoke")
            size = drive.get("size", "bespoke")
            grade = drive.get("grade", "bespoke")
            type_ = drive.get("type", "bespoke")
            if name == "":
                name = "bespoke"
            if size == "":
                size = "bespoke"
            if grade == "":
                grade = "bespoke"
            if type_ == "":
                type_ = "bespoke"
            if key in ini_content:
                ini_content[key] = f"{name} ({size} Grade {grade} {type_})"

    def add_cooler_information(self, data, ini_content):
        if "coolers" not in data:
            print("No coolers found in the JSON data.")
            return 0

        coolers = data["coolers"]

        # Search for the key from the ini content and add the information to the ini content
        for key, cooler in coolers.items():
            name = cooler.get("name", "bespoke")
            size = cooler.get("size", "bespoke")
            grade = cooler.get("grade", "bespoke")
            type_ = cooler.get("type", "bespoke")
            if name == "":
                name = "bespoke"
            if size == "":
                size = "bespoke"
            if grade == "":
                grade = "bespoke"
            if type_ == "":
                type_ = "bespoke"
            if key in ini_content:
                ini_content[key] = f"{name} ({size} Grade {grade} {type_})"

    def change_english_ini_file(self):
        # Check if the ini file exists
        if not os.path.exists(self.ini_file):
            raise FileNotFoundError(f"INI file '{self.ini_file}' does not exist.")

        # Read the ini file
        print(f"Reading INI file: {self.ini_file}")
        self.ini_file = os.path.abspath(self.ini_file)

        ini_data = {}

        # Read the ini file line by line
        with open(self.ini_file, 'r', encoding='latin1') as file:
            for line in file:
                if line and not line.startswith(';') and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    ini_data[key.strip()] = value.strip()

        # Now ini_data contains all key-value pairs from the file
        print(f"Loaded {len(ini_data)} entries from the INI file")

        # Load the JSON data
        data = self.load_json()

        # Add power plant information to the ini data
        print("Adding power plant information to the INI data...")
        self.add_power_plant_information(data, ini_data)

        # Add shield information to the ini data
        print("Adding shield information to the INI data...")
        self.add_shield_information(data, ini_data)

        # Add quantum drive information to the ini data
        print("Adding quantum drive information to the INI data...")
        self.add_quantum_drive_information(data, ini_data)

        # Add cooler information to the ini data
        print("Adding cooler information to the INI data...")
        self.add_cooler_information(data, ini_data)

        print("Removing spaces between keys and values in the INI data...")
        ini_data = {key.strip(): value.strip() for key, value in ini_data.items()}

        # Write the updated ini data back to the file
        print(f"Writing updated INI data back to {self.ini_file}")
        with open(self.ini_file, 'w', encoding='latin1') as file:
            for key, value in ini_data.items():
                file.write(f"{key}={value}\n")

        print("INI file updated successfully.")

    def copy_DATA_folder_into_star_citizen_folder(self):
        # Define the source and destination paths
        source_path = "Data"
        destination_path = os.path.join(self.game_path, "Data")

        # Check if the source path exists
        if not os.path.exists(source_path):
            os.makedirs(source_path)

        # Copy the Data folder into the Star Citizen folder
        print(f"Copying {source_path} to {destination_path}...")
        try:
            subprocess.run(["xcopy", source_path, destination_path, "/E", "/I", "/Y"], check=True, shell=True)
            print("Data folder copied successfully.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"An error occurred while copying the Data folder: {e}")

if __name__ == "__main__":
    if len(os.sys.argv) > 1:
        ini_file = os.sys.argv[1]
    if len(os.sys.argv) > 2:
        json_file = os.sys.argv[2]

    auto_add_info = AutoAddInfo()
    try:
        # Clean up old ini file if it exists
        auto_add_info.cleanup_old_ini_file()

        # Unpak the data if necessary
        if not os.path.exists(auto_add_info.ini_file):
            auto_add_info.unpak_data()

        # Load the JSON data
        data = auto_add_info.load_json()
        auto_add_info.change_english_ini_file()

        # Copy the Data folder into the Star Citizen folder
        auto_add_info.copy_DATA_folder_into_star_citizen_folder()
    except Exception as e:
        print(f"An error occurred: {e}")
