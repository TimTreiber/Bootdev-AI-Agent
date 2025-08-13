import os

def get_files_info(working_directory, directory="."):
    try:
        path = os.path.join(working_directory, directory)
        abspath = os.path.abspath(path)
        if not os.path.isdir(path):
            return f'Error: "{directory}" is not a directory'
        if working_directory not in abspath:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        contents = os.listdir(path)
        return_string = ""
        for file in contents:
            size = 0
            is_dir = True
            temp_path = os.path.join(path, file)
            if os.path.isfile(temp_path):
                size = os.path.getsize(temp_path)
                is_dir = False
            if os.path.isdir(temp_path):
                size = os.path.getsize(temp_path)
            return_string += f"- {file}: file_size={size} bytes, is_dir={is_dir}\n"
        return return_string
    except Exception as e:
        return f"Error: {e}"
