import json
from collections import Counter

class ContributorAnalyzer():
    def __init__(self, username, repository):
        self.username = username
        self.repository = repository

    def get_commits(self):
        commits = []
        for com in self.repository.commits_by_user():
            cur_com = {}
            cur_com['author name'] = com.get_author_name()
            cur_com['author username'] = com.get_author_username()
            cur_com['commit_msg'] = com.get_commit_msg()
            cur_com['date'] = com.get_date()
            cur_com['url'] = com.get_url()
            cur_com['added'] = com.get_num_line_added()
            cur_com['deleted'] = com.get_num_line_deleted()
            commits.append(cur_com)
        return commits

    def get_name(self):
        for cont in self.repository.get_contributors():
            if self.username == cont.get_login():
                return cont.get_name()
        return self.username

    def get_added_lines(self):
        added = 0
        for com in self.repository.commits_by_user():
            added += com.get_num_line_added()
        return added

    def get_deleted_lines(self):
        deleted = 0
        for com in self.repository.commits_by_user():
            deleted += com.get_num_line_deleted()
        return deleted

    def weekly_commits_stats(self):
        contributor_stats = self.repository.get_contributor_stats()
        for stat in contributor_stats:
            if stat['author'] == self.username:
                return stat

    def get_favorite_files(self, n=5):
        user_commits = self.repository.commits_by_user(self.username)
        file_cnt = Counter()
        for commit in user_commits:
            filenames = [changed_file['filename'] for changed_file in commit.get_files()]
            file_cnt.update(filenames)
        top_files = file_cnt.most_common()[:n]
        return top_files
