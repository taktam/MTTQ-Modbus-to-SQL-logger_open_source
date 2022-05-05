import sys
import paho.mqtt.client as mclient

class mqtt:
    '''Make the mqtt connection...'''
    def __init__(self, client_name, host, port, keep_alive):
        self.client_name = client_name
        self.host = host
        self.port = port
        self.keep_alive = keep_alive

    def client_name (self):
        return self.client_name
    
    def host (self):
        return self.host
    
    def port (self):
        return self.port
    
    def keep_alive (self):
        return self.keep_alive
    
    def create_client(self):
        return mclient.Client(self.client_name)
        
            
def clean_str(text):
    text = text.replace("\n", "")
    text = text.replace("=", "")
    text = text.replace(" ", "")
    text = text.replace("mqtt_client_name", "")
    text = text.replace("mqtt_host", "")
    text = text.replace("mqtt_port", "")
    text = text.replace("mqtt_keep_alive", "")
    return text
    
def mqtt_config(confile):
    config_file = open(confile, "r")
    try:
        conf = config_file.readlines()
        config_file.close()
        for i in conf:
            if ("mqtt_client_name" in i):
                client_name = clean_str(i)
            if ("mqtt_host" in i):
                host = clean_str(i)
            if ("mqtt_port" in i):
                port = int(clean_str(i))
            if ("mqtt_keep_alive" in i):
                keep_alive = int(clean_str(i))
            
        mqtt_con = mqtt(client_name, host, port, keep_alive)
        return mqtt_con
    
    except:
        print("Sorry, the config file does not exist.")
        sys.exit(1)