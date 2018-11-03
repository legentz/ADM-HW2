import pandas as pd
import os

COMMA = ','
TAB = '\t'
SPACE = ' '

class Loader:
	def __init__(self, csv=None, nrows=None, chunksize=10000, separator=COMMA):

		# check csv path
		assert os.path.isfile(csv)

		self.csv = csv
		self.chunksize = chunksize
		self.separator = separator
		self.nrows = nrows
		self.to_merge = None
		self.to_merge_direction = None
		self.to_merge_on = None

	# get line with columns
	def get_columns(self, nline=0):
		with open(self.csv, 'r') as f:
			for i, line in enumerate(f):
				if i == nline:
					return line.rstrip('\n').split(self.separator)

	# this could not be iterated
	def merge(self, csv=None, on=None, direction='left', usecols=[], separator=COMMA, drop_on_columns=False):

		# check csv path
		assert os.path.isfile(csv)
		assert type(on) == tuple and len(on) > 0

		if len(usecols) > 0:
			self.to_merge = pd.read_csv(csv, usecols=usecols, sep=separator)
		else:
			self.to_merge = pd.read_csv(csv)

		self.to_merge_direction = direction
		self.to_merge_on = on
		self.drop_on_columns = drop_on_columns

	# get all parsed content
	def iterate(self, usecols=[], parse_dates=False, date_index=None):

		# get all data from all columns
		if len(usecols) == 0:
			iterator = pd.read_csv(self.csv, nrows=self.nrows, chunksize=self.chunksize, sep=self.separator, iterator=True, parse_dates=parse_dates)

		# take precise columns
		else:
			iterator = pd.read_csv(self.csv, nrows=self.nrows, chunksize=self.chunksize, sep=self.separator, iterator=True, parse_dates=parse_dates, usecols=usecols)

		# create a generator
		for df in iterator:

			# if something has to be merged
			if self.to_merge is not None:
				df = pd.merge(df, self.to_merge, how=self.to_merge_direction, left_on=self.to_merge_on[0], right_on=self.to_merge_on[1])

				# remove columns that we're used to join
				if self.drop_on_columns:
					df = df.drop(columns=list(self.to_merge_on))

			# check date_index
			assert date_index in parse_dates and type(date_index) == str

			# dates have to be indexed to be manipulated
			if parse_dates:
				df = df.set_index(date_index)

			yield df