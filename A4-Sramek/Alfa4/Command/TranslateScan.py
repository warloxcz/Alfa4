from ICommand import ICommand
import sys
sys.path.append("./")
from Log import Log
from TCP import send, parse_message, receive
import socket
import ipaddress

class TranslateScan(ICommand):
    def __init__(self,conn,word,dict,ip_address,port_range) -> None:
        self.conn = conn
        self.word = word
        self.dict = dict
        self.ip_address = ip_address
        self.port_range = port_range
    

    def execute(self):
        found = False
        for ip_address in self.ip_address:
            for port in range(self.port_range[0], self.port_range[1]+1):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    Log.out(f"{ip_address}:{port}")
                    s.settimeout(1)
                    try:
                        s.connect((str(ip_address),port))
                        send(s,f'TRANSLATEPING"{self.dict.name}"')
                        recv = receive(s)
                        parsed = parse_message(recv)
                        Log.out(parsed)
                        if parsed[0] != "TRANSLATEPONG":
                            continue
                        recv = send(s,f'TRANSLATELOCL"{self.word}"')
                        recv = receive(s)
                        Log.out(recv)
                        parsed = parse_message(recv)
                        if parsed[0] == "TRANSLATEDSUC":
                            send(self.conn,f'TRANSLATEDSUC"{parsed[1]}"')
                            found = True
                            break
                        if parsed[0] == "TRANSLATEDERR":
                            continue
                    except Exception as e:
                        Log.out(e)
            if found:
                break
        if not found:
            send(self.conn,f'TRANSLATEDERR"neni"')
        
                