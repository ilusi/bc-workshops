let Web3 = require("web3")

let web3 = new Web3("http://localhost:7545")
web3.eth.getAccounts().then(console.log)

web3.eth.getBalance("0x700EF5B254A8A0325a3AE24D543F459308071853").then(console.log)

web3.eth.getBlock("latest").then(function(block) {
    console.log(block)
})

web3.eth.getTransactionFromBlock("latest", 0).then(console.log)

let tx = {
    from: "0x734Ce75a4065821E340939E932348b377f8d3627",
    to: "0xBc78FcA65fd55e6D34058665Dc36448D59C9BD35",
    value: web3.utils.toWei("2", "ether")
}

web3.eth.sendTransaction(tx)
    .on("transactionHash", function(hash) {
        console.log("inside sendTransaction transactionHash")
        console.log(hash)
    })
    .on("receipt", function(receipt) {
        console.log("inside sendTransaction receipt")
        console.log(receipt)
    })
    .on("error", console.error)
