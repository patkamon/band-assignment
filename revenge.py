# time complexity of O(N) since we loop through string one time.

def revenge(string):
    shot = 0
    # if shoot first or endup with no revenge that just return bad boy
    if string[0] == "R" or string[-1] == "S":
        return "Bad boy"

    for i in range(len(string)):
        # if found r then decease the shot count
        # not decease in case we revenge more than baby's shot 
        if string[i] == "R" and shot >0:
            shot -=1
        # if found s increase shot
        elif string[i] == "S":
            shot +=1

    # if there're shot left
    if shot >0:
        return  "Bad boy"
    return "Good boy"
        
# TEST
# print(revenge("SRSSRRR")) #Good boy
# print(revenge("RSSRR")) #Bad boy
# print(revenge("SSSRRRRS")) #Bad boy
# print(revenge("SRRSSR")) #Bad boy
# print(revenge("SSRSRRR")) #Good boy


baby = input()
print(revenge(baby))