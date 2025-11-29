import sys
import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions import get_file_info

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose_flag = False

    if len(sys.argv) < 2:
        print("Please provide input text as a command-line argument.")
        sys.exit(1)

    print("Arguments",sys.argv[1])

    if len(sys.argv) ==3 and sys.argv[2].strip().lower() == "--verbose":
        verbose_flag = True

    prompt = sys.argv[1].strip()
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )


    print(response.text)

    if response is None or response.usage_metadata is None:
        print("No usage metadata available.")
        return

    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response token: {response.usage_metadata.candidates_token_count}")

print(get_file_info.get_files_info("calculator","pkg"))



