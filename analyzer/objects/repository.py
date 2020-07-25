
class Repository():
    def __init__(self, repo_info : dict):
        """
        Class representing a repository

        metadata - languages, topics & description
        """
        self.contributors = repo_info['contributors']
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
        return self.code_frequency

    def last_weeks_commits(self):
        
    
    
