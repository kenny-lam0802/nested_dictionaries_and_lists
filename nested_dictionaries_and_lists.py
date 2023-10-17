#********Update Values in Dictionaries and Lists*********
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1) Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3]],[[15,8,9]]
x[1][0]= 15
print(x)

#2) Change the last_name of the first student from "Jordan" to "Bryant"
students[0]["last_name"]= "Bryant"
print(students[0])

#3) In the sports_dictionary, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])

#4) Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#**********Iterate through a list of dictionaires*********
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(a_list):
    for i in range(len(a_list)): #iterate through the list
        for key, value in a_list[i].items(): #iterate through the dictionary
            print(f"{key} - {value},")
    
iterateDictionary(students)

#*********3) Get values from List of dictionaries********
def iterateDictionary2(key_name, list):
    for item in range(len(list)):
        print(list[item][key_name])

iterateDictionary2("first_name", students)

#*********4)Iterate through a dictionary with List Values*********
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        for i in (some_dict[key]):
            print(i)

printInfo(dojo)



