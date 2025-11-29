import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: The file {abs_file_path} is not in the working directory"

    if not os.path.isfile(abs_file_path):
        parent_dir = os.path.dirname(abs_file_path)
        try:
            os.makedirs(parent_dirs)
        except Exception as e:
            return f"Error creating directories for {parent_dir}: {str(e)}"

    try:
        with open(abs_file_path, 'w', encoding='utf-8', errors='replace') as file:
            file.write(content)
        return f"Successfully wrote to file {abs_file_path}: lenghth {len(content)} characters."
    except Exception as e:
        return f"Error writing to file {abs_file_path}: {str(e)}"

    