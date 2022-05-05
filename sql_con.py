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
        return self.port
    
    def db (self):
        return self.db

def clean_str(text):
    text = text.replace("\n", "")
    text = text.replace("=", "")
    text = text.replace("db", "")
    text = text.replace("sql_port", "")
    text = text.replace("sql_host", "")
    text = text.replace("sql_user", "")
    text = text.replace("sql_passwd", "")
    text = text.replace(" ", "")
    text = text.replace("mqtt_client_name", "")
    return text
    

def sql_config(confile):
    config_file = open(confile, "r")
    try:
        conf = config_file.readlines()
        config_file.close()
        for i in conf:
            if ("sql_user" in i):
               user = clean_str(i)
            if ("sql_passwd" in i):
               passwd = clean_str(i)
            if ("sql_host" in i):
               host = clean_str(i)
            if ("sql_port" in i):
               port = clean_str(i)
            if ("db" in i):
               db = clean_str(i)
                
        sql_con = connect(user, passwd, host, port, db)
        return sql_con
    
    except:
        print("Sorry, the config file does not exist.")
        sys.exit(1)
    