import sys

class connect:
    '''Make the connection based on the configuration file'''
    def __init__(self, user, passwd, host, port, db):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.db = db

    def user (self):
        return self.user
    
    def passwd (self):
        return self.passwd
    
    def host (self):
        return self.host
    
    def port (self):
        return int(self.port)
    
    def db (self):
        return self.db

def clean_str(text):
    text = text.replace("\n", "")
    text = text.replace("=", "")
    text = text.replace("db", "")
    text = text.replace("port", "")
    text = text.replace("host", "")
    text = text.replace("user", "")
    text = text.replace("passwd", "")
    text = text.replace(" ", "")
    return text
    

def load_config(confile):
    config_file = open(confile, "r")
    try:
        conf = config_file.readlines()
        config_file.close()
        for i in conf:
            if ("user" in i):
               user = clean_str(i)
            if ("passwd" in i):
               passwd = clean_str(i)
            if ("host" in i):
               host = clean_str(i)
            if ("port" in i):
               port = clean_str(i)
            if ("db" in i):
               db = clean_str(i)
                
        con = connect(user, passwd, host, port, db)
        #print (con.user)
        return con
    except:
        print("Sorry, the config file does not exist.")
        sys.exit(1)
    