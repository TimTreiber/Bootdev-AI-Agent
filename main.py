import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import get_files_info

load_dotenv()
api_key_local = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key_local)

def main():
    print("Hello from bootdev-ai-agent!")

    if len(sys.argv) == 1:
        sys.exit("No prompt was provided!")
    user_prompt = sys.argv[1]

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages
    )

    print(response.text)
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
