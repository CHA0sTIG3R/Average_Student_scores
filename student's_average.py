# Student's Average scores

school_class = {}

while True:
    # input name as the key
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    # input score as the name's values
    score = int(input("Enter the student's score (0-10): "))
    
    # check if the key already exist in the dictionary
    if name in school_class:
        # add the score to the name as tuples
        school_class[name] += (score,)
    else:
        # else create a new key : values in the dictionary
        school_class[name] = (score,)

# iterate through the dictionary with the keys        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    # iterate through the tuple
    for score in school_class[name]:
        # add the values in the tuple
        adding += score
        counter += 1
    # print the name and their respective average
    print(name, ":", adding / counter)
