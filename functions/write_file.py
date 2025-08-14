import os
from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the content into the file in the specified directory, returns a success message, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is supposed to be written into the file.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file where the content can be written into, relative to the working directory. If not provided makes a new file.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    try:
        path = os.path.join(working_directory, file_path)
        abspath = os.path.abspath(path)
        if working_directory not in abspath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"