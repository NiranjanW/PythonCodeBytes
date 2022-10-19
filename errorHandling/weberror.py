from web3 import Web3
from time import sleep
from requests.exceptions import ConnectionError, ConnectTimeout, HTTPError
import sys

class NodeError(Exception):
    """Base exception for node errors"""
    def __init__(self, url, msg=None):
        if msg is None:
            msg = f"An error occurred with the node at {url}."
        super().__init__(msg)
        self.url = url

class NodeNotConnected(NodeError):
    """web3 could not connect to a node"""
    def __init__(self, url, w3=None):
        msg = f"A web3 connection could not be made to URL {url}."
        super().__init__(url, msg=msg)
        self.w3 = w3

class NodeConnectionError(NodeError):
    """A web3 error occurred communicating with a node"""
    def __init__(self, w3):
        msg = (
            f"A web3 connection error occurred talking to "
            f"{w3.provider.endpoint_uri}."
        )
        super().__init__(msg)
        self.w3 = w3

class NodeTooManyRequests(NodeError):
    def __init__(self, w3):
        msg = (
            f"Too many requests made to {w3.provider.endpoint_uri}.  Try a "
            f"different node."
        )
        super().__init__(msg)
        self.w3 = w3

class NodeNoAvailableNodes(NodeError):
    def __init__(self):
        msg = f"Unable to connect to any nodes."
        super().__init__(msg)

class NodeInternalError(NodeError):
    def __init__(self):
        msg = "The node had an internal error."
        super().__init__(msg)

def lib_connect_to_node(url):
    """Emulates library connect to node function"""
    try:
        w3 = Web3(
            Web3.HTTPProvider(
                url,
                request_kwargs={"timeout": 5}
            )
        )
        if not w3.isConnected():
            raise NodeNotConnected(url, w3)
    except Exception as e:
        raise NodeNotConnected(url) from e
    else:
        return w3

def connect_to_node(urls, node_retries):
    while node_retries >= 0:
        try:
            w3 = lib_connect_to_node(urls[0])
        except NodeNotConnected(urls[0]) as e:
            if node_retries == 0:
                raise NodeNoAvailableNodes from e
            node_retries -= 1
            urls = get_next_node(urls)
            print('Trying another node')
            sleep(1)
            continue
        else:
            return w3

def get_next_node(urls):
    urls.append(urls.pop(urls.index(urls[0])))
    return urls

def get_tx_count(w3, address):
    try:
        nonce = w3.eth.get_transaction_count(address)
    except (ConnectionError, ConnectTimeout) as e:
        print("A requests.exceptions.ConnectionError occurred.")
        raise NodeConnectionError(w3) from e
    except HTTPError as e:
        if e.code == 429:
            raise NodeTooManyRequests from e
    else:
        return nonce

def main():
    urls = [
        'https://matic-mainnet-full-rpc.bwarelabs.com:443',
        'https://matic-mainnet.chainstacklabs.com:443',
        'https://rpc-mainnet.maticvigil.com:443',
        'https://rpc-mainnet.matic.network:443'
    ]
    node_retries = 3
    address = '0xe18A0D121057B002BaFb90aD5F1AB951594A61E8'
    try:
        w3 = connect_to_node(urls, node_retries)
    except NodeNoAvailableNodes as e:
        print(e)
        sys.exit()

    while True:
        try:
            print(get_tx_count(w3, address))
            sleep(0.05)
        except NodeNotConnected(w3.provider.endpoint_uri, w3):
            urls = get_next_node(urls)
            try:
                w3 = connect_to_node(urls, node_retries)
            except NodeNoAvailableNodes as e:
                print(e)
                sys.exit()
        except NodeConnectionError(w3) as e:
            urls = get_next_node(urls)
            try:
                w3 = connect_to_node(urls, node_retries)
            except NodeNoAvailableNodes as e:
                print(e)
                sys.exit() 
        except NodeTooManyRequests(w3) as e:
            print('Too many requests')
            urls = get_next_node(urls)
            try:
                w3 = connect_to_node(urls, node_retries)
            except NodeNoAvailableNodes as e:
                print(e)
                sys.exit()

if __name__ == '__main__':
    main()