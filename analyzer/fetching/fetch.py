import sys
sys.path.append("./PyGithub");
from github import Github
from objects import Contributor, Commit

class Fetcher():
    def __init__(self, repository):
        self.repository = repository

    def get_contributors(self):
        """
        Returns list of contributors
        """
        contributors = []
        for user in self.repository.get_contributors():
            contributor = Contributor(login=user.login, name=user.name, url=user.html_url)
            contributors.append(contributor)
        return contributors

    def get_metadata(self):
        """
        Returns used languages, topics and description of the repository
        """
        data = {}
        data['languages'] = self.repository.get_languages()
        data['topics'] = self.repository.get_topics()
        data['description'] = self.repository.get_description()
        return data

    def get_commits(self):
        commits = self.repository.get_commits()
        commits_list = []
        for commit in commits:
            commit_dict = {}
            commit_dict['sha'] = commit.sha 
            commit_dict['author'] = commit.author.name
            commit_dict['commit message'] = commit.raw_data['commit']['message']
            commit_dict['date'] = commit.raw_data['commit']['author']['date']
            commit_dict['stats'] = commit.raw_data['stats']
            commit_dict['url'] = commit.html_url
            commit_dict['files'] = []
            for f in commit.files:
                commit_dict['files'].append( {"sha" : f.sha, "filename" : f.filename, "patch" : f.patch} )
            new_commit = Commit(commit_dict)
            commits_list.append(new_commit)
        return commits_list