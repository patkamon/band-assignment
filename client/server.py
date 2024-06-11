import requests
import time

# transaction client class
class TransactionClient:
    def __init__(self, server_url):
        self.server_url = server_url # server url
        self.history = [] # keep tx history in here

    # broadcast transaction
    def broadcast_transaction(self, transaction_data):
        response = requests.post(f"{self.server_url}/broadcast", json=transaction_data)
        if response.status_code == 200:
            self.history.append(response.json()["tx_hash"])
            return response.json()["tx_hash"]
        else:
            raise Exception(f"Failed to broadcast transaction: {response.text}")

    # check transaction status
    def check_status(self, tx_hash):
        response = requests.get(f"{self.server_url}/check/{tx_hash}")
        if response.status_code == 200:
            return response.json()["tx_status"]
        else:
            raise Exception(f"Failed to check status: {response.text}")

    # monitor transaction
    def monitor_transaction(self, transaction_id, interval=5):
        while True:
            status = self.check_status(transaction_id)
            print(f"Transaction {transaction_id} status: {status}")
            if status != "PENDING":
                if status == "CONFIRMED":
                    print("Transaction finalized.")
                elif status == "DNE": # not exist 
                    print("Transaction not found!")
                elif status == "FAILED": # failed
                    print("Transaction failed!")
                    print("Please wait for a moment and try again!")
                break
            time.sleep(interval)

    # list history transaction
    def show_history_list(self):
        for i in range(len(self.history)):
            # latest
            if i == len(self.history)-1:
                print(f"{i+1}. {self.history[i]} ", "Latest!")
            else:
                print(f"{i+1}. {self.history[i]} ")

    def conduct_payload(self, symbol, price):
        return {
            "symbol": symbol,
            "price": price,
            "timestamp": int(time.time())  
        }

