import hashlib
from datetime import datetime

from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
KEY = "YOUR_PRIVATE_KEY"

provider = Web3(
    Web3.HTTPProvider(RPC)
)

wallet = Account.from_key(KEY)

labels = [
    "coverage",
    "oracles",
    "API matched",
]

transaction = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 120500,
    "gasPrice": provider.to_wei(
        4,
        "gwei"
    ),
    "nonce": provider.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(
    transaction
)

signature = signed.raw_transaction.hex()

digest = hash
