from server import TransactionClient 
import os

# func for clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


client = TransactionClient("https://mock-node-wgqbnxruha-as.a.run.app")


while True:
    # Command line interface (CLI)
    print("+++++++++++++++++++++++")
    print("TRANSACTION BROADCAST")
    print("======================")
    print()

    print("Chose your option")
    print("1. Broadcast")
    print("2. Monitor transaction status")
    print("3. Searching transaction")
    print("4. Quit")
    print("======================")

   
    option = input("Fill number (1-4): ")  # take input
    # validate input
    try:
        option = int(option) 
    except Exception as e:
        print(f"Error: {e}")

    # option 1 conduct payload and broadcast    
    if option == 1: 
        # conduct payload
        symbol = input("Fill in symbol (ETH): ")
        price = input("Fill in price (integer): ")
        # validate
        try: 
            price = int(price)
        except Exception as e:
            print(f"Error: {e}")
        transaction_data = client.conduct_payload(symbol, price)
        print("payload: ", transaction_data)
        try:
            # broadcast transaction
            tx_hash = client.broadcast_transaction(transaction_data)
            print(f"Transaction broadcasted with ID: {tx_hash}")
            back = input("Type anything to back to main menu: ")
        except Exception as e:
            print(f"Error: {e}")

    # option 2 chosing transaction in history to monitor
    elif option == 2: 
        print("Chose transaction")
        print("======================")
        client.show_history_list()
        print("======================")
        # chosing tx in history
        chosing = input("Fill number of transaction (1, 2 etc.): ")
        # validate chosing
        try:
            tx = client.history[int(chosing)-1]
            print("Choosing transaction: ", tx)
        except Exception as e:
            print(f"Error: {e}")
        print("Monitor until transaction finalized")
        # monitor transaction
        client.monitor_transaction(tx_hash)
        back = input("Type anything to back to main menu: ")

    # option 3 fill in tx hash to monitor
    elif option == 3: 
        print("Searching transaction")
        print("======================")
        # fill in txhash
        tx_hash = input("Fill transaction hash (tx hash): ")
        print("Monitor until transaction finalized")
        # monitor transaction
        client.monitor_transaction(tx_hash)
        back = input("Type anything to back to main menu: ")

    # quit 
    else:
        break
    cls()
