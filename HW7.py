def lstCompare(list1, list2):
    x = len(list1)
    y = len(list2)
    if x <= y:
        list1.extend(list2)
        return list1
    if x > y:
        list1.insert(y, list2)
        return list1

lstCompare(["team", "mate", "referee"], ["fan", "desk", "pen", "wardrobe"])
#should return ['team', 'mate', 'referee', 'fan', 'desk', 'pen', 'wardrobe']
lstCompare(['orange', 'mango', 'pineapple'], ['pear', 'apple']) #should return
#['orange', 'mango', ['pear', 'apple'], 'pineapple']
lstCompare(['Tokyo', 'Lagos', 'Washington'], [ ]) #should return [[ ], 'Tokyo',
#'Lagos', 'Washington']
        
#--------------------------------------------------------------------------------

def itemType(things):
    value  = []
    for x in range(len(things)):
        char = len(things[x])
        if char % 2 == 1:
            value.append(x)
            value.append(things[x])
        else:
            value = value
    return value

itemType(["soccer", "baseball", "football", "cricket"])# should return [3, 'cricket']
itemType(["baiting", "venatio", "carting", "mushing"]) #should return [0, 'baiting', 1, 'venatio', 2, 'carting', 3, 'mushing']
itemType(["cirit", "dressage", "cutting", "eventing", "horseball"]) #should
#)return [0, 'cirit', 2, 'cutting', 4, 'horseball']
itemType(["ball", "kite", "tale"]) # should return [ ]

#------------------------------------------------------------------------------------

def oddUpper(string):
    odd_list = []
    even_list = []
    for idx in range(len(string)):
        if idx % 2 == 0:
            even_list.append(string[idx].capitalize())
        else:
            odd_list.append(string[idx].upper())
            
    return odd_list + even_list

oddUpper(["boxing", "judo", "javelin", "discus"])#should return
#['JUDO', 'DISCUS', 'Boxing', 'Javelin']
oddUpper(["hammer", "throw", "boomerang", "jump", "vault"])
#should return ['THROW', 'JUMP', 'Hammer', 'Boomerang', 'Vault']
oddUpper(["relay", "race", "hurdle", "pole"])
#should return ['RACE', 'POLE', 'Relay', 'Hurdle']

#--------------------------------------------------------------------------------

def charPick(word_list):
    ret_list = []
    for idx in range(len(word_list)):
        if idx % 2 == 0:
            cap = word_list[idx][0].upper()
            new_word = word_list[idx] + cap
            ret_list.append(new_word)
            
    return ret_list
        
charPick(["pop", "rock", "hiphop", "classical"]) #should return ['popP', 'hiphopH']
charPick(["rap", "jazz", "country", "electronics", "blues"]) #should return
#['rapR', 'countryC', 'bluesB']
charPick(["amapiano", "macarena", "electric", "slide", "moonwalk", "twist",
"chacha"]) #should return ['amapianoA', 'electricE', 'moonwalkM', 'chachaC']

#------------------------------------------------------------------------------------

def listRev(words):
    result = []
    for word in words:
        char_list = list(word)    
        char_list.reverse()      
        reversed_word = "".join(char_list)
        result.append(reversed_word)
    return result

listRev(["referee", "whistle", "player", "net"]) #should return
#['eerefer', 'eltsihw', 'reyalp', 'ten']
listRev(["eld", "light", "card", "pitch", "leather"]) #should return
#['dleif', 'thgil', 'drac', 'hctip', 'rehtael']
listRev(["orange", "mango"])# should return ['egnaro', 'ognam']




























