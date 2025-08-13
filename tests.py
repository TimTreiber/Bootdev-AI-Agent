from functions.get_files_info import get_files_info

def main():
    print("running tests\n")

    result1 = get_files_info("calculator", ".")
    print(f"Result for current directory:\n{result1}\n")
    
    result2 = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n{result2}\n")
    
    result3 = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n{result3}\n")
    
    result4 = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n{result4}\n")

    print("ending tests")

if __name__ == "__main__":
    main()
