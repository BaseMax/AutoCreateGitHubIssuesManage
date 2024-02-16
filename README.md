# Auto Create GitHub Issues - Project Managment

Automatically create GitHub issues from a file using Python.

This script reads a file, splits it into lines, trims each line, and creates issues on your GitHub repository with the titles from the non-empty lines.

## Installation

Clone the repository:

```bash
git clone https://github.com/BaseMax/AutoCreateGitHubIssuesManage.git
```

Navigate to the project directory:

```bash
cd AutoCreateGitHubIssuesManage
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Use:

```bash
GITHUB_TOKEN=xxxxxxxxxxxx python script.py

or

set GITHUB_TOKEN=xxxxxxxxxxxx && python script.py
```

## Usage

Create a GitHub token and set it in the `.env` file:

```dotenv
GITHUB_TOKEN=your_actual_github_token_here
```

Replace the placeholder values in script.py with your actual file path, GitHub username/organization, and repository name.

Run the script:

```bash
python script.py
```

## Demo

```
C:\Users\MAX\Projects\AutoCreateGitHubIssuesManage>python script.py
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/1
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/2
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/3
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/4
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/5
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/6
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/7
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/8
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/9
Issue created successfully: https://github.com/BaseMax/AutoCreateGitHubIssuesManage/issues/10
```

## License

This project is licensed under the MIT License.

Copyright © 2024 Max Base
