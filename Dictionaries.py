Dictionaries


cmp(dict1, dict2) - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
len() - give the total length of the dictionary.
str() - produces a string representation of a dictionary.
type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dictionary type.

.clear() - removes all elements from the dictionary
.copy() - returns a shallow copy dictionary
.fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
.get(key, default=None) - For key key, returns value or default if key is not in dictionary.
.has_key(key) - returns true if a given key is available in the dictionary, otherwise it returns false.
.items() - returns a list of dictionary's (key, value) tuple pairs
.keys() - return a list of dictionary keys.
.setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
.update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
.values() - returns list of dictionary values.

##########################################################################################################################################

for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"


Question # 1 :  Why is there a light in the fridge and not in the freezer?
----
Question # 2 :  Why don't sheep shrink when it rains?
----
Question # 3 :  Why are they called apartments when they are all stuck together?
----
Question # 4 :  Why do cars drive on the parkway and park on the driveway?
----


##########################################################################################################################################




data ={"house":"Haus","cat":"Katze","red":"rot"}
print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
#['house', 'red', 'cat']
print data.values()
#['Haus', 'rot', 'Katze']



##########################################################################################################################################



country_specialities = zip(countries, dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]


country_specialities_dict = dict(country_specialities)
print country_specialities_dict
#Result is...
#{'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}


countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]

##########################################################################################################################################

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names(x):
	count=0
	counts=0
	# for key, values in users['Students']:
	print "STUDENTS"
	for values in users['Students']:
		
		count+=1
		print  str(count), values["first_name"], values['last_name'], + len(values["first_name"]+values["last_name"])
		

	print "INSTRUCTORS"
	for values in users['Instructors']:
		counts +=1
		print counts, values["first_name"], values['last_name'], + len(values["first_name"]+values["last_name"])
	# 	for students in range(1,len('Students')):
	# 		print .get('first_name', "")

names(users)

