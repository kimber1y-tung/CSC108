from typing import List, Dict, Tuple

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
    
    
    
    
    
    
    
    
    
    
    
    
    
