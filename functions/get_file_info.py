import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory,directory))

    if not abs_directory.startswith(abs_working_directory):
        return f"Error: The directory {abs_directory} is not in the working directory {abs_working_directory}."

    contents = os.listdir(abs_directory)

    print("Contents of directory:", abs_directory)

    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response = f"- file size is {size} bytes. Is directory: {is_dir}. Name: {content}\n"
        print(final_response)
    return final_response