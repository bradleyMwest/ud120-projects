#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

people = enron_data.keys()

#the number of people in this dataset
print 'Number of people in Enron Dataset: ', len(people)

#features available per person
feat = enron_data[people[0]].keys()
print 'Number of Features Per Person: ', len(feat)

#Number of people identified as interest
num_pois = 0
for i in people:
	if enron_data[i]['poi'] == 1:
		num_pois+=1
print 'The number of people of interest in this set is: ', num_pois

# people of interest identified:
file = open('../final_project/poi_names.txt','r')
pois = []
for l in file.readlines()[2:]:
	pois.append(l.strip())
file.close()
print 'The number of people of interest is: ', len(pois)

# What is the total value of the stock belonging to James Prentice
#print feat
#print people
print 'The total stock value belonging to James Prentice is: ', enron_data['PRENTICE JAMES']['total_stock_value'], '$'

#
print 'Number of emails form Wesley Colwell to poi :',enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#
print 'The value of stock options exercised by Jeffrey K Skilling is:',enron_data['SKILLING JEFFREY K']['exercised_stock_options'], '$'

# Who took home the most money? 
# for i in people:
	# print i
names = ['LAY KENNETH L', 'SKILLING JEFFREY K', 'FASTOW ANDREW S']
for i in names:
	print i,'took home ', enron_data[i]['total_payments'], '$'

# What does an undefined feature look like
#answer NaN

#How many people have a quantified salary?
#How many people have an email address listed?
sal = 0
add = 0
tot_pay = 0
poi_no_sal = 10
for i in people:
	if enron_data[i]['salary'] != 'NaN':
		sal+=1
	if enron_data[i]['email_address'] != 'NaN':
		add+=1
	if enron_data[i]['total_payments'] == 'NaN':
		tot_pay += 1
	if enron_data[i]['total_payments'] == 'NaN' and enron_data[i]['poi'] == True:
		poi_no_sal += 1
print 'The total number of salaries is:', sal
print 'The total number of known emails is:',add
print 'The total number of unknwon total_payemetnts is:',tot_pay, 'which is ', round((tot_pay/float(len(people)))*100,2), '% of the dataset'
print 'The total POIs with no total_payemetnts is:',poi_no_sal, 'which is ', round((poi_no_sal/float(len(people)))*100,2), '% of the dataset'

# how many pois have salaries listed:
for i in pois:
	a = i.split(' ')
	if a[0] == '(y)':
		name = a[1][0:-1] + ' ' + a[2]
		name = name.upper()
		for j,k in enumerate(people):
			if k.startswith(name) == True:
				print enron_data[people[j]]['email_address']
				
