from datetime import datetime, timedelta, date

class Repository():
    def __init__(self, repo_info : dict):
        """
        Class representing a repository

        metadata - name, languages, topics & description
        """
        self.contributors = repo_info['contributors']
        self.num_contributors = len(self.contributors)
        self.metadata = repo_info['metadata']
        self.contributor_stats = repo_info['contributor stats']
        self.commit_stats = repo_info['commit stats']
        self.code_frequency = repo_info['code frequency']
        self.commits = repo_info['commits']

    def get_contributors(self):
        return self.contributors

    def get_metadata(self):
        return self.metadata

    def get_name(self):
        return self.metadata['name']

    def get_languages(self):
        return self.metadata['languages']

    def get_language_lines_cnt(self, lang : str):
        return self.metadata['languages'][lang]

    def get_topics(self):
        return self.metadata['topics']

    def get_description(self):
        return self.metadata['description']

    def get_contributor_stats(self):
        return self.contributor_stats

    def get_commit_stats(self):
        return self.commit_stats
    
    def get_code_frequency(self):
        return self.code_frequency

    def commits_by_user(self, username):
        user_commits = []
        

    # TODO: current_date = start_date
    def ndays_commits(self, n=30):
        current_date = date.today()
        nd_commits = []
        for i in range(n):
            cur_day_info = {}
            commits_list = []
            cur_date = current_date - timedelta(days=i)
            for commit in self.commits:
                commit_date = commit.get_date()
                if commit_date.date() == cur_date:
                    commits_list.append(commit)
                elif commit_date.date() < cur_date:
                    break
            cur_day_info['date'] = commit_date
            cur_day_info['commits'] = commits_list
            nd_commits.append(cur_day_info)
        return nd_commits
    
    def n_commits(self, n=10):
        coms = []
        for commit in self.commits:
            if n == 0:
                break
            coms.append(commit)
            n -= 1
        return coms