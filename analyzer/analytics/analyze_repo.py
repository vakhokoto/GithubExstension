from collections import Counter

class RepoAnalyzer():
    def __init__(self, repository):
        self.repository = repository

    def weekly_code_frequency(self):
        print('zd')

    def language_distribution(self):
        languages = self.repository.get_languages()
        total_lines = sum([lines for lang, lines in languages.items()])
        for lang, lines in languages.items():
            percentage = round((lines / total_lines) * 100, 1)
            languages[lang] = percentage
        return languages
    
    def commit_frequency(self):
        print('zd')

    def top_contributors_monthly(self, n=5):
        last_commits = self.repository.ndays_commits(n=30)
        commit_cnt = Counter()
        commit_authors = [commit.get_author_username() for commit in last_commits]
        commit_cnt.update(commit_authors)
        top_contributors = commit_cnt.most_common()[:n]
