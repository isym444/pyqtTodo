# build_application.py
import subprocess
import sys
import os

def build_application():
    spec_file = 'main.spec'  # Change this if your spec file has a different name

    if not os.path.isfile(spec_file):
        print(f"Spec file '{spec_file}' not found.")
        return

    command = [
        'pyinstaller',
        spec_file
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Built application using '{spec_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error building application: {e}")

if __name__ == '__main__':
    build_application()
