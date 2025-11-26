# Star Citizen Component Classifier

A tool to automatically add component classification information to Star Citizen's English localization files.

## Features

- Extracts component information from components.json
- Adds classification details (name, size, grade, type) to components in the localization file
- Supports power plants, shields, quantum drives, and coolers
- Automatically updates the English localization file in Star Citizen's installation directory

## Requirements

- Python 3.x
- `unp4k.exe` tool (for extracting Star Citizen data files, included in the repository)
- Star Citizen installed in the default location (Changeable in the script)

## Installation

Clone this repository:
   ```bash
   git clone https://github.com/Pakobbix/sc_component_classifier.git
   cd sc_component_classifier
   ```


## Usage

1. Run the script:
   ```bash
   python sc_component_classifier.py
   ```

2. The script will:
   - Extract the English localization file from Star Citizen
   - Add component classification information
   - Copy the updated file back to Star Citizen's directory

## Configuration

You can customize the script by modifying these variables in the `AutoAddInfo` class:

- `ini_file`: Path to the English localization file
- `json_file`: Path to your components JSON file
- `game_path`: Path to your Star Citizen installation

## InGame

The changes will be visible everywhere, where the name of the component is shown, including:
- Ship Scans
- Shopping Menus
- Tractor Beams

Instead of `TS-2`, you will see `TS-2 (S3 Grade A Military Quantum Drive)`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
