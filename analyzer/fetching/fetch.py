import sys
sys.path.append("./PyGithub");
from github import Github
from ..objects import Contributor, Commit, Repository

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
        data['description'] = self.repository.description
        data['name'] = self.repository.name
        return data

    def get_contributor_stats(self):
        """
        Returns contributor statistics - additions/deletions per week
        """
        contributor_stats = []
        for stat in self.repository.get_stats_contributors():
            stat_info = {}
            stat_info['author'] = stat.author.name
            stat_info['total'] = stat.total
            weeks = []
            for week in stat.weeks:
                weeks.append({'week':week.w, 'additions':week.a, 'deletions':week.d, 'commits':week.c})
            stat_info['weeks'] = weeks
            contributor_stats.append(stat_info)
        return contributor_stats

    def get_commit_stats(self):
        """
        Returns commit statistics - total commits per week
        """
        commit_stats = []
        for stat in self.repository.get_stats_commit_activity():
            commit_stats.append({'date':stat.week, 'total':stat.total, 'days':stat.days})
        return commit_stats

    def get_code_frequency(self):
        """
        Returns code frequency per week
        """
        code_frequency = []
        for stat in self.repository.get_stats_code_frequency():
            code_frequency.append({'date':stat.week, 'additions':stat.additions, 'deletions':stat.deletions})
        return code_frequency

    def get_repository(self):
        """
        Returns Repository object with all the info about the repository
        """
        repo_dict = {
                    'contributors' : self.get_contributors(), 
                    'metadata' : self.get_metadata(), 
                    'contributor stats' : self.get_contributor_stats(), 
                    'commit stats' : self.get_commit_stats(), 
                    'code frequency' : self.get_code_frequency(),
                    'commits' : self.get_commits(limit=10)
                    }
        repo = Repository(repo_dict)
        return repo

    def get_commits(self, limit=None):
        """
        Returns repository's commits
        """
        commits = self.repository.get_commits()
        commits_list = []
        if not limit:
            limit = commits.totalCount
        for commit in commits:
            if limit == 0:
                break
            commit_dict = {}
            commit_dict['sha'] = commit.sha 
            commit_dict['author name'] = commit.author.name
            commit_dict['author username'] = commit.raw_data['author']['login']
            commit_dict['commit message'] = commit.raw_data['commit']['message']
            commit_dict['date'] = commit.commit.author.date
            commit_dict['stats'] = commit.raw_data['stats']
            commit_dict['url'] = commit.html_url
            commit_dict['files'] = []
            for f in commit.files:
                commit_dict['files'].append( {"sha" : f.sha, "filename" : f.filename, "patch" : f.patch} )
            new_commit = Commit(commit_dict)
            commits_list.append(new_commit)
            limit -= 1
        return commits_list
