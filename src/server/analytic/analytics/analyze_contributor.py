import json
from collections import Counter

class ContributorAnalyzer():
    def __init__(self, username, repository):
        self.username = username
        self.repository = repository

    def get_commits(self):
        commits = []
        for com in self.repository.commits_by_user(self.username):
            cur_com = {}
            cur_com['author name'] = com.get_author_name()
            cur_com['author username'] = com.get_author_username()
            cur_com['commit_msg'] = com.get_commit_msg()
            cur_com['date'] = com.get_date()
            cur_com['url'] = com.get_url()
            cur_com['added'] = com.get_num_line_added()
            cur_com['deleted'] = com.get_num_line_deleted()
            commits.append(cur_com)
        return json.dumps(commits, default=str)

    def get_name(self):
        name = self.repository.name_of_user(self.username)
        dct = {'name' : name}
        return json.dumps(dct, default=str)

    def get_added_lines(self):
        added = 0
        for com in self.repository.commits_by_user(self.username):
            added += com.get_num_line_added()
        dct = {'added lines' : added}
        return json.dumps(dct, default=str)

    def get_deleted_lines(self):
        deleted = 0
        for com in self.repository.commits_by_user(self.username):
            deleted += com.get_num_line_deleted()
        dct = {'deleted lines' : deleted}
        return json.dumps(dct, default=str)

    def weekly_commits_stats(self):
        commit_stats = {}
        contributor_stats = self.repository.get_contributor_stats()
        name = self.repository.name_of_user(self.username)
        for stat in contributor_stats:
            if stat['author'] == name:
                commit_stats = stat
                break
        return json.dumps(commit_stats, default=str)
        

    def get_favorite_files(self, n=5):
        user_commits = self.repository.commits_by_user(self.username)
        file_cnt = Counter()
        for commit in user_commits:
            filenames = [changed_file['filename'] for changed_file in commit.get_files()]
            file_cnt.update(filenames)
        top_files = file_cnt.most_common()[:n]
        return json.dumps(top_files, default=str)
