config_file = open("logger.conf", "r")
try:
    conf = config_file.readlines()
    config_file.close()
        
except:
    print("Sorry, the config file does not exist.")
    sys.exit(1)