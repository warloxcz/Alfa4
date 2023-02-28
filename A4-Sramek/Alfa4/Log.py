from datetime import datetime

path = "log.txt"
mode = 1 # 0 = print to cli, 1 = writing to file
class Log:
    @staticmethod
    def out(content):
        if mode == 0:
            print(content)
        else:
            with open(path,"a+") as f:
                now = datetime.now()
                out_str = f"{now}> {content}\n"
                f.write(out_str)
