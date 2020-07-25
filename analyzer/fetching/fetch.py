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
        data['description'] = self.repository.description
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