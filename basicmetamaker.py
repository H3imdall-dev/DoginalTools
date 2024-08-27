import json

def get_user_input():
    # Prompt the user for the collection name
    name = input("Enter the collection name: ").strip()
    while not name:
        print("Collection name cannot be empty. Please try again.")
        name = input("Enter the collection name: ").strip()
    
    # Prompt the user for the collection size
    while True:
        size_input = input("Enter the collection size (number of entries): ").strip()
        try:
            size = int(size_input)
            if size <= 0:
                print("Collection size must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the collection size.")
    
    return name, size

def create_ow_entries(name, size):
    ow_entries = []
    for i in range(1, size + 1):
        ow_entry = {
            "id": "",
            "meta": {
                "name": f"{name} #{i}"
            }
        }
        ow_entries.append(ow_entry)
    return ow_entries

def create_dm_entries(name, size):
    dm_entries = []
    for i in range(1, size + 1):
        dm_entry = {
            "inscriptionId": "",
            "name": f"{name} #{i}"
        }
        dm_entries.append(dm_entry)
    return dm_entries

def save_json_file(file_path, data):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Successfully saved {file_path}")
    except Exception as e:
        print(f"Error saving {file_path}: {e}")

def main():
    # Get user input
    name, size = get_user_input()
    
    # Create entries
    ow_entries = create_ow_entries(name, size)
    dm_entries = create_dm_entries(name, size)
    
    # Define file names
    ow_file_name = f'OW_{name}.json'
    dm_file_name = f'DM_{name}.json'
    
    # Save files
    save_json_file(ow_file_name, ow_entries)
    save_json_file(dm_file_name, dm_entries)
    
    print("\nFiles have been created successfully:")
    print(f"- {ow_file_name}")
    print(f"- {dm_file_name}")

if __name__ == "__main__":
    main()
