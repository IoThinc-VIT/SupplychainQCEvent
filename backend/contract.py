from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
import json



w3 = Web3(Web3.HTTPProvider(
    'https://eth-ropsten.alchemyapi.io/v2/FggN__A_hciRCWxGCS_E7lTY_jmIp2UX'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


abi = json.loads("""[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			}
		],
		"name": "AddProduct",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "wid",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "flag",
				"type": "bool"
			}
		],
		"name": "AddStatus",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "getProductStatus",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "location",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "data",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "w_id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "p_id",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "flag",
						"type": "bool"
					}
				],
				"internalType": "struct Supplychain.Status[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getProductsList",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "price",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "data",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Product[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getWorkerssList",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Worker[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "productStatus",
		"outputs": [
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "w_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "p_id",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "flag",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "product_Status",
		"outputs": [
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "w_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "p_id",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "flag",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "products",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "products_list",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "data",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"name": "setWorker",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "workers",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "workers_list",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]""")

key = 'c91e7c75c03c0d2814e00b23200a521197c036bb87537cb9bcd1356e410cb4b8'
account = w3.toChecksumAddress('0x20509aC8AcE7546fF5Aa8160Bc789D554FFc92CF')

address = w3.toChecksumAddress('0x294befe9cd6a95f5762526d7420d77022b999db4')
deployed_contract = w3.eth.contract(address=address, abi=abi)


def setWorker(name):
  transaction = deployed_contract.functions.setWorker(name).buildTransaction({'from': account})
  transaction.update({'nonce': w3.eth.get_transaction_count(account)})
  signed_tx = w3.eth.account.sign_transaction(transaction, key)
  txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
  print(txn_receipt)
  return "worker added"


def AddProduct(name, price, description, data):
  transaction = deployed_contract.functions.AddProduct(name, price, description, data).buildTransaction({'from': account})
  transaction.update({'nonce': w3.eth.get_transaction_count(account)})
  signed_tx = w3.eth.account.sign_transaction(transaction, key)
  txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
  print(txn_receipt)
  return "product added"


def AddStatus(location, data, wid, pid, flag):
  transaction = deployed_contract.functions.AddStatus(location, data, wid, pid, flag).buildTransaction({'from': account})
  transaction.update({'nonce': w3.eth.get_transaction_count(account)})
  signed_tx = w3.eth.account.sign_transaction(transaction, key)
  txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
  print(txn_receipt)
  return "status added"


def  getProductsList():
    
    return deployed_contract.functions.getProductsList().call()

def getWorkersList():
   return deployed_contract.functions.getWorkerssList().call()

def getProductStatus(pid):
   return deployed_contract.functions.getProductStatus(pid).call()


    
