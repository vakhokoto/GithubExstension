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
