def main():
    try:
        #  Ask user for filename
        filename = input("Enter the name of the file to read: ")

        #  Open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content (example: make it uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f" File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except IOError:
        print(" Error: Could not read or write the file.")

# Run the program
if __name__ == "__main__":
    main()
