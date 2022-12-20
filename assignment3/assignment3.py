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
    See Page 3 Function 3 of th .pdf.
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
    profile_tuple = ()
    for key in profile_dictionary:
        if key==user_id:
            profile_tuple = profile_dictionary[key]
    
    #temp contains all top posts of each follower 
    temp = []
    if len(profile_tuple[2])==0:
        return [""]
    for i in range(0,len(profile_tuple[2])):
        temp2=()
        for key2 in chirp_dictionary:
            temp3 = chirp_dictionary[key2]
            if temp3[0]==profile_tuple[2][i] and (len(temp2)==0):
                temp2 = temp3
            if temp3[0]==profile_tuple[2][i] and (len(temp2)!=0):
                if len(temp3[3])>len(temp2[3]):
                    temp2=temp3
        if len(temp2)!=0:
            temp.append(temp2)
            
    if temp == []:
        return [""]
    
    high = 0
    data = []
    for x in range(0,len(temp)):
        temp4 = temp[x]
        if high == 0:
            high = len(temp4[3])
            data.append(temp4[1])
        if high!=0 and (len(temp4[3])>high):
            high = len(temp4[3])
            data.append(temp4[1])
    return data

    
def create_tag_dictionary( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> Dict[str, Dict[int, List[str]]]:
    """
    Creates a dictionary that keys tags to tweets that contain them.

    Note, some spacing has been added for human readability.
    
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> create_tag_dictionary(chirp_dictionary)
    {'SnowMan': {
        400: ['Does not want to build a %SnowMan %StopAsking', 'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'StopAsking': {
        400: ['Does not want to build a %SnowMan %StopAsking']}, 
    '': {
        200: ['Make the ocean great again.']}, 
    'OhNoes': {
        500: ["Help I'm being held captive by a beast!  %OhNoes"]}, 
    'StockholmeSyndrome': {
        500: ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"], 
        400: ['LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'ShowYouTheWorld': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}, 
    'JustSayNo': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}}
    """
    #Your code goes here
    tag_dict = {}
    for chirp in chirp_dictionary: #100000, 100001, 100002, 100003, 100004, 100005
        for tag in chirp_dictionary[chirp][2]: #tag = all tag messages
            if tag not in tag_dict:
                temp = dict()
                temp[chirp_dictionary[chirp][0]]=[chirp_dictionary[chirp][1]]
                tag_dict[tag]=temp
            else:
                if chirp_dictionary[chirp][0] not in tag_dict[tag]:
                    temp = tag_dict[tag]
                    temp[chirp_dictionary[chirp][0]]=[chirp_dictionary[chirp][1]]
                    tag_dict[tag]=temp
                else:
                    tag_dict[tag][chirp_dictionary[chirp][0]].append(chirp_dictionary[chirp][1])
    return tag_dict
  

def get_tagged_chirps( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]], \
        tag: str) \
        -> List[str]:
    """
    Returns a list of chirps containing specified tag.
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> get_tagged_chirps(chirp_dictionary, "SnowMan")
    ['Does not want to build a %SnowMan %StopAsking', 
    'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']
    """
    #Your code goes here
    tagged_list = []
    tags_dict=create_tag_dictionary(chirp_dictionary)
    for key in tags_dict:
        if key==tag:
            temp = tags_dict[key]
            
            for key2 in temp:
                if len(temp[key2])==1:
                    tagged_list.append(temp[key2][0])
                else:
                    for i in range(0,len(temp[key2])):
                        tagged_list.append(temp[key2][i])
            return tagged_list
    return tagged_list
    



    
