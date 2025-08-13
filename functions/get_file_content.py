import os
from functions.config import character_limit

def get_file_content(working_directory, file_path):
    try:
        path = os.path.join(working_directory, file_path)
        abspath = os.path.abspath(path)
        print(path)
        print(abspath)
        if working_directory not in abspath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        file_content_string = ""
        with open(path, "r") as f:
            file_content_string = f.read(character_limit)

        #truncate to character_limit message missing
        
        return file_content_string
    except Exception as e:
        return f"Error: {e}"