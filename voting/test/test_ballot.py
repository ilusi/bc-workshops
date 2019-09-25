from black_mamba.testlib import contract, eth_tester
import pytest
from eth_tester.exceptions import TransactionFailed


def test_initial_ballot(eth_tester):
    accounts = eth_tester.get_accounts()
    ballot_contract = contract("ballot", [[b"bitcoin", b"ethereum"]])
    assert ballot_contract.functions.int128Proposals().call() == 2
    assert ballot_contract.functions.chairperson().call() == accounts[0]
    assert ballot_contract.functions.voterCount().call() == 0
    assert ballot_contract.functions.proposals__name(0).call()[:7] == b"bitcoin"
    assert ballot_contract.functions.proposals__name(1).call()[:8] == b"ethereum"
    assert ballot_contract.functions.proposals__voteCount(0).call() == 0
    assert ballot_contract.functions.proposals__voteCount(1).call() == 0

def test_giveRightToVote(eth_tester):
    accounts = eth_tester.get_accounts()
    ballot_contract = contract("ballot", [[b"bitcoin", b"ethereum"]])
    assert ballot_contract.functions.voterCount().call() == 0
    assert ballot_contract.functions.voters__weight(accounts[1]).call() == 0
    tx = { "from": accounts[0] }
    ballot_contract.functions.giveRightToVote(accounts[1]).transact(tx)
    assert ballot_contract.functions.voterCount().call() == 1
    assert ballot_contract.functions.voters__weight(accounts[1]).call() == 1
    ballot_contract.functions.giveRightToVote(accounts[2]).transact(tx)
    assert ballot_contract.functions.voterCount().call() == 2
    assert ballot_contract.functions.voters__weight(accounts[2]).call() == 1

def test_giveRightToVote_fails(eth_tester):
    accounts = eth_tester.get_accounts()
    ballot_contract = contract("ballot", [[b"bitcoin", b"ethereum"]])
    tx = { "from": accounts[1] }
    with pytest.raises(TransactionFailed):
        ballot_contract.functions.giveRightToVote(accounts[1]).transact(tx)

def test_vote(eth_tester):
    accounts = eth_tester.get_accounts()
    ballot_contract = contract("ballot", [[b"bitcoin", b"ethereum"]])
    tx = { "from": accounts[0] }
    ballot_contract.functions.giveRightToVote(accounts[1]).transact(tx)
    ballot_contract.functions.giveRightToVote(accounts[2]).transact(tx)
    voter1_tx = { "from": accounts[1] }
    ballot_contract.functions.vote(0).transact(voter1_tx)
    voter2_tx = { "from": accounts[2] }
    ballot_contract.functions.vote(0).transact(voter2_tx)
    assert ballot_contract.functions.proposals__voteCount(0).call() == 2
    assert ballot_contract.functions.proposals__voteCount(1).call() == 0
    assert ballot_contract.functions.winnerName().call()[:7] == b"bitcoin"
