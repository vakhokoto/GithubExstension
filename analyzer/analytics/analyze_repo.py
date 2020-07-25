from collections import Counter
import json

class RepoAnalyzer():
    def __init__(self, repository):
        self.repository = repository

    def weekly_code_frequency(self):
        json_file = json.dumps(self.repository.get_code_frequency(), default=str)
        return json_file

    def language_distribution(self):
        languages = self.repository.get_languages()
        total_lines = sum([lines for lang, lines in languages.items()])
        for lang, lines in languages.items():
            percentage = round((lines / total_lines) * 100, 1)
            languages[lang] = percentage
        json_file = json.dumps(languages)
        return json_file
    
    # Monthly?
    def weekly_commit_frequency(self):
        json_file = json.dumps(self.repository.get_commit_stats(), default=str)
        return json_file

    def top_contributors_monthly(self, n=5):
        last_commits = self.repository.ndays_commits(n=30)
        commit_cnt = Counter()
        commit_authors = []
        for data_dict in last_commits:
            commits = data_dict['commits']
            for commit in commits:
                commit_authors.append(commit.get_author_username())
        
        commit_cnt.update(commit_authors)
        top_contributors = commit_cnt.most_common()[:n]
        json_file = json.dumps(top_contributors, default=str)
        return json_file


# tsalke: last change
# day/week/month commits (easy)  !(from -> to : time period)
# filtering: commits by author
# lines added by author
# lines deleted by author

# tito file rogor itsvleba: deleted & added lines