

def oneCharacter(dictionary):
    variations = []

    for i in dictionary:
        variations.append(i)
    return variations
        
        
def twoCharacters(dictionary):
    old = oneCharacter(dictionary)
    variations = []
    for k in dictionary:
        for i in dictionary:
            combo = str(k+i)
            variations.append(combo)
    return variations+old


def threeCharacters(dictionary):
    old = twoCharacters(dictionary)
    variations = []
    for k in dictionary:
        for l in dictionary:
            for i in dictionary:
                combo = str(k+l+i)
                variations.append(combo)
    return variations+old


def threeCharactersZ(dictionary):           ## COMPARE ORDER OF L K I 
    old = twoCharacters(dictionary)
    variations = []
    for k in dictionary:
        for l in dictionary:
            for i in dictionary:
                combo = str(l+k+i)
                variations.append(combo)
    return variations+old



def fourCharacters(dictionary):
    old = threeCharacters(dictionary)
    variations = []
    for k in dictionary:
        for d in dictionary:
            for l in dictionary:
                for i in dictionary:
                    combo = str(k+d+l+i)
                    variations.append(combo)
    return variations+old


def fourCharactersSOLO(dictionary):
    variations = []
    for k in dictionary:
        for d in dictionary:
            for l in dictionary:
                for i in dictionary:
                    combo = str(i+l+d+k)
                    variations.append(combo)
    return variations



def fiveCharacters(dictionary):
    old = fourCharacters(dictionary)
    variations = []
    for k in dictionary:
        for z in dictionary:
            for d in dictionary:
                for l in dictionary:
                    for i in dictionary:
                        combo = str(k+z+d+l+i)
                        variations.append(combo)
    return variations+old


def sixCharacters(dictionary):
    old = fiveCharacters(dictionary)
    variations = []
    for k in dictionary:
        for z in dictionary:
            for d in dictionary:
                for l in dictionary:
                    for i in dictionary:
                        for y in dictionary:
                            combo = str(k+z+d+l+i+y)
                            variations.append(combo)
    return variations+old


def sevenCharacters(dictionary):
    old = fiveCharacters(dictionary)
    variations = []
    for k in dictionary:
        for z in dictionary:
            for d in dictionary:
                for l in dictionary:
                    for y in dictionary:
                        for i in dictionary:
                            for r in dictionary:
                                combo = str(k+z+d+l+y+i+r)
                                variations.append(combo)
    return variations+old


def eightCharacters(dictionary):
    old = sevenCharacters(dictionary)
    variations = []
    for k in dictionary:
        for z in dictionary:
            for d in dictionary:
                for l in dictionary:
                    for y in dictionary:
                        for i in dictionary:
                            for r in dictionary:
                                for b in dictionary:
                                    combo = str(k+z+d+l+y+i+r+b)
                                    variations.append(combo)
    return variations+old


def nineCharacters(dictionary):
    old = eightCharacters(dictionary)
    variations = []
    for k in dictionary:
        for z in dictionary:
            for d in dictionary:
                for l in dictionary:
                    for y in dictionary:
                        for i in dictionary:
                            for r in dictionary:
                                for b in dictionary:
                                    for s in dictionary:
                                        combo = str(k+z+d+l+y+i+r+b+s)
                                        variations.append(combo)

    return variations+old

def tenCharacters(dictionary):
    old = nineCharacters(dictionary)
    variations = []
    for k in dictionary:
        for z in dictionary:
            for d in dictionary:
                for l in dictionary:
                    for y in dictionary:
                        for i in dictionary:
                            for r in dictionary:
                                for b in dictionary:
                                    for m in dictionary:
                                        for s in dictionary:
                                            combo = str(k+z+d+l+y+i+r+b+m+s)
                                            variations.append(combo)
    return variations+old




def elevenCharacters(dictionary):
    old = tenCharacters(dictionary)
    variations = []
    for k in dictionary:
        for z in dictionary:
            for d in dictionary:
                for l in dictionary:
                    for y in dictionary:
                        for i in dictionary:
                            for r in dictionary:
                                for b in dictionary:
                                    for s in dictionary:
                                        for d in dictionary:
                                            for q in dictionary:
                                                combo = str(k+z+d+l+y+i+r+b+s+d+q)
                                                variations.append(combo)
    return variations+old