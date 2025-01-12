def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = content.upper()  # Modify the content

        with open('modified_' + filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified file saved as modified_{filename}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied to read file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
