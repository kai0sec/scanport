import socket
import threading
import Queue

class DoRun(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue=queue
    def run(self):
        while not self._queue.empty():
            ip=self._queue.get()
            port =[21,22,445,80,3389,8080]
            for i in port:
                try:
                    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.connect((ip,i))
                    s.send("hello world\n")
                    back=s.recv(1024)
                    if back:
                        print "ip: %s:%d"%(ip,i)
                    s.close
                except:
                    pass
            
#ips=["182.243.67.58","127.0.0.1","8.8.8.8","182.243.67.58"]
ips=["216.189.157.152"]
def main():
    threads=[]
    threads_count=4
    quequ=Queue.Queue()
    
    for ip in ips:
        quequ.put(ip)
    
    for i in range(threads_count):
        threads.append(DoRun(quequ))
    
    for i in threads:
        i.start()
    
    for i in threads:
        i.join()
        
if __name__=='__main__':
    main()