from web3 import Web3
import time


RPC_URL = 'https://testnet.dplabs-internal.com'
PRIVATE_KEY = 'YOUR_PKEY_HERE'
CONTRACT_ADDRESS = '0x0000000038f050528452D6Da1E7AACFA7B3Ec0a8'
MINT_METHOD_ID = '0x5b70ea9f'


web3 = Web3(Web3.HTTPProvider(RPC_URL))
sender_address = web3.eth.account.from_key(PRIVATE_KEY).address


while True:
    try:
        nonce = web3.eth.get_transaction_count(sender_address)
        tx = {
            'from': sender_address,
            'nonce': nonce,
            'to': CONTRACT_ADDRESS,
            'data': MINT_METHOD_ID,
            'gas': 300000,
            'gasPrice': web3.to_wei('2', 'gwei'),
            'chainId': 688688

        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"hash: https://testnet.pharosscan.xyz/tx/{web3.to_hex(tx_hash)}")

    except Exception as e:
        print(f"Error saat mint: {e}")

    print("Menunggu 7 detik...")
    time.sleep(7)
