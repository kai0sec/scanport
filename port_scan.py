from optparse import OptionParser  
import socket
import threading
import Queue
import sys
#coding:utf-8
port =[21,22,445,80,81,3389,8080,9090]    

class DoRun(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue=queue
        
    def run(self):
        while not self._queue.empty():
            ips =self._queue.get()
            ips=ips
            result=[]
 
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(ips)
                #s.send("hello world\n")
                #back=s.recv(50)
                #if back:
                s.close
                print "%s:%d---------Open"%(ips[0],ips[1])
                result.append(b)

            except:
                print "%s:%s---------Fail\n"%(ips)
                pass 
    
              
#-------------help file-------------------
def main():
    usage = "usage: %prog [options] arg"  
    parser=OptionParser(usage)
    parser.add_option("-f","--infile",dest="filename",
                      help="please input start file")
    parser.add_option("-u","--outfile",dest="ip",
                      help="please input IP")  
    (options,args)=parser.parse_args()
    filename=options.filename
    ip=options.ip
    parser = OptionParser() 
    #---------thread--------
    threads=[]
    threads_count=10
    queue=Queue.Queue()  
    

    #------if input ip----------
    if ip:  
        ip=ip
        for i in port:
            ips=(ip,i)  
            queue.put(ips)
        for i  in range(threads_count):
            threads.append(DoRun(queue))
        
        for i in threads:
            i.start()
        for i  in threads:
            i.join()             
         
    #-------------input file----------
    if filename:
        ips=open(filename,'r')
        for ip in ips:
            ip=ip.strip('\n')
            for i in port:
                ips=(ip,i)  
                queue.put(ips)
        for i  in range(threads_count):
            threads.append(DoRun(queue))
        
        for i in threads:
            i.start()
        for i  in threads:
            i.join()                 

if __name__=='__main__':
    main()