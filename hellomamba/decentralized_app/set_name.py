from black_mamba.deploy import DeployContract


deployed = DeployContract()
contract = deployed.deployed_contract("HelloWorld")
greet = contract.functions.greet().call()
print(greet)

account = "0x0269AaeB4128435E763c3E3ACEE554a68CE95fA9"
nonce = deployed.w3.eth.getTransactionCount(account)
tx_param = {
    "from": account,
    "nonce": nonce
}
txn = contract.functions.setGreeting(b"Hello Satoshi").buildTransaction(tx_param)
# Don't hardcode the private key. This is just for demonstration purpose.
private_key = "2f702d87dabd62ce7c14543f01d24a5ed05a49c1ee80640866db7dbb50d91cf2"
signed_txn = deployed.w3.eth.account.signTransaction(txn, private_key=private_key)
tx_hash = deployed.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
tx_receipt = deployed.w3.eth.waitForTransactionReceipt(tx_hash)
print(tx_receipt)

greet = contract.functions.greet().call()
print(greet)
