import random
import re
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--number", type="int", dest="n",
        help="print n number of french expressions", metavar="NUMBER")
(options, args) = parser.parse_args()

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

def find_matching(sounds, animals, adjectives):
    sound = sounds[random.choice(list(sounds.keys()))]
    #print(sound)

    matching_animals = match(sound, animals)
    matching_adjectives = match(sound, adjectives)
    if matching_animals and matching_adjectives:
        return matching_animals, matching_adjectives
    else:
        return find_matching(sounds, animals, adjectives)


def generate():
    f_animals = read_datas("female_animals")
    f_adjectives = read_datas("female_adjectives")
    m_animals = read_datas("male_animals")
    m_adjectives = read_datas("male_adjectives")

    sounds = get_sounds()

    i = 0
    while (i < options.n):
        animals, adjectives = find_matching(sounds, f_animals, f_adjectives)
        for animal in animals:
            if (i < options.n):
                print(random_choice(adjectives) + " " + animal)
            i += 1


