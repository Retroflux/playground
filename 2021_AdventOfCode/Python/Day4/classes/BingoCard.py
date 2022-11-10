class BingoCard(object):
	"""docstring for BingoCard object"""
	def __init__(self,BingoCardValues, BingoCardNumber):
		self.BingoCardValues = BingoCardValues 
		self.BingoCardNumber = BingoCardNumber

		@property
		def BingoCardValue(self):
			return self.BingoCardValue

		@property
		def BingoCardNumber(self):
			return self.BingoCardNumber

		@BingoCardNumber.setter
		def BingoCardNumber(self, BingoCardNumber):
			self.BingoCardNumber = BingoCardNumber

		