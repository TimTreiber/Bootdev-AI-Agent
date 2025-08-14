from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    print("running tests\n")

    '''
    --get file info tests--
    result1 = get_files_info("calculator", ".")
    print(f"Result for current directory:\n{result1}\n")
    
    result2 = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n{result2}\n")
    
    result3 = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n{result3}\n")
    
    result4 = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n{result4}\n")
    --get file info tests--

    --get file content tests--
    result1 = get_file_content("calculator", "lorem.txt")
    print(f"Result for lorem:\n{result1}\n")
    
    result2 = get_file_content("calculator", "pkg/calculator.py")
    print(f"Result for calculator:\n{result2}\n")
    
    result3 = get_file_content("calculator", "main.py")
    print(f"Result for main:\n{result3}\n")
    
    result4 = get_file_content("calculator", "/bin/cat")
    print(f"Result for '/bin/cat' directory:\n{result4}\n")
    
    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result for 'pkg/does_not_exist.py' file:\n{result5}\n")
    --get file content tests--
    
    --write file tests--
    print (write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    
    print (write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print (write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    --write file tests--
    
    --run python file tests--
    print(run_python_file("calculator", "main.py"))
    
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
    --run python file tests--
    '''
    '''
    print(write_file("calculator", "readme.md", "testing"))
    result1 = get_files_info("calculator", ".")
    print(f"Result for current directory:\n{result1}\n")
    result2 = get_file_content("calculator", "readme.md")
    print(f"Result for readme:\n{result2}\n")
    '''
    print("ending tests")

if __name__ == "__main__":
    main()
