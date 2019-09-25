# from black_mamba.deploy import DeployContract


# deploy_contract_instance = DeployContract()
# parameters = []
# tx_params = { "from": "" }
# private_key = None

# deploy_contract_instance.deploy_contract("HelloWorld", parameters, tx_params, private_key)

# With Ganache
# from black_mamba.deploy import DeployContract
# from web3 import Web3


# deploy_contract_instance = DeployContract()
# parameters = []
# tx_params = { "from": None }
# private_key = None

# deploy_contract_instance.deploy_contract("HelloWorld", parameters, tx_params, private_key)

# Using Geth
from black_mamba.deploy import DeployContract

deploy_contract_instance = DeployContract()
parameters = []
tx_params = { "from": "0x0269AaeB4128435E763c3E3ACEE554a68CE95fA9" }
# Don't hardcode the private key. This is just for demonstration purpose.
private_key = "2f702d87dabd62ce7c14543f01d24a5ed05a49c1ee80640866db7dbb50d91cf2"

deploy_contract_instance.deploy_contract("HelloWorld", parameters, tx_params, private_key)
