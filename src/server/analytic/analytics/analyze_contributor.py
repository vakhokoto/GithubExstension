import json

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
        pass

    def get_added_lines(self):
        pass

    def get_deleted_lines(self):
        pass

    def weekly_commits_stats(self):
        pass

    def get_favorite_files(self):
        pass

    