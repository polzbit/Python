import socket

PORT = XXXXX # enter host port
HOSTNAME = 'x.x.x.x' # enter host ip address

def netcat(text_to_send):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( HOSTNAME, PORT ))
    s.sendall(text_to_send)
    s.shutdown(socket.SHUT_WR)

    rec_data = []
    while 1:
        data = s.recv(1024)
        if not data:
            break
        rec_data.append(data)
    print rec_data
    if '\n' in rec_data[1]:
        mess=str(parse_rpn(rec_data[1].replace("\n","")))
    else:
        mess = rec_data
    s.send(mess)
       
    s.close()
    return mess

message =''
if __name__ == '__main__':
    while 1:
        text_to_send = message
        text_recved = netcat(text_to_send)
        message = text_recved
        print message
    


