from functions.get_file_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def get_file_info_test():
    working_dir = "calculator"
    root_contents = get_files_info(working_dir)
    pkg_contents = get_files_info(working_dir, "pkg")
    print("Root Directory Contents:\n", root_contents)
    print("pkg Directory Contents:\n", pkg_contents)

    out_contents = get_files_info(working_dir, "/bin")
    print(out_contents)

def get_file_content_test():
    working_dir = "calculator"
    print(get_file_content(working_dir, "random.txt"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "pkg/notexis.py"))
    print(get_file_content(working_dir, "/bin/cat"))

def write_file_test():

    working_dir = "calculator"
    print(write_file(working_dir, "random.txt", "print('Hello World')"))
    print(write_file(working_dir, "test_write.txt", "This is a test content."))
    print(write_file(working_dir, "pkg/new_dir/new_file.txt", "New file content here."))
    print(write_file(working_dir, "/etc/passwd", "Trying to write outside working dir."))

if __name__ == "__main__":
    write_file_test()