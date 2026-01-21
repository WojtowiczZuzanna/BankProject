import socket
import threading
from bank import Bank, Account

HOST = "127.0.0.1"
PORT = 5000

bank = Bank()

for i in range(5):
    bank.add_account(Account(i, 1000))

def handle_client(conn, addr):
    print(f"Connected: {addr}")
    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            parts = data.split()
            if parts[0] == "TRANSFER":
                _, from_id, to_id, amount = parts
                success = bank.transfer(int(from_id), int(to_id), int(amount))
                response = "OK" if success else "FAILED"
                conn.send(response.encode())

            elif parts[0] == "BALANCES":
                balances = bank.get_balances()
                conn.send(str(balances).encode())

    print(f"Disconnected: {addr}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Bank server started...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
