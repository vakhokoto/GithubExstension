from datetime import datetime, timedelta, date

class Repository():
    def __init__(self, repo_info : dict):
        """
        Class representing a repository

        metadata - languages, topics & description
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
        return self.code_frequencyfor 

    def ndays_commits(self, n=7):
        cur_date = date.today()
        print('cur date', cur_date, type(cur_date))
        nd_commits = []
        for i in range(n):
            cur_date += timedelta(days=i)
            cur_day_info = {}
            commits_list = []

            for commit in self.commits:
                commit_date = datetime(commit.get_date())
                print(commit_date)
                commit_date = datetime.strptime(commit.get_date(), '%Y-%m-%d')
                print('commit date', commit_date, type(commit_date))
                if commit_date == cur_date:
                    commits_list.append(commit)
                elif commit_date > cur_date:
                    break
            cur_day_info['date'] = cur_date
            cur_day_info['commits'] = commits_list
            nd_commits.append(cur_day_info)
        return nd_commits
    
