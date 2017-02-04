import random
import re
from sounds import get_sounds

def read_datas(file):
    with open("data/" + file + ".in") as datas:
        data_list = [name.strip() for name in datas]
    return data_list

def random_choice(alist):
    return alist[random.randint(0, len(alist) - 1)]

def match(suffix, alist):
    matching = []
    for name in alist:
        if name.endswith(tuple(suffix)):
            matching.append(name)
    return matching

def find_matching(options, sounds, animals, adjectives):
    sound = sounds[random.choice(list(sounds.keys()))]
    #print(sound)

    if options.debug:
        print(sound)
    matching_animals = match(sound, animals)
    matching_adjectives = match(sound, adjectives)
    if matching_animals and matching_adjectives:
        return matching_animals, matching_adjectives
    else:
        return find_matching(options, sounds, animals, adjectives)

def generate_animals(options):
    f_animals = read_datas("female_animals")
    f_adjectives = read_datas("female_adjectives")
    m_animals = read_datas("male_animals")
    m_adjectives = read_datas("male_adjectives")

    sounds = get_sounds()

    i = 0
    while (i < options.n):
        female = bool(random.getrandbits(1))
        animals, adjectives = find_matching(options, sounds,
                f_animals if female else m_animals,
                f_adjectives if female else m_adjectives)

        if len(animals) < len(adjectives):
            for animal in animals:
                if (i < options.n):
                    print(random_choice(adjectives) + " " + animal)
                i += 1
        else:
            for adjective in adjectives:
                if (i < options.n):
                    print(adjective + " " + random_choice(animals))
                i += 1



def generate_expressions(options):
    verbs = read_datas("verbs")
    adverbial_phrases = read_datas("adverbial_phrases")
    coordinators = read_datas("coordinators")
    prepositions = read_datas("prepositions")
    m_names = read_datas("male_names")
    f_names = read_datas("female_names")

    i = 0
    while (i < options.n):
        x = random.randint(0, 3)
        if options.debug:
            print(x)
        if x == 0:
            print(random_choice(verbs) + " " + \
                            random_choice(m_names + f_names) + " " + \
                            random_choice(adverbial_phrases)
                    )
        elif x == 1:
            print(random_choice(verbs) + " " + \
                            random_choice(m_names + f_names) + " " + \
                            random_choice(prepositions) + " " + \
                            random_choice(m_names + f_names) + " "
                    )
        elif x == 2:
            print(random_choice(prepositions) + " " + \
                            random_choice(m_names + f_names) + " " + \
                            random_choice(prepositions) + " " + \
                            random_choice(m_names + f_names) + " " + \
                            random_choice(coordinators) + " " + \
                            random_choice(m_names + f_names)
                    )
        elif x == 3:
            print(random_choice(verbs) + " " + \
                            random_choice(prepositions) + " " + \
                            random_choice(m_names + f_names) + " " + \
                            random_choice(coordinators) + " " + \
                            random_choice(m_names + f_names) + " "
                    )
        i += 1
