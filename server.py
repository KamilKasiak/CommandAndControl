import socket

HOST = "0.0.0.0"
PORT = 443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST, PORT)
    s.listen()

    #loop for accepting the connection
    while(True):
        print("Listening...")
        conn, addr = s.accept()
        #when connection is accepted
        with conn:
            print(f"Connected by {addr}")
            cmd = input("Enter cmd: ")
            cmd = cmd + '\n'
            
            # encode cmd to byte array and send it to the client
            cmdRequest = cmd.encode()
            conn.sendall(cmdRequest)

            # receive output from a client
            cmdOutput = conn.recv(1024)
            print(cmdOutput)
