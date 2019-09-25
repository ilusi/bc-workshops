let Web3 = require("web3");
let net = require("net");

let web3 = new Web3("/usr/local/MyProjects/Blockchain/workshop-level-up/hellomamba/datadir/geth.ipc", net);

web3.eth.getAccounts().then(function(accounts) {
  console.log("Accounts: ");
  console.log(accounts);
});

let account1 = "0x0269AaeB4128435E763c3E3ACEE554a68CE95fA9";
web3.eth.getBalance(account1).then(function(balance) {
  console.log(`Balance ${account1}`);
  console.log(balance);
});

web3.eth.getBlock("latest").then(function(block) {
  console.log("Latest block:");
  console.log(block);
});

web3.eth.getTransactionFromBlock("latest", 0).then(function(tx) {
  console.log("First transaction in latest block:");
  console.log(tx);
});

let account2 = "0xAe2e5211b23F306a06Bd19778079fD89cbaAFE34";
let account3 = "0x53A70642e649d616cBA669d7BdF5937edB7fBD4B";

web3.eth.getBalance(account2).then(function(balance) {
  console.log(`Balance ${account2} before sending ethers`);
  console.log(balance);
});
web3.eth.getBalance(account3).then(function(balance) {
  console.log(`Balance ${account3} before receiving ethers`);
  console.log(balance);
});

web3.eth.getTransactionCount(account2).then(function(nonce) {
  let rawTx = {
    from: account2,
    to: account3,
    chainId: 15,
    value: web3.utils.toWei("2", "ether"),
    nonce: nonce,
    gasPrice: web3.utils.toWei("200", "gwei"),
    gas: 300000,
  };
  let account2PrivateKey = "0x644ab73946362e2a0bb4219bc77166cca0e3022b5f6b880f93a384355027fb57";

  web3.eth.accounts.signTransaction(rawTx, account2PrivateKey).then(function(signed) {
    web3.eth.sendSignedTransaction(signed.rawTransaction)
        .on("receipt", function(receipt) {
          console.log("inside sendTransaction receipt");
          console.log(receipt);
          console.log("Balance ${account2} after sending ethers");
          web3.eth.getBalance(account2).then(console.log);
          console.log("Balance ${account3} after receiving ethers");
          web3.eth.getBalance(account3).then(console.log);
        })
        .on("error", console.error);
  });
});
