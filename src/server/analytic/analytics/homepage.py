import json

class Homepage():
    """
    Information for homepage rendering
    repository - repository object

    Attributes
    ----------
    repository : Repository object
        current repository's object
    
    Methods
    ----------
    get_repo_name()
        gets first 10 days commits
    get_description()
        returns repository's description
    get_topics()
        returns topics of a repository
    get_commits()
        returns list of repository's commits
    """
    def __init__(self, repository):
        self.repository = repository

    def get_repo_name(self):
        """
        Returns repository name
        
        Format
        ----------
        { 'name' : str }
        """
        jsn = { 'name' : self.repository.get_name() }
        return json.dumps(jsn)

    def get_description(self):
        """
        Returns repository name
        
        Format
        ----------
        { 'name' : str }
        """
        jsn = { 'description' : self.repository.get_description() }
        return json.dumps(jsn)

    def get_topics(self):
        """
        Returns repository's topics
        
        Format
        ----------
        [ str ]
        """
        return json.dumps(self.repository.get_topics())

    def get_commits(self):
        """
        Returns repository's last 10 commits
        Each commit consists of author's username, commit message,
        date, url, added and deleted line numbers
        """
        coms = []
        for com in self.repository.n_commits(n=10):
            cur_com = {}
            cur_com['author username'] = com.get_author_username()
            cur_com['commit_msg'] = com.get_commit_msg()
            cur_com['date'] = com.get_date()
            cur_com['url'] = com.get_url()
            cur_com['added'] = com.get_num_line_added()
            cur_com['deleted'] = com.get_num_line_deleted()
            coms.append(cur_com)
        return json.dumps(coms, default=str)

    