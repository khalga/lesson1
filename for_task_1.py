school_list = [
    {'school_class': '1a' , 
    'scores' : [3, 4, 5, 2, 4, 4, 5]},

    {'school_class': '1b' , 
    'scores' : [3, 4, 5, 2, 2, 2, 5, 8]},

    {'school_class': '3c' , 
    'scores' : [5, 4, 5, 3, 4, 2, 5, 5, 2]}

]

for i in school_list:
    j = sum(i['scores'])/len(i['scores'])
    print(i['school_class'] + ': ' + round(str(j, 2))