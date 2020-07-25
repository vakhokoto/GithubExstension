class User(Object):
    def __init__(self, login, name, url):
        self.login = login
        self.name = name
        self.url = url
    
    def get_login(self):
        return self.login
    
    def get_name(self):
        return self.name

    def get_url(self):
        return self.url