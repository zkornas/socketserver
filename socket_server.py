import socket
import random
import threading

quotes = [
    #Princess Bride Quotes:
    "Inconceivable! - Vizzini",
    "I always think that everything could be a trap, which is why I am still alive. - Prince Humperdinck",
    "As you wish. - Westley",
    "There is a shortage of perfect breasts in the world. It would be a pity to damage yours. - Westley",
    "Good night, Westley. Good work. Sleep well. I will most likely kill you in the morning. - Dread Pirate Roberts",
    "This is true love. Do you think this happens every day? - Westley",
    "Boo! - The Ancient Booer",
    #Clueless Quotes
    "Ugh, as if! - Cher",
    "She could be a farmer in those clothes. - Amber",
    "Suddenly a dark cloud settled over first period... I got a C in debate? - Cher",
    "That was way harsh, Tai. - Cher",
    "I was just totally clueless. - Cher",
    "Oh my God, I am totally buggin. - Cher"
    "Whatever. - Amber"
]

host = "" 
port = 17

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcp_socket.bind((host, port))
udp_socket.bind((host, port))

tcp_socket.listen()

print(f"Listening for connections on {host}:{port}...")

def handle_tcp_client():

    while True:
        tcp_client, tcp_addr = tcp_socket.accept()

        print(f"Received TCP connection from {tcp_addr}")

        quote = random.choice(quotes)
        tcp_client.sendall(quote.encode())

        tcp_client.close()


def handle_udp_request():

    while True:
        udp_client, udp_addr = udp_socket.recvfrom(1024)  
        print(f"Received UDP request from {udp_addr}")

        quote = random.choice(quotes)
        udp_socket.sendto(quote.encode(), udp_addr)  

udp_thread = threading.Thread(target=handle_udp_request)
udp_thread.daemon = True
udp_thread.start()

tcp_thread = threading.Thread(target=handle_tcp_client)
tcp_thread.daemon = True
tcp_thread.start()


input("Press ENTER to exit...")