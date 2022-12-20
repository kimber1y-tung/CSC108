from typing import List, Dict, Tuple

def create_profile_dictionary(file_name: str) \
        -> Dict[int, Tuple[str, List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    profile dictionary as defined on Page 2 Functions 1.

    Note, some spacing has been added for human readability.
    
    >>> create_profile_dictionary("profiles.txt")
    {100: ('Mulan', [300, 500], [200, 400]), 
    200: ('Ariel', [100, 500], [500]), 
    300: ('Jasmine', [500], [500, 100]), 
    400: ('Elsa', [100, 500], []), 
    500: ('Belle', [200, 300], [100, 200, 300, 400])}
    """
    #Helper
    def helper(x):
        y = []
        if x == '\n':
            return []
        else:
            x = x.strip('\n').split(',')
            for numbers in x:
                y.append(int(numbers))
            return y
        
    #Your code goes here
    f = open(file_name, "r")
    H = dict()

    line = f.readline()

    while line:
        userid = int(line) #100
        username = f.readline().strip('\n') #Mulan
        followerss = f.readline() #300,500
        followeds = f.readline() #200,400
        sperate = f.readline() #sperates to the next userid (\n)
        line = f.readline()

        followers = helper(followerss)
        followed = helper(followeds)
        H[userid] = (username, followers, followed)
        
    return H
    
