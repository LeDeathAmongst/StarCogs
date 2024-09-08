import os
import glob

def remove_files_with_extension(directory: str, extension: str):
    # Create a pattern for the files to be removed
    pattern = os.path.join(directory, f"*.{extension}")
    # Use glob to find all files matching the pattern
    files = glob.glob(pattern)

    for file in files:
        try:
            os.remove(file)
            print(f"Removed: {file}")
        except Exception as e:
            print(f"Error removing {file}: {e}")

# Specify the directory and the extension
directory = "./"
extension = "md"

# Remove the files
remove_files_with_extension(directory, extension)
