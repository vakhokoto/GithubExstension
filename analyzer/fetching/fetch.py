import sys
sys.path.append("./PyGithub");
from github import Github
import json
import getpass


class Fetcher(Object):
    def __init__(self, repository):
        self.repository = repository

    def 