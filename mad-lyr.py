import random

nounlist = []
verblist = []
adjectivelist = []

def initialize():
    nounfile = open("resources\\nouns.txt", "r")
    for noun in nounfile:
        nounlist.append(noun.rstrip())

    verbfile = open("resources\\verbs.txt", "r")
    for verb in verbfile:
        verblist.append(verb.rstrip())
    
    adjectivefile = open("resources\\adjectives.txt", "r")
    for adjective in adjectivefile:
        adjectivelist.append(adjective.rstrip())
    return

def get_noun():
    return random.choice(nounlist)

def get_verb():
    return random.choice(verblist)

def get_adj():
    return random.choice(adjectivelist)

def replace_all_nouns(line):
    old_line = None
    new_line = line

    while(old_line is not new_line):
        old_line = new_line
        new_line = old_line.replace("<noun>", get_noun(), 1)
    return new_line

def replace_all_verbs(line):
    old_line = None
    new_line = line

    while(old_line is not new_line):
        old_line = new_line
        new_line = old_line.replace("<verb>", get_verb(), 1)
    return new_line
    
def replace_all_adj(line):
    old_line = None
    new_line = line

    while(old_line is not new_line):
        old_line = new_line
        new_line = old_line.replace("<adjective>", get_adj(), 1)
    return new_line


if __name__ == "__main__":
    # Main Method
    print("Hi pal")

    initialize()

    random_noun = get_noun()
    print("you're such a " + random_noun)
   
    random_verb = get_verb()
    print("I really want to " + random_verb)

    random_adj = get_adj()
    print("I feel " + random_adj)

    input = open("input.txt", "r")
    for line in input: 
        line = line.rstrip()
        line = replace_all_nouns(line) 
        line = replace_all_verbs(line)
        line = replace_all_adj(line)
        print(line)
  
