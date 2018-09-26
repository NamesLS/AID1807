from socket import *
import sys,time

#基本文件操作功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            data = self.sockfd.recv(4096).decode()
            files = data.split(" ")
            for file in files:
                print(file)
            print("文件列表展示完毕\n")
        else:
            print(data)

    def getfile(self,filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s 下载完毕\n"%filename)
        else:
            print(data)
    def do_quit(self):
        self.sockfd.send(b"Q")
# 创建套接字
def show_menu():
    print("+" + "-" * 5 + "命令选项" + "-" * 5 + "+")
    print("| 1) 查看所有文件  |")
    print("| 2) 下载文件      |")
    print("| 3) 上传文件      |")
    print("| 4) 退出          |")
    print("+" + "-" * 18 + "+")
def main():
    # if len(sys.argv) < 3:
    #     print("argv is error")
    # HOST = sys.argv[1]
    # PORT = int(sys.argv[2])
    # ADDP = (HOST,PORT)    
    sockfd = socket(AF_INET,SOCK_STREAM)
    try:
        sockfd.connect(('127.0.0.1',8888))
    except:
        print("连接服务器失败")
        return
    ftp = FtpClient(sockfd) # 功能类的对象
    while True:
        show_menu()
        cmd = input("请选择:")
        if cmd.strip() == "1":
            ftp.do_list()
        elif cmd[0] == "2":
            filename = cmd.split(" ")[-1]
            ftp.getfile(filename)
        elif cmd.strip() == "4":
            ftp.do_quit()
            sockfd.close()
            sys.exit("谢谢使用")
        else:
            print("输入不合法")
            continue
if __name__ == "__main__":
    main()
