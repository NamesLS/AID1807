'''
ftp 文件服务器
'''
from socket import *
import os,sys,time
from signal import *

# 文件库路径
FILE_PATH = "/home/tarena/ftp/"
ADDR = ("0.0.0.0",8888)
# 讲文件服务器功能写在类中
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        # 获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)
        files = ""
        for file in file_list:
            if file[0] != "." and os.path.isfile(FILE_PATH + file):
                files = files + file + " "
        self.connfd.sendall(files.encode())

    def getfile(self):
        wjm = self.connfd.recv(1024).decode()
        try:
            f = open(FILE_PATH + wjm,"rb")
        except:
            self.connfd.send('文件不存在'.encode())
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()
        print("%s 发送完毕\n" % wjm)


    def putfile(self):
        self.connfd.send(b"OK")
        wjm = self.connfd.recv(1024).decode()
        try:
            f = open(FILE_PATH + wjm,"wb")
            while True:
                data = self.connfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
            print("%s 接收完毕\n" % wjm)
        except:
            self.connfd.send('文件上传失败'.encode())
            return
# 创建套接字,接收客户端,创建新的进程
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    # 处理子进程退出
    signal(SIGCHLD,SIG_IGN)
    print("Listen the port 8000 .....")
    while True:
        try:
            connfd,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常:",e)
            continue
        print("已连接客户端:",addr)
        # 为客户端创建新的进程处理请求
        pid = os.fork()
        # 子进程处理具体请求
        if pid == 0:
            s.close()
            ftp = FtpServer(connfd)
            # 判断客户端请求
            while True:
                data = connfd.recv(1024).decode()
                if not data or data == "Q":
                    connfd.close()
                    sys.exit("客户端退出")
                elif data == "L":
                    ftp.do_list()
                elif data == "G":
                    ftp.getfile()
                elif data == "P":
                    ftp.putfile()

        else:
            # 父进程或者创建失败都继续等待下个客户端连接
            connfd.close()
            continue

if __name__ == "__main__":
    main()
