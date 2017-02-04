import random
import re
from sounds import find_matching

def read_datas(file):
    with open("data/" + file + ".in") as datas:
        data_list = [name.strip() for name in datas]
    return data_list

def random_choice(alist):
    return alist[random.randint(0, len(alist) - 1)]

def randomize_shortest_based(lista, listb, i, n):
    results = []
    if len(lista) < len(listb):
        for a in lista:
            if (i < n):
                results.append(' '.join([random_choice(listb) + ",", a]))
            i += 1
    else:
        for b in listb:
            if (i < n):
                results.append(' '.join([b + ",", random_choice(lista)]))
            i += 1
    return results, i

def upperfirst(s):
    return s[0].upper() + s[1:]

def generate_animals(options):
    f_animals = read_datas("female_animals")
    f_adjectives = read_datas("female_adjectives")
    m_animals = read_datas("male_animals")
    m_adjectives = read_datas("male_adjectives")

    i = 0
    while (i < options.n):
        female = bool(random.getrandbits(1))
        animals, adjectives = find_matching(options,
                f_animals if female else m_animals,
                f_adjectives if female else m_adjectives)

        results, i = randomize_shortest_based(animals, adjectives, i, options.n)
        for result in results:
            print(upperfirst(result + "."))

def generate_sentence(*words):
    if len(words) == 1 and type(words[0]) is list:
        # Allow multiple arguments or a list in one argument
        words = words[0]
    return upperfirst(' '.join(words) + ".")

def generate_random_sentence(*lists):
    chosen = []
    for alist in lists:
        chosen.append(random_choice(alist))
    return generate_sentence(chosen)

class grammar_details:
    def __init__(self, female=bool(random.getrandbits(1)),
            plural=bool(random.getrandbits(1))):
        self.female = (female == 1)
        self.plural = (plural == 1)

def match_gender(female, female_thing, male_thing):
    return female_thing if female else male_thing

def match_grammar(g_details, female_singular, male_singular,
        female_plural, male_plural):
    if g_details.plural:
        return match_gender(g_details.female, female_plural, male_plural)
    else:
        return match_gender(g_details.female, female_singular, male_singular)

def match_adjective(gd, f_adjectives, m_adjectives):
    adj = random_choice(match_gender(gd.female, f_adjectives,
        m_adjectives))
    if gd.plural:
        if not adj.endswith("x"):
            adj = adj + "s"
    return adj


def generate_expressions(options):
    verbs = read_datas("verbs")
    adverbial_phrases = read_datas("adverbial_phrases")
    coordinators = read_datas("coordinators")
    prepositions = read_datas("prepositions")

    m_s_names = read_datas("male_singular_names")
    f_s_names = read_datas("female_singular_names")
    m_p_names = read_datas("male_plural_names")
    f_p_names = read_datas("female_plural_names")

    f_adjectives = read_datas("female_adjectives")
    m_adjectives = read_datas("male_adjectives")

    names = m_s_names + m_p_names + f_s_names + f_p_names

    i = 0
    while (i < options.n):
        x = random.randint(0, 3)
        if options.debug:
            print(x)

        if x == 0:
            print(generate_random_sentence(verbs, names, adverbial_phrases))
        elif x == 1:
            print(generate_random_sentence(verbs, names, prepositions, names))
        elif x == 2:
            gd = grammar_details()

            print(generate_random_sentence(
                prepositions, names, prepositions, names, coordinators,
                match_grammar(gd, f_s_names, m_s_names, f_p_names, m_p_names),
                ["sont"] if gd.plural else ["est"],
                [match_adjective(gd, f_adjectives, m_adjectives)]
                ))

        elif x == 3:
            print(generate_random_sentence(verbs, prepositions, names))
        i += 1
