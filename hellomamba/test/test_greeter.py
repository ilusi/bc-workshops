from black_mamba.testlib import contract, eth_tester


def test_initial_greeting():
    hello_world_contract = contract("HelloWorld")
    assert hello_world_contract.functions.greet().call() == b"Hello World"

def test_initial_accounts(eth_tester):
    accounts = eth_tester.get_accounts()
    assert len(accounts) == 10
    assert eth_tester.get_balance(accounts[0]) == 1000000000000000000000000
