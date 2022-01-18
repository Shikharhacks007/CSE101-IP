# Assignment - 2
# Name - Shikhar Sharma
# Roll No - 2020121

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="demo_data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''

	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	integers = []
	for rec in records:
		if rec["first_name"].lower() == str(first_name).lower():
			integers.append(int(rec["id"]))
	return integers


def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	integers = []
	for rec in records:
		if rec["last_name"].lower() == str(last_name).lower():
			integers.append(rec["id"])
	return integers


def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	integers = []
	full_name = full_name.split()
	for rec in records:
		if (rec["last_name"].lower() == str(full_name[1]).lower()) and (rec["first_name"].lower() == str(full_name[0]).lower()):
			integers.append(rec["id"])
	return integers


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''

	integers = []
	for rec in records:
		if min_age <= rec["age"] <= max_age:
			integers.append(rec["id"])
	return integers


def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''

	gender = {"male":0, "female":0}
	for rec in records:
		if rec["gender"] == "male":
			gender["male"] += 1

		elif rec["gender"] == "female":
			gender["female"] += 1
		else:
			continue

	return gender


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''

	names = []
	if address == {}:
		return records
	else:
		for rec in records:
			flag = 0
			for i in address.keys():
				if str(rec["address"][i]).lower() != str(address[i]).lower():
					flag = 1

			if flag == 0:
				names.append({"first_name": rec["first_name"], "last_name": rec["last_name"]})
	return names


def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''

	alum = []
	temp = {"first_name": "", "last_name": "", "percentage": 0}
	for rec in records:
		for rec1 in rec["education"]:
			if (rec1["institute"] == institute_name) and (rec1["ongoing"] == False):
				temp["first_name"] = rec["first_name"]
				temp["last_name"] = rec["last_name"]
				temp["percentage"] = rec1["percentage"]
				alum.append(temp)
			temp = {"first_name": "", "last_name": "", "percentage": 0}

	# print(alum)
	return alum


def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''

	topper = {}
	temp = {}
	for rec in records:
		for rec1 in rec["education"]:
			if not rec1["ongoing"]:
				temp[rec1["institute"]] = 0
				topper[rec1["institute"]] = 0

	for rec in records:
		for rec1 in rec["education"]:
			if (rec1["ongoing"] == False) and (temp[rec1["institute"]] < rec1["percentage"]):
				temp[rec1["institute"]] = float(rec1["percentage"])
				topper[rec1["institute"]] = int(rec["id"])

	return topper


def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''

	group = ""
	for rec in records:
		if rec["id"] == receiver_person_id:
			group = rec["blood_group"]

	donors = {}
	blood = {'A': ['A', 'O'], 'B': ['B', 'O'], 'AB': ['AB', 'A', 'B', 'O'], 'O': ['O']}
	temp = blood[group]

	for rec in records:
		if (rec["blood_group"] in temp) and (rec["id"] != receiver_person_id):
			donors[rec["id"]] = rec["contacts"]

	return donors


def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''

	temp = []
	for i in list_of_ids:
		for rec in records:
			if rec["id"] == i:
				temp.extend(rec["friend_ids"])

	temp1 = set()
	# print(temp)
	for i in temp:
		if temp.count(i) == len(list_of_ids):
			temp1.add(i)
	# print(temp1)
	c_f = []
	c_f.extend(temp1)
	# print(c_f)
	# 5 4 2 1 1
	return c_f


def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	if person_id_1 == person_id_2:
		return False
	else:
		return True


def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	if person_id != "":
		for rec in records:
			if rec["id"] == person_id:
				records.pop(records.index(rec))

		for rec in records:
			if person_id in rec["friend_ids"]:
				rec["friend_ids"].remove(person_id)

		return records

	else:
		return records


def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	if person_id != friend_id:
		if (0 <= person_id < len(records)) and (0 <= friend_id < len(records)):
			for rec in records:
				if rec["id"] == person_id and (friend_id not in rec["friend_ids"]):
					rec["friend_ids"].append(friend_id)
				elif rec["id"] == friend_id and (person_id not in rec["friend_ids"]):
					rec["friend_ids"].append(person_id)

		return records


def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	if person_id != friend_id:
		# print("hi1")
		for rec in records:
			if rec["id"] == person_id:
				# print("hi2")
				for rec1 in records:
					if rec1["id"] == friend_id:
						# print("hi3")
						if (person_id in rec1["friend_ids"]) and (friend_id in rec["friend_ids"]):
							# print("hi4")
							rec1["friend_ids"].remove(person_id)
							rec["friend_ids"].remove(friend_id)
							# print(rec)
							# print(rec1)
							return records

		return records

	else:
		# print("lol3")
		return records


def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''

	temp = {}
	for rec in records:
		if rec["id"] == person_id:
			temp["institute"] = institute_name
			if ongoing:
				temp["ongoing"] = ongoing
			else:
				temp["ongoing"] = ongoing
				temp["percentage"] = percentage

			rec["education"].append(temp)
			# print(temp)
			# print(rec)
			return records


'''
#records = read_data_from_file()
# name_f = input()
# filter_by_first_name(records, name_f)

# name_l = input()
# filter_by_last_name(records, name_l)

# f_name = input()
# filter_by_full_name(records, f_name)

# start = int(input())
# end = int(input())
# filter_by_age_range(records, start, end)

# count_by_gender(records)

# addr = {}
# house = input().strip()
# block = input().strip()
# town = input().strip()
# city = input().strip()
# state = input().strip()
# pincode = input().strip()
# if house != "":
# 	addr["house_no"] = house
# if block != "":
	# 	addr["block"] = block
# if town != "":
# 	addr["town"] = town
# if city != "":
# 	addr["city"] = city
# if state != "":
# 	addr["state"] = state
# if pincode != "":
# 	addr["pincode"] = pincode
#
# print(addr)
# print(filter_by_address(records, addr)) # need solve


# inst_name = input()
# find_alumni(records, inst_name)

# print(find_topper_of_each_institute(records))

# receive = int(input())
# find_blood_donors(records, receive)

# a = list(map(int, input().split()))
# print(get_common_friends(records, a)) # need to check this

# d = input()
# if d!= "" and d.isdigit() == True:
# 	print(delete_by_id(records, int(d)))
# else:
# 	print("done")

# e = int(input())
# f = int(input())
# print(add_friend(records, e, f))

# e = int(input())
# f = int(input())
# print(remove_friend(records, e, f))

# id = int(input())
# institute = input()
# ongoing = input()
# percentage = float(input())
# print(add_education(records, id, institute, ongoing, percentage )) # need solve
'''