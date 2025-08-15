import os
import subprocess
from google import genai
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the python file that is supposed to be executed, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="A list of optional arguments to pass into the python file",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    try:
        path = os.path.join(working_directory, file_path)
        abspath = os.path.abspath(path)
        if working_directory not in abspath:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        arguments = ["python3", file_path] + args
        completed_process = subprocess.run(arguments, cwd=working_directory, capture_output=True, timeout=5, text=True)
        return_string = "This is the result:\n"
        if completed_process == None:
            return "No output produced."
        return_string += f"STDOUT: \n{completed_process.stdout}\n"
        return_string += f"STDERR: \n{completed_process.stderr}\n"
        if completed_process.returncode != 0:
            return_string += f"Process exited with code {completed_process.returncode}\n"
        return return_string
    except Exception as e:
        return f"Error: executing Python file: {e}"