import json

class Homepage():
    def __init__(self, repository):
        """
        Information for homepage rendering
        repository - repository object
        
        Methods
        get_commits - gets first 10 days commits
        """
        self.repository = repository

    def get_repo_name(self):
        jsn = { 'name' : self.repository.get_name() }
        return json.dumps(jsn)

    def get_description(self):
        jsn = { 'description' : self.repository.get_description() }
        return json.dumps(jsn)

    def get_topics(self):
        return json.dumps(self.repository.get_topics())

    def get_commits(self):
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

    