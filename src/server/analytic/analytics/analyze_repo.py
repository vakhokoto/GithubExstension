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

    def get_most_fire_files(self, n=5):
        file_cnt = Counter()
        for commit in self.repository.n_commits(n):
            filenames = [cf['filename'] for cf in commit.get_files()]
            file_cnt.update(filenames)
        top_files = file_cnt.most_common()[:n]
        json_file = json.dumps(top_files, default=str)
        return json_file

