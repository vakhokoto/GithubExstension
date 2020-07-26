from analytic import Fetcher, RepoAnalyzer, ContributorAnalyzer, Homepage
import sys
sys.path.append("./PyGithub")
from github import Github
import getpass
from datetime import datetime


username = input("Github Username: ")
password = getpass.getpass()

account = Github(username, password)
repo_name = input("Name of Repository: ")
repository = account.get_user().get_repo(name=repo_name)
fetcher = Fetcher(repository)
repo = fetcher.get_repository()
repo_analyzer = RepoAnalyzer(repo)
homepage = Homepage(repo)
contr_analyzer = ContributorAnalyzer(repository=repo, username='koaning')

# test repo analyzer
# print(repo_analyzer.weekly_code_frequency())
# print(repo_analyzer.language_distribution())
# print(repo_analyzer.weekly_commit_frequency())
# print(repo_analyzer.top_contributors_monthly())
# print(repo_analyzer.get_most_fire_files())

# test homepage 
# print(homepage.get_repo_name())
# print(homepage.get_description())
# print(homepage.get_topics())
# print(homepage.get_commits())

# test contributor analyzer
# print(contr_analyzer.get_commits())
# print(contr_analyzer.get_name())
# print(contr_analyzer.get_added_lines())
# print(contr_analyzer.get_deleted_lines())
# print(contr_analyzer.weekly_commits_stats())
# print(contr_analyzer.get_favorite_files())