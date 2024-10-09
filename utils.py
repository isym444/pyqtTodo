import sys,os
import appdirs


basedir = os.path.dirname(__file__)

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    app_name = 'YourAppName'  # Replace with your application's name
    author = 'YourNameOrCompany'  # Replace with your name or company
    base_path = appdirs.user_data_dir(app_name, author)
    os.makedirs(base_path, exist_ok=True)
    return os.path.join(base_path, relative_path)