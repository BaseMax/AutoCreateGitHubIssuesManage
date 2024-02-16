import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_github_token():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GitHub token not found in environment variables. Please set GITHUB_TOKEN.")
    return token

def create_github_issue(repo_owner, repo_name, title, body):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"Bearer {get_github_token()}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Issue created successfully: {response.json()['html_url']}")
    else:
        print(f"Failed to create issue. Status code: {response.status_code}, Response: {response.text}")

def main(file_path, repo_owner, repo_name):
    with open(file_path, 'r') as file:
        for line in file:
            trimmed_line = line.strip()
            if trimmed_line:
                create_github_issue(repo_owner, repo_name, trimmed_line, "")

if __name__ == "__main__":
    file_path = "file.txt"
    repo_owner = "BaseMax"
    repo_name = "AutoCreateGitHubIssuesManage"

    main(file_path, repo_owner, repo_name)
