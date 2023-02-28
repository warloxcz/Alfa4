from Server import Server
from Dictionary import Dictionary
import json

def main():
    f = open("config.json")
    config = json.load(f)
    d = Dictionary(config["name"],config["words"])
    s = Server(config["ip"],config["port"],d,config["scan"]["port_range"],config["scan"]["ip_range"])

if __name__ == "__main__":
    main()


