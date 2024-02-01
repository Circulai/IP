import requests
import json
import base64

def commit_file():
    with open(".env","r") as f:
        lines = f.readlines()

        access_token = lines[0]
        owner = lines[1]
        repo = lines[2]
        path = lines[3]

    branch = 'main'  # or the branch you want to commit to

    api_url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'

    try:
        response = requests.get(api_url, headers={'Authorization': f'Bearer {access_token}'})
        data = response.json()

        updated_data = {
            'key': 'python',
            'updated': True
        }

        content = base64.b64encode(json.dumps(updated_data, indent=2).encode()).decode()
        sha = data['sha']

        commit_message = 'Update data.json'
        commit_url = f'https://api.github.com/repos/{owner}/{repo}/git/refs/heads/{branch}'
        commit_data = {
            'sha': sha,
            'force': True
        }

        requests.patch(commit_url, headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=commit_data)

        requests.put(api_url, headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'},
                     json={
                         'message': commit_message,
                         'content': content,
                         'sha': sha,
                         'branch': branch
                     })

        print('File committed successfully!')
    except Exception as error:
        print('Error:', error)
        print('Error committing file. Check the console for details.')

commit_file()

