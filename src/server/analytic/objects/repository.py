from datetime import datetime, timedelta, date

class Repository():
    """
    Class representing a repository

    Attributes
    ----------
    contributors : list
        list of strings, contains contributors
    num_contributors : int
        number of contributors in repository
    metadata : dict
        dictionary containing languages, topics, description and name of repository
    contributor_stats : list
        list containing author's name, total commits count and statistics per week
    commit_stats : list
        commits statistics given per week
    code_frequency : list
        code lines deletion and addition given per day
    commits : list
        list of commit objects


    Methods
    ----------
    get_contributors()
        returns list of contributors
    get_metadata()
        returns metadata dictionary of a repository
    get_name()
        returns name of a repository
    get_languages()
        returns language names repository is written in
    get_language_lines_cnt()
        returns line count of a specified language
    get_topics()
        returns list of repository's topics
    get_description()
        returns description of repository
    get_contributor_stats()
        returns statistics of contributor activities
    get_commit_stats()
        returns weekly statistics of commits
    get_code_frequency()
        returns line addition and deletion statistics
    name_of_user()
        returns fullname of a contributor
    commits_by_user()
        returns commits made by a person
    commits_by_fullname()
        returns commits made by a person
    get_commits()
        returns list of commit objects
    ndays_commits()
        returns list of commits
    n_commits()
        returns list of n commits
    """
    def __init__(self, repo_info : dict):
        self.contributors = repo_info['contributors']
        self.num_contributors = len(self.contributors)
        self.metadata = repo_info['metadata']
        self.contributor_stats = repo_info['contributor stats']
        self.commit_stats = repo_info['commit stats']
        self.code_frequency = repo_info['code frequency']
        self.commits = repo_info['commits']
        self.issues = repo_info['issues']

    def get_issues(self):
        return self.issues

    def get_contributors(self):
        """
        Returns list of contributors
        """
        return self.contributors

    def get_metadata(self):
        """
        Returns metadata dictionary of a repository
        Metadata consists of dictionary containing languages, 
        topics, description and name of repository
        """
        return self.metadata

    def get_name(self):
        """
        Returns name of a repository
        """
        return self.metadata['name']

    def get_languages(self):
        """
        Returns language names repository is written in
        """
        return self.metadata['languages']

    def get_language_lines_cnt(self, lang : str):
        """
        Returns line count of a specified language

        Parameters
        ----------
        lang : str
            specific language
        """
        return self.metadata['languages'][lang]

    def get_topics(self):
        """
        Returns list of repository's topics
        """
        return self.metadata['topics']

    def get_description(self):
        """
        Returns description of repository
        """
        return self.metadata['description']

    def get_contributor_stats(self):
        """
        Returns statistics of contributor activities

        Format
        ----------
        [
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
        ]
        """
        return self.contributor_stats

    def get_commit_stats(self):
        """
        Returns weekly statistics of commits 

        Format
        ----------
        [
            {
                'date' : str (week count)
                'total' : int
                'days' : [int, int, int, int, int, int, int]
            }
        ]
        """
        return self.commit_stats
    
    def get_code_frequency(self):
        """
        Returns line addition and deletion statistics 
        per week

        Format
        ----------
        [ 
            { 
                'date' : str (week count)
                'additions' : int
                'deletions' : int
            }
        ]
        """
        return self.code_frequency

    def name_of_user(self, username):
        """
        Returns fullname of a contributor, based on his/her
        username

        Parameters
        ----------
        username : str
            username of a contributor
        """
        name = username
        for cont in self.get_contributors():
            if username == cont.get_login():
                name = cont.get_name()
                break
        return name

    def commits_by_user(self, username):
        """
        Returns commits made by a person specified with
        a username

        Parameters
        ----------
        username : str
            username of a contributor
        """
        user_commits = []
        for commit in self.commits:
            if commit.get_author_username() == username:
                user_commits.append(commit)
        return user_commits

    def commits_by_fullname(self, fullname):
        """
        Returns commits made by a person specified with
        a fullname

        Parameters
        ----------
        fullname : str
            fullname of a contributor
        """
        user_commits = []
        for commit in self.commits:
            if commit.get_author_name() == fullname:
                user_commits.append(commit)
        return user_commits
        
    def get_commits(self):
        """
        Returns list of commit objects, whole repository's
        commits
        """
        return self.commits

    def ndays_commits(self, n=30):
        """
        Returns list of commits made in n days

        Parameters
        ----------
        n : int, optional
            number of days requested
        """
        current_date = date.today()
        nd_commits = []
        for i in range(n):
            cur_day_info = {}
            commits_list = []
            cur_date = current_date - timedelta(days=i)
            for commit in self.commits:
                commit_date = commit.get_date()
                if commit_date.date() == cur_date:
                    commits_list.append(commit)
                elif commit_date.date() < cur_date:
                    break
            cur_day_info['date'] = commit_date
            cur_day_info['commits'] = commits_list
            nd_commits.append(cur_day_info)
        return nd_commits
    
    def n_commits(self, n=10):
        """
        Returns list of n commits

        Parameters
        ----------
        n : int, optional
            number of commits requested
        """
        coms = []
        for commit in self.commits:
            if n == 0:
                break
            coms.append(commit)
            n -= 1
        return coms
        