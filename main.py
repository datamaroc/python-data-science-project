# import libraries
from typing import List, Dict

# Constants should be uppercase in PEP 8
DEFAULT_NUM1 = 10
DEFAULT_NUM2 = 5

def add_numbers(num1: int, num2: int) -> int:
    """
    Calculate the sum of two numbers.

    Parameters:
    - num1 (int): The first number.
    - num2 (int): The second number.

    Returns:
    - int: The result of adding num1 and num2.
    """
    try:
        result = num1 + num2
        return result
    except TypeError:
        print("Error: Both arguments must be integers.")
        return None

def parse_data(raw_data: str) -> List[Dict[str, str]]:
    """
    Process raw CSV data into a list of dictionaries.

    Parameters:
    - raw_data (str): A raw CSV string with headers, where each row is a record.

    Returns:
    - List[Dict[str, str]]: A list of dictionaries with 'Name', 'Age', and 'Height' as keys.
    """
    if not raw_data:
        print("Error: The input data is empty.")
        return []

    try:
        # Split the raw data by lines and remove any leading/trailing whitespace
        data_lines = raw_data.strip().split('\n')

        # Extract headers from the first line and records from the remaining lines
        headers = [header.strip() for header in data_lines[0].split(',')]
        records = data_lines[1:]

        # Convert each record into a dictionary
        structured_data = []
        for record in records:
            values = [value.strip() for value in record.split(',')]
            if len(values) != len(headers):
                print(f"Warning: Skipping invalid record: {record}")
                continue
            record_dict = dict(zip(headers, values))
            structured_data.append(record_dict)

        return structured_data
    except Exception as e:
        print(f"Error occurred while parsing data: {e}")
        return []

def main():
    # Example raw data to be processed
    raw_csv_data = 'Name, Age, Height\nJohn, 25, 175\nJane, 30, 160\n'

    # Process and display the structured data
    processed_data = parse_data(raw_csv_data)
    if processed_data:
        print(processed_data)
    else:
        print("No valid data to display.")

    # Demonstrate the usage of the add_numbers function
    result = add_numbers(DEFAULT_NUM1, DEFAULT_NUM2)
    if result is not None:
        print(f"Sum of {DEFAULT_NUM1} and {DEFAULT_NUM2} is: {result}")
    else:
        print("Error: Could not calculate the sum.")

# Ensures the script runs only when executed directly (not imported)
if __name__ == '__main__':
    main()
