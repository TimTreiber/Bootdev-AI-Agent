import os
from functions.config import character_limit
from google import genai
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of the file in the specified directory truncated to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to get the file content from, relative to the working directory. If not provided, returns an error.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    try:
        path = os.path.join(working_directory, file_path)
        abspath = os.path.abspath(path)
        if working_directory not in abspath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        file_content_string = ""
        with open(path, "r") as f:
            file_content_string = f.read(character_limit)
            if os.path.getsize(path) > 10000:
                print(f'[...File "{file_path}" truncated at 10000 characters]')
        
        return file_content_string
    except Exception as e:
        return f"Error: {e}"