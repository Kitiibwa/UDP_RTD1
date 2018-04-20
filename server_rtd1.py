import socket # import socket module
import os

class UDP_Server:
    """
    UDP server receives binary file from client in chunks at
    specified host and port, responds with a message.
    
    UDP rtd1.0, we assume no bit error and no packet loss.
    """
    def __init__(self,host=socket.gethostname(),port=0,BUFFERSIZE=0):   #host gets localhost
        self.host = host
        self.port = port
        self.BUFFERSIZE =BUFFERSIZE
        
        self.port = 7130    # an arbitrary non-privileged port
        self.BUFFERSIZE = 1024   #set buffer size for data to be received
    
    def recv_and_send(self):
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:  # create a socket object and assign it to variable s
            s.bind((self.host,self.port))   # bind the socket to the (host,port) tuple
            print('Server waiting for file chunks...\n') 
            cross_2 = 'cross_2.jpg' #destination file
            if os.path.exists(cross_2): #if destination file exists,
                os.remove(cross_2)  #delete it, otherwise if the program is run a few time, the same file will be appended
            with open(cross_2,'ab') as fobj:  #open a binary file to append and assign it to object fobj
                while 1: 
                    chunks, addr = s.recvfrom(self.BUFFERSIZE)  #receive chunks and client's address
                    if chunks == b'end':    #if server receives end bytes,
                        print('\nServer done receiving whole file.\n')  
                        break   #break
                    print('Chunk of {} bytes received from {}'.format(len(chunks), addr))    #print size of file chunk  as it is received from client
                    s_response = "Chunk of {} bytes sent".format(len(chunks))   #message to be sent to client
                    s.sendto(s_response.encode('utf-8'),addr)    #encoding the message to be sent
                    fobj.write(chunks)  #Write reassembles chunks in order    
        s.close()
if __name__ == '__main__':
    server1=UDP_Server() # make instance of UDP_Server class
    server1.recv_and_send() # call the sending() method