def connect(client,base_info):
    try:
        client.connect(('127.0.0.1', int(base_info["num_port"])))
        return True
    except ConnectionRefusedError:
        print("Could not connect to the server. Server may not be running or address/port is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")

def disconnect(client):
    client.close()
    return True