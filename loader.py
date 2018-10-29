import pandas as pd
import os

class Loader:
	def __init__(self, csv=False, chunksize=10000, separator=','):

		# check csv path
		assert csv != False and os.path.isfile(csv)

		self.csv = csv
		self.chunksize = chunksize
		self.separator = separator

	# get line with columns
	def get_columns(self, nline=0):
		with open(self.csv, 'r') as f:
			for i, line in enumerate(f):
				if i == nline:
					return line.rstrip('\n').split(self.separator)

	# get all parsed content
	def iterate(self, usecols=[]):

		# get all data from all columns
		if len(usecols) == 0:
			iterator = pd.read_csv(self.csv, chunksize=self.chunksize, sep=self.separator, iterator=True)

		# take precise columns
		else:
			iterator = pd.read_csv(self.csv, chunksize=self.chunksize, sep=self.separator, iterator=True, usecols=usecols)

		return iterator