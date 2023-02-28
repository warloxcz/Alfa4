import re

@staticmethod
def send(conn,data:str):
    conn.send(data.encode())
    
@staticmethod
def receive(conn):
    conn.settimeout(5.0)   
    data = conn.recv(1024)
    return data.decode("utf-8")

@staticmethod
def parse_message(message: str):
        message = message.replace("\n","").replace("\r","")
        if re.match(r'^[A-Z]{13}".*"$',message):
            command = message[:13]
            value = message[14:len(message)-1]
            return (command,value)
        else:
            raise Exception("not a command")