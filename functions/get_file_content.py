import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: The file {abs_file_path} is not in the working directory"

    if not os.path.isfile(abs_file_path):
        return f"Error: The path {abs_file_path} is not a file."

    file_content_string = ""
    try:
        with open(abs_file_path, 'r', encoding='utf-8 ', errors='replace') as file:
            file_content_string = file.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += "\n\n...TRUNCATED..."
        return file_content_string
    except Exception as e:
        return f"Error reading file {abs_file_path}: {str(e)}"