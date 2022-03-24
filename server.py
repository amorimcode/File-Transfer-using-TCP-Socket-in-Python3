
import socket
import numpy as np

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        """ Receiving the filename from the client. """
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the client. """
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))

        """ Closing the file. """
        file.close()

        file_aluno = open(filename)
        file_gabarito = open('gabarito.txt')

        answers_aluno = []
        for line in file_aluno.readlines():
            line = line.split('-')[1]
            answer=[]
            for letter in line.split(';'):
                answer.append(letter)
            if '' in answer:
                answer.remove('')
            if '\n' in answer:
                answer.remove('\n')
            answers_aluno.append(answer)

        answers_gabarito = []
        for line in file_gabarito.readlines():
            line = line.split('-')[1]
            answer=[]
            for letter in line.split(';'):
                answer.append(letter)
            if '' in answer:
                answer.remove('')
            if '\n' in answer:
                answer.remove('\n')
            answers_gabarito.append(answer)

        print(answers_aluno, answers_gabarito)

        """ Closing the connection from the client. """
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")

if __name__ == "__main__":
    main()
