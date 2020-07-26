import json
from collections import Counter

class ContributorAnalyzer():
    """
    A class used to analyze a contributor of the repository 

    Attributes
    ----------
    username : str
        username handle of a contributor
    repository : Repository object
        current repository's object

    Methods
    ----------
    get_commits()
        returns all commits of current repository in json
    get_name()
        returns name of repository in json
    get_added_lines()
        returns number of added lines in json
    get_deleted_lines()
        returns number of deleted lines in json
    weekly_commits_stats()
        returns weekly statistics of commits in json
    get_favorite_files(n=5)
        returns n top updated files 
    """
    def __init__(self, username, repository):
        """
        Parameters
        ----------
        username : str
            username handle of a contributor
        repository : Repository object
            current repository's object
        """
        self.username = username
        self.repository = repository

    def get_commits(self):
        """
        Returns commits from current repository
        Single commit has fullname, username of an author
        Commit message, date, url, added and deleted lines number
        """
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
        """
        Returns name of the repository
        'name' : name
        """
        name = self.repository.name_of_user(self.username)
        dct = {'name' : name}
        return json.dumps(dct, default=str)

    def get_added_lines(self):
        """
        Returns number of added lines in json

        Format
        ----------
        'added lines' : number
        """
        added = 0
        for com in self.repository.commits_by_user(self.username):
            added += com.get_num_line_added()
        dct = {'added lines' : added}
        return json.dumps(dct, default=str)

    def get_deleted_lines(self):
        """
        Returns deleted lines count

        Format
        ----------
        'deleted lines' : deleted
        """
        deleted = 0
        for com in self.repository.commits_by_user(self.username):
            deleted += com.get_num_line_deleted()
        dct = {'deleted lines' : deleted}
        return json.dumps(dct, default=str)

    def weekly_commits_stats(self):
        """
        Returns weekly statistics about commits

        Format
        ----------
        'author' : fullname
        'total' : int (commits count)
        'weeks' : [ 
                    { 
                        'week' : str (week count)
                        'additions' : int
                        'deletions' : int
                        'commits' : int
                    }
                  ]
        """
        commit_stats = {}
        contributor_stats = self.repository.get_contributor_stats()
        name = self.repository.name_of_user(self.username)
        for stat in contributor_stats:
            if stat['author'] == name:
                commit_stats = stat
                break
        return json.dumps(commit_stats, default=str)

    def get_favorite_files(self, n=5):
        """
        Returns n most popular files

        Parameters
        ----------
        n : int, optional
            number of top files requested
        """
        user_commits = self.repository.commits_by_user(self.username)
        file_cnt = Counter()
        for commit in user_commits:
            filenames = [changed_file['filename'] for changed_file in commit.get_files()]
            file_cnt.update(filenames)
        top_files = file_cnt.most_common()[:n]
        return json.dumps(top_files, default=str)

        
        