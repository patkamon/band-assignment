import requests
import time

# transaction client class
class TransactionClient:
    def __init__(self, server_url):
        self.server_url = server_url # server url
        self.history = [] # keep tx history in here
        self.memory = {} # cache

    # broadcast transaction
    def broadcast_transaction(self, transaction_data):
        response = requests.post(f"{self.server_url}/broadcast", json=transaction_data)
        if response.status_code == 200:
            self.history.append(response.json()["tx_hash"])
            return response.json()["tx_hash"]
        else:
            raise Exception(f"Failed to broadcast transaction: {response.text}")

    # check transaction status
    def __check_status(self, tx_hash):
        # memory cache
        if self.memory.get(tx_hash) != None:
            return self.memory.get(tx_hash)

        response = requests.get(f"{self.server_url}/check/{tx_hash}")
        if response.status_code == 200:
            return response.json()["tx_status"]
        else:
            raise Exception(f"Failed to check status: {response.text}")

    # monitor transaction
    def monitor_transaction(self, tx_hash, interval=5):
        while True:
            status = self.__check_status(tx_hash)
            print(f"Transaction {tx_hash} status: {status}")
            if status != "PENDING":
                if status == "CONFIRMED":
                    print("Transaction finalized.")
                elif status == "DNE": # not exist 
                    print("Transaction not found!")
                elif status == "FAILED": # failed
                    print("Transaction failed!")
                    print("Please wait for a moment and try again!")
                # store in cache
                self.memory["tx_hash"] = status
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

