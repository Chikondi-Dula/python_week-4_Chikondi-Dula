def aquaculture_file_service():
    try:
        # Ask user for the filename (e.g., fish_data.txt)
        filename = input("Enter the aquaculture file to read: ")

        # Open and read file
        with open(filename, "r") as file:
            content = file.readlines()

        # Modify the content: clean formatting & capitalize fish species names
        modified_content = []
        for line in content:
            modified_line = line.strip().title()  # Make each word title case
            modified_content.append(modified_line)

        # Save modified content in a new file
        new_filename = "aquaculture_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write("\n".join(modified_content))

        print(f"✅ Aquaculture data successfully processed into '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The aquaculture file does not exist. Please check the filename.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run program
aquaculture_file_service()
