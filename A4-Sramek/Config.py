import json

class Config:
    def __init__(self,ip_address,port,word):
        self.ip_address = ip_address
        self.port = port
        self.word = word

with open('config.json', 'r') as f:
      config_data = json.load(f)
config = Config(config_data['ip_address'],config_data['port'],config_data['word'])
