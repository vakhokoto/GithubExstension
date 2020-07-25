from fetching import Fetcher
from analytics import RepoAnalyzer
import sys
sys.path.append("./PyGithub");
from github import Github
import json
import getpass


username = input("Github Username: ")
password = getpass.getpass()
account = Github(username, password)
repo_name = input("Name of Repository: ")
repository = None
for repo in account.get_user().get_repos():
        if repo.name == repo_name:
            repository = repo

fetcher = Fetcher(repository)
contributors = fetcher.get_contributors()
metadata = fetcher.get_metadata()
contributor_stats = fetcher.get_contributor_stats()
commit_stats = fetcher.get_commit_stats()
code_freq = fetcher.get_code_frequency()
#print(contributors, metadata, contributor_stats, commit_stats, code_freq)

#commits = fetcher.get_commits(limit = 9)
repo = fetcher.get_repository()

print(repo.ndays_commits())

#Pytorch_Part_Of_Speech_Tagging


"""
for contr in repo.get_contributors():
    print(contr.get_login())

print("DESC: ", repo.get_description())
print("")
print("CONTRIBUTOR STATS: ", repo.get_contributor_stats())
print("")
print("COMMIT STATS: ", repo.get_commit_stats())
print("")
print("CODE FREQUENCY: ", repo.get_code_frequency())
"""
