from black_mamba.testlib import contract, eth_tester
import pytest
from eth_tester.exceptions import TransactionFailed


def test_initial_erc20(eth_tester):
    accounts = eth_tester.get_accounts()
    erc20_contract = contract("erc20", ["Dance", "JLO", 3, 1000])
    assert erc20_contract.functions.name().call() == "Dance"
    assert erc20_contract.functions.symbol().call() == "JLO"
    assert erc20_contract.functions.decimals().call() == 3
    assert erc20_contract.functions.totalSupply().call() == 1000000
    assert erc20_contract.functions.balanceOf(accounts[0]).call() == 1000000
