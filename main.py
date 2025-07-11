import os
import sys
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) > 3 and sys.argv[2] == "--verbose":
        verbose == True
    else:
        verbose == False

    if len(sys.argv) < 2:
        print("Usage: python my_script.py 'your prompt here'")
        sys.exit(1)  
        
    #print("enter your prompt for the AI: ")
    #prompt = input()
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=sys.argv[1]
    )
    #print("Hello from aiagent!")
    print(response.text)
    if verbose == True:
        print("User prompt:",sys.argv[1])
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)




if __name__ == "__main__":
    main()
