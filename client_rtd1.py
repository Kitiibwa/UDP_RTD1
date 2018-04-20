import socket
import time

class UDP_Client:
    """
    UDP client send a binary file to a server at
    specified host and port in chunks of 1024 bytes at a time.
    
    UDP rtd1.0, we assume no bit error and no packet loss.
    """ 
    def __init__(self,host=socket.gethostname(),port=0,BUFFERSIZE=0):   #host gets localhost
        self.host = host
        self.port = port
        self.BUFFERSIZE =BUFFERSIZE
        
        self.port = 7130 #an arbitrary non-privileged port
        self.BUFFERSIZE = 1024   #set buffer size for data to be received
            
    def make_packets(self):
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as c:  # create a socket object and assign it variable c
            print('\nClient ready to send...\n')
            with open('cross_1.jpg', 'rb') as fobj: #open binary file for reading and assign it of object fobj
                while 1:
                    chunks = fobj.read(self.BUFFERSIZE) #read binary file in chunks of 1024 bytes    
                    if not chunks:  #if no more chunks of binary file to read
                        print('\nSending end transmission msg...')
                        c.sendto(b'end',(self.host, self.port)) # Sending message to end transmission.
                        time.sleep(2)   #sleep for 2 seconds before final message
                        print("File sent successfully.")
                        break   #break
                    c.sendto(chunks,(self.host, self.port)) #otherwise send binary file chunks to server
                    data, addr = c.recvfrom(self.BUFFERSIZE)    #receive message from server
                    print('{} to server {}'.format(data,addr))  #display received data and server addr          
        c.close() 
if __name__ == '__main__':
    client1=UDP_Client()    # make an instance of the UDP_Client class 
    client1.make_packets()  # call the make_packets() method
    