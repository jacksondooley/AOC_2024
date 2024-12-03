import requests
import os
from pathlib import Path

def get_input(day: int) -> str:
    # Check for existing input file
    input_file = Path(f"day_{day}/input.txt")
    
    # If file exists, read and return its contents
    if input_file.exists():
        return input_file.read_text()
    
    # If not, fetch from AOC and cache it
    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {
        'Cookie': f'session={os.getenv("AOC_SESSION")}'
    }
    
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        # Create directory if it doesn't exist
        input_file.parent.mkdir(exist_ok=True)
        # Save the input to a file
        input_file.write_text(response.text)
        return response.text
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Only run if this is the main file
if __name__ == "__main__":
    print(get_input(1))