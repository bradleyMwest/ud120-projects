#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
	"""
		Clean away the 10% of points that have the largest
		residual errors (difference between the prediction
		and the actual net worth).

		Return a list of tuples named cleaned_data where 
		each tuple is of the form (age, net_worth, error).
	"""

	cleaned_data = []

	### your code goes here
	residuals = (predictions-net_worths)**2
	pts2rmv = int(len(predictions)*0.9)
	cleaned_data = sorted(zip(ages,net_worths, residuals),key=lambda err: err[2])[:pts2rmv]
	
	
	return cleaned_data

