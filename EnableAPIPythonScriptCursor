import subprocess

def enable_proposed_apis(apis):
    for api in apis:
        try:
            subprocess.run(['cursor', '--enable-proposed-api', api], check=True, capture_output=True, text=True)
            print(f"Successfully enabled: {api}")
        except subprocess.CalledProcessError as e:
            print(f"Error enabling {api}: {e.stderr}")

apis_to_enable = [
    "ms-azuretools.vscode-docker",
    "vscjava.vscode-gradle",
    "googlecloudtools.cloudcode",
    "GitHub.copilot",
    "GitHub.copilot-chat",
    "github.vscode-github-actions",
    "genaiscript.genaiscript-vscode",
    "google.geminicodeassist",
    "usernamehw.errorlens"
]

enable_proposed_apis(apis_to_enable)

def check_api_status(api):
    try:
        result = subprocess.run(['cursor', '--query-proposed-api', api], capture_output=True, text=True, check=True)
        status = result.stdout.strip()
        return status
    except subprocess.CalledProcessError as e:
        return f"Error checking {api}: {e.stderr}"

apis_to_check = [
    "GitHub.vscode-codeql",
    "openai.openai-chatgpt-adhoc",
    "ms-vscode-remote.remote-containers",
    "google.geminicodeassist",
    "genaiscript.genaiscript-vscode",
    "GitHub.codespaces",
    "modular-mojotools.vscode-mojo",
    "Supermaven.supermaven"
]

for api in apis_to_check:
    status = check_api_status(api)
    print(f"Status of {api}: {status}")


""" The Python script manages proposed APIs within an application, likely the Cursor editor. It uses the cursor command-line tool to interact with these APIs.

The script has two main functions:

enable_proposed_apis(apis): This function takes a list of API identifiers and attempts to enable each one. It uses subprocess.run to execute the cursor --enable-proposed-api command for each API. The output (success or error message) is printed to the console. Error handling is included to catch issues during the enabling process.

check_api_status(api): This function checks the status of a given API. It uses subprocess.run with cursor --query-proposed-api. The output of the command, representing the API's status, is returned. Like the enable_proposed_apis function, it includes error handling.

The script defines two lists: apis_to_enable and apis_to_check. It first calls enable_proposed_apis with the apis_to_enable list, attempting to enable those APIs. Then, it iterates through the apis_to_check list, calling check_api_status for each API and printing the returned status to the console.

Several of the APIs mentioned relate to development tools and services: GitHub, Docker, YAML, Gradle, Cloud Code, Copilot, Gemini Code Assist, and more. This suggests the script might be used for configuring a development environment within Cursor.

Open Cursor’s integrated terminal.
• In Cursor, look for “Terminal” or find an option to open a terminal or console.
• Alternatively, you can use a keyboard shortcut depending on your platform (e.g., Ctrl+ or Cmd+).
Once you have the integrated terminal open, run your Python script with:
python enable_proposed_apis.py
This will execute the script in the Cursor environment, calling the “cursor” CLI commands and printing the results in the terminal.
If you see zsh messages like “zsh: no matches found” or “bad math expression,” try enclosing arguments in quotes or disabling zsh globbing, but typically just running python enable_proposed_apis.py in Cursor’s terminal should work. Make sure you have the “cursor” CLI installed and available in your environment path.
That’s it! Your script should now run in Cursor’s integrated terminal, enabling the specified proposed APIs and then checking their statuses. """
