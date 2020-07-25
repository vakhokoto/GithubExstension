import sys
sys.path.append("./PyGithub");
from github import Github
import json
import getpass


def find_repository(account, repo_name):
    """
    Finds repository
    Parameters:
        account   - github.MainClass.Github, user's account
        repo_name - str, repository's name 
    """
    repository = None
    for repo in account.get_user().get_repos():
        if repo.name == repo_name:
            repository = repo
    if not repository:
        print("Repository not found")
    return repository

def get_commits(repository: str) -> json:
    """
    Collects commits and their info from specified repository
    Info of a single commit consists of:
        sha, author, commit message, date, stats, url, files
    
    Parameters:
        repository - str, repository we need commits from

    """
    commits = repository.get_commits()

    json_tobe = []
    for commit in commits:
        cur_commit = {}
        cur_commit['sha'] = commit.sha 
        cur_commit['author name'] = commit.author.name
        cur_commit['author username'] = commit.raw_data['author']['login']
        cur_commit['commit message'] = commit.raw_data['commit']['message']
        cur_commit['date'] = commit.raw_data['commit']['author']['date']
        cur_commit['stats'] = commit.raw_data['stats']
        cur_commit['url'] = commit.html_url
        cur_commit['files'] = []
        for f in commit.files:
            cur_commit['files'].append( {"sha" : f.sha, "filename" : f.filename, "patch" : f.patch} )
        json_tobe.append(cur_commit)
    jsn = json.dumps(json_tobe, indent=4)

username = input("Github Username: ")
password = getpass.getpass()
account = Github(username, password)
repo_name = input("Name of Repository: ")
repository = find_repository(account, repo_name)
get_commits(repository)

