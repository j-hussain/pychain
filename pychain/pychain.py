import hashlib, json
from time import time
from tqdm import tqdm as progress_bar
from typing import Optional

class Pychain(object):

	def __init__(self) -> None:
		self.ledger = []
		self.current_transactions = []

		# initialise Blockchain
		self.add_block(previous_hash=1, proof_from_PoW=100)

	def add_transaction(self, sender: str, recipient: str, amount: int) -> int:
		self.current_transactions.append({
			"from": sender,
			"to": recipient,
			"amount" : amount
			})

		return self.final_block["index"] + 1

	def add_block(self, proof_from_PoW: int, previous_hash: Optional[str] = None) -> dict:
		block = {
		"transactions" : self.current_transactions,
		"proof" : proof_from_PoW,
		"index" : len(self.chain) + 1,
		"timestamp" : time(),
		"previous_hash" : self.hash(self.ledger[-1]) or previous_hash
		}

		# reset current transactions
		self.current_transactions = []

		self.ledger.append(block)
		return block

	@staticmethod
	def hash(block):
		pass

	@property
	def final_block(self):
		pass
	
	
