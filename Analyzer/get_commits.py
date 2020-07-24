import sys
sys.path.append("./PyGithub");
from github import Github
import getpass


def find_repository(account, repo_name):
    repo_name = input("Name of Repository:")
    repository = None
    for repo in account.get_user().get_repos():
        if repo.name == repo_name:
            repository = repo
    if not repository:
        # can't find
        # list of repos
    return repository



def get_commits():
    username = input("Github Username:")
    password = getpass.getpass()
    account = Github(username, password)
    


get_commits()