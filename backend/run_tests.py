import os
import sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    # Add the current directory to the Python path
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    print(f"Using settings module: {os.environ['DJANGO_SETTINGS_MODULE']}")
    print("Running tests...")  # Indicate that tests are starting
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any errors that occur
