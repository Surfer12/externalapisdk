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
