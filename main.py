import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import get_files_info
from functions.get_files_info import schema_get_files_info
from functions.config import *
from functions.get_file_content import get_file_content
from functions.get_file_content import schema_get_file_content
from functions.write_file import write_file
from functions.write_file import schema_write_file
from functions.run_python import run_python_file
from functions.run_python import schema_run_python_file

load_dotenv()
api_key_local = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key_local)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file
    ]
)

function_dict = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
    }

def main():
    print("Hello from bootdev-ai-agent!")

    if len(sys.argv) == 1:
        sys.exit("No prompt was provided!")
    user_prompt = sys.argv[1]
    verbose_arg = False
    if "--verbose" in sys.argv:
        verbose_arg = True

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )
    for part in response.candidates[0].content.parts:
        if hasattr(part, "function_call") and part.function_call:
            for call in response.function_calls:
                #print(f"Calling function: {call.name}({call.args})")
                function_result = call_function(call, verbose_arg)
                if not function_result.parts[0].function_response.response:
                    raise Exception("Error: No response from function call!")
        elif hasattr(part, "text") and part.text:
            print(part.text)
    
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if verbose_arg:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
        print(f"-> {function_result.parts[0].function_response.response}")


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    if function_name not in function_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
    func = function_dict[function_name]
    function_result = func("calculator",**function_args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
                )
            ],
        )



if __name__ == "__main__":
    main()
