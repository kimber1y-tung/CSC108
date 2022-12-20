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


def create_chirp_dictionary(file_name: str) \
        -> Dict[int, Tuple[int, str, List[str], List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    chirp dictionary as defined on Page 2 Functions 2.

    Note, some spacing has been added for human readability.
    
    >>> create_chirp_dictionary("chirps.txt")
    {100000: (
        400, 
        'Does not want to build a %SnowMan %StopAsking',
        ['SnowMan', 'StopAsking'], 
        [100, 200, 300], 
        [400, 500]), 
    100001: (
        200, 
        'Make the ocean great again.', 
        [''], 
        [], 
        [400]), 
    100002: (
        500, 
        "Help I'm being held captive by a beast!  %OhNoes", 
        ['OhNoes'], 
        [400], 
        [100, 200, 300]), 
    100003: (
        500, 
        "Actually nm. This isn't so bad lolz :P %StockholmeSyndrome", 
        ['StockholmeSyndrome'], 
        [400, 100], 
        []), 
    100004: (
        300, 
        'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
        ['ShowYouTheWorld', 'JustSayNo'], 
        [500, 200], 
        [400]), 
    100005: (
        400, 
        'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan', 
        ['StockholmeSyndrome', 'SnowMan'], 
        [], 
        [200, 300, 100, 500])}
    """
    #Your code goes here
    f = open(file_name, "r")
    H = dict()

    #Helper for tag
    def tag_helper(x):
        y = []
        if x == '\n':
            return []
        else:
            x = x.split(', ')
            for i in x:
                y.append(str(i))
            return y
    
    #Helper for liked and disliked
    def helper(a):
        b = []
        if a == '\n':
            return []
        else:
            a = a.strip('\n').split(',')
            for numbers in a:
                b.append(int(numbers))
            return b
        
    
    line = f.readline()

    while line:
        chirpid = int(line) #10000
        userid = int(f.readline()) #400
        message = f.readline().strip('\n') #Does not want to build a %SnowMan %StopAsking
        tags = f.readline().strip('\n') #SnowMan, StopAsking
        likeds = f.readline() #100, 200, 300
        dislikeds = f.readline() #400, 500
        sperate = f.readline() #sperates to the next userid (\n)
        line = f.readline()

        tag = tag_helper(tags)
        liked = helper(likeds)
        disliked = helper(dislikeds)
        H[chirpid] = (userid, message, tag, liked, disliked)
    return H

def get_top_chirps( \
        profile_dictionary: Dict[int, Tuple[str, List[int], List[int]]], \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        user_id: int)\
        -> List[str]:
    """
    Returns a list of the most liked chirp for every user user_id follows.
    See Page 3 Function 3 of the .pdf.
    >>> profile_dictionary = create_profile_dictionary("profiles.txt")
    >>> chirp_dictionary   = create_chirp_dictionary("chirps.txt")
    >>> get_top_chirps(profile_dictionary, chirp_dictionary, 300)
    ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"]
    >>> get_top_chirps( profile_dictionary, chirp_dictionary, 500 )
    ['Make the ocean great again.', 
    'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
    'Does not want to build a %SnowMan %StopAsking']
    """
    
    #Your code goes here
    
    #helper: puts profile_dictionary into a list
    def helper1(x):
        y = []
        for i in x: #puts into a list
            y.append(i)
        return y

    userlist = helper1(profile_dictionary[user_id]) #['Jasmine', [500], [500, 100]]
    num_of_followed = len(userlist[2])

    #helper2: returns the dictionary of {userid_post: num_of_likes, message}
    def helper2(s):
        a = list(s.values())
        H = {}
        num_of_likes = 0
        for j in range(len(a)):
            userid_post = a[j][0]
            if len(a[j][3]) > num_of_likes:
                num_of_likes = len(a[j][3])
                message = a[j][1]
            else:
                message = a[j][1]
            H[userid_post] = (num_of_likes, message )
        return H
    
    new_dict = helper2(chirp_dictionary)
    return new_dict
    if num_of_followed == 0:
        return ['']

    elif num_of_followed == 1: #Ex: 200, Ariel only follows 500
        #find 500s highest liked post
        return

    else:
        return 



        
        
    """
    chirp_list = list(chirp_dictionary.items())
    num_of_likes = len(chirp_list[0][1][3]) #write loop to change 0, add 1

    for j in range(len(chirp_list)):
        
    

    """




    
    

    

    

    

    

    













