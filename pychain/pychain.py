import hashlib, json
from time import time
from tqdm import tqdm as progress_bar
from typing import Optional
from uuid import uuid4

class Pychain(object):

	def __init__(self) -> None:
		self.ledger = []
		self.current_transactions = []

		# initialise Blockchain
		self.add_block(previous_hash=1, proof_from_PoW=100)

	def add_transaction(self, sender: str, recipient: str, amount: int) -> int:
		# append transaction details as a dict to the ledger
		self.current_transactions.append({
			"from": sender,
			"to": recipient,
			"amount" : amount
			})

		return self.final_block["index"] + 1

	def add_block(self, proof_from_PoW: int, previous_hash: Optional[str] = None) -> dict:
		# 
		block = {
		"transactions" : self.current_transactions,
		"proof" : proof_from_PoW,
		"index" : len(self.chain) + 1,
		"timestamp" : time(),
		"previous_hash" : self.hash(self.final_block()) or previous_hash
		}

		# reset current transactions
		self.current_transactions = []

		self.ledger.append(block)
		return block

	@staticmethod
	def hash(block: dict) -> str:
		# make SHA256 hash
		to_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(to_string).hexdigest()

	@property
	def final_block(self) -> int:
		return self.ledger[-1]

	def pow(self, previous_proof: int) -> int:
		# proof of work function
		proof = 0
		while self.proof_validation(previous_proof, proof):
			proof += 1

		return proof

	@staticmethod
	def proof_validation(previous_proof: int, proof: int) -> bool:
		# validates proof: checks if hash matches with leading number of zeroes
		return hashlib.sha256(f"{previous_proof}{proof}".encode()).hexdigest()[:4] == "0000"

	
