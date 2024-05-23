import re
import json
import os

def is_valid_mobile(number):
    """Check if the mobile number is valid."""
    return re.fullmatch('[6-9][0-9]{9}', number) is not None

def read_mobile_numbers(file_path):
    """Read mobile numbers from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def write_mobile_numbers(file_path, numbers):
    """Write mobile numbers to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(numbers, file, indent=4)

def main():
    mobile_file = 'mobile_numbers.json'
    
    n = input('Enter a Mobile number: ')
    
    if is_valid_mobile(n):
        existing_numbers = read_mobile_numbers(mobile_file)
        
        if n not in existing_numbers:
            existing_numbers.append(n)
            write_mobile_numbers(mobile_file, existing_numbers)
            print('This is a valid mobile number and has been added to the JSON file.')
        else:
            print('This is a valid mobile number but already exists in the JSON file.')
    else:
        print('This is not a valid mobile number.')

if __name__ == "__main__":
    main()
