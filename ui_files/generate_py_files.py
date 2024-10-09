import os
import subprocess

def convert_ui_files(ui_directory):
    # Ensure the directory exists
    if not os.path.isdir(ui_directory):
        print(f"Directory '{ui_directory}' does not exist.")
        return

    # List all .ui files in the directory
    ui_files = [f for f in os.listdir(ui_directory) if f.endswith('.ui')]

    if not ui_files:
        print(f"No .ui files found in '{ui_directory}'.")
        return

    for ui_file in ui_files:
        ui_file_path = os.path.join(ui_directory, ui_file)
        py_file = ui_file.replace('.ui', '_ui.py')
        py_file_path = os.path.join(ui_directory, py_file)

        # Construct the command
        command = [
            'pyuic6',
            '-x',
            ui_file_path,
            '-o',
            py_file_path
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True)
            print(f"Converted '{ui_file}' to '{py_file}'.")
        except subprocess.CalledProcessError as e:
            print(f"Error converting '{ui_file}': {e}")

if __name__ == '__main__':
    ui_directory = 'ui_files'  # Change this if your directory has a different name
    convert_ui_files(ui_directory)
