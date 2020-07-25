class Commit():
    def __init__(self, commit_info):
        """
        Class representing a single commit
        Methods:
            get_sha - sha of a commit
            get_author_name - name of an author
            author_username - username of an author
            get_commit_msg - commit message
            get_date - date of a commit
            get_stats - statistics of a commit, lines added/deleted
            get_num_line_changed - number of lines changed
            get_num_line_added - number of lines added
            get_num_line_deleted - number of lines deleted
            get_url - url of a commit
            get_files - info about files changed, contains sha, filename and patch
            get_files_changed_count - count of files changed
        """
        self.sha = commit_info['sha']
        self.author_name = commit_info['author name']
        self.author_username = commit_info['author username']
        self.commit_msg = commit_info['commit message']
        self.date = commit_info['date']
        self.stats = commit_info['stats']
        self.url = commit_info['url']
        self.files = commit_info['files']

    def get_sha(self):
        return self.sha
    
    def get_author_name(self):
        return self.author_name

    def get_author_username(self):
        return self.author_username

    def get_commit_msg(self):
        return self.commit_msg

    def get_date(self):
        return self.date
    
    def get_stats(self):
        return self.stats

    def get_num_line_changed(self):
        return self.stats['total']

    def get_num_line_added(self):
        return self.stats['additions']

    def get_num_line_deleted(self):
        return self.stats['deletions']
    
    def get_url(self):
        return self.url

    def get_files(self):
        return self.files

    def get_files_changed_count(self):
        return len(self.files)
    