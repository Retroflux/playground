class Bit(object):
	"""docstring for Bit object"""
	def __init__(self, bitColumn,count = 0):
		self.bitColumn = bitColumn
		self.count = count

		@property
		def bitColumn(self):
			return self.bitColumn
		@property
		def count(self):
			return self.count

		@bitColumn.setter
		def bitColumn(self, bitColumn):
			self.bitColumn = bitColumn
		@count.setter
		def count(self, count):
			self.count = count

