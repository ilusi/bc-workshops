from black_mamba.deploy import DeployContract


deploy_contract_instance = DeployContract()
parameters = ["Dance", "JLO", 3, 1000]
tx_params = { "from": "" }
private_key = None

deploy_contract_instance.deploy_contract("erc20", parameters, tx_params, private_key)
