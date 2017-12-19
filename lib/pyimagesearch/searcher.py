# import the necessary packages
import numpy as np
import json

class Searcher:
	def __init__(self, trainPath):
		# store our index path
		self.trainPath = trainPath

	def search(self, queryFeatures, limit = 31):
		# initialize our dictionary of results
		results = {}

		data = json.load(open(self.trainPath,'r'))

		features = []
		for x in data:
			for row in data[x]:
				features.append(row['region_1'])
				features.append(row['region_2'])
				features.append(row['region_3'])
				features.append(row['region_4'])
				d = self.chi2_distance(features,queryFeatures)
				results[x] = d
				features = []

		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])

		# return our (limited) results
		return results[:limit]

	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		# return the chi-squared distance
		return d