# band-assignment


# 1. Boss Baby's Revenge
time complexity is O(N) since we loop through input for 1 iteration
memory complexity is O(1) since it use only 1 variable (shot) to keep track of all progress

to run     
`python3 revenge.py`

# Superman's Chicken Rescue
time complexity is O(N) since we loop through input for 1 iteration
memory complexity is O(N) since it the roof can cover chicken at most N

to run     
`python3 superman.py`

# Transaction Broadcasting and Monitoring Client

1. **Create a virtual environment**

        ```python3 -m venv venv```

2. **Activate the virtual environment**

        ```source venv/bin/activate```

3. **Install the dependencies**

        ```pip install -r requirements.txt```

4. **Run the script**

        ```python3 client.main.py```


# diagram
![Alt text](https://raw.githubusercontent.com/patkamon/band-assignment/main/digram.drawio.png)

# features
- conduct payload
- validate input
- monitor transaction status (by loop)
- handle message for each status
- CLI (command line interface)
- cache, prevent to much request