import socket
import random
import time

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    for _ in range(10):
        from_acc = random.randint(0, 4)
        to_acc = random.randint(0, 4)
        amount = random.randint(10, 200)

        message = f"TRANSFER FROM ACCOUNT: {from_acc} TO ACCOUNT: {to_acc} AMOUT: {amount}"
        client.send(message.encode())

        response = client.recv(1024).decode()
        print(f"{message} -> {response}")

        time.sleep(0.5)

    client.send("BALANCES".encode())
    balances = client.recv(1024).decode()
    print("Final balances:", balances)
