class Contributor():
    """
    Class for contributor object
    """
    def __init__(self, login: str, name: str, url: str):
        """
        Initializing contributor object.
        Contains following fields:
            login - username of user
            name - name of user
            url - github url of user
        """
        self.login = login
        self.name = name
        self.url = url
    
    def get_login(self):
        return self.login
    
    def get_name(self):
        return self.name

    def get_url(self):
        return self.url