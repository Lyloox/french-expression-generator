import random

sounds = {
        # 1-syll sounds sounds
        "a": ["a", "at", "ât", "as"],
        "eu": ["eux", "eut", "eue", "eu"],
        "é": ["é", "ée", "ger", "nier", "tier", "lier", "vier"],
        "è": ["è", "ès", "ai", "aie", "et", "ais", "ait", "ey", "ay"],
        "i": ["i", "ie", "bis", "ris", "cis", "rit", "til", "ï", "tit", "by"],
        "o": ["o", "au", "aux", "aud", "aut", "gros", "ot"],
        "u": ["ru", "gu", "nu", "du", "lu", "bu", "lue", "tue", "due", "nue",
            "rue", "us"],
        "ou": ["ou", "oux", "oue", "oup", "out"],

        "oi": ["oie", "oigt", "oua", "oit", "oa", "oid", "ois"],
        "en": ["ant", "an", "anc", "eng", "ent", "amps"],
        "in": ["in", "un", "en", "ein", "aim", "ain", "ien"],
        "on": ["on", "om", "ong", "ond"],

        # 2-syll sounds
        "al": ["al", "alle", "ale", "âl", "âle", "âlle"],
        "aj": ["age", "aje", "aj", "âge"],
        "ag": ["ague"],
        "as": ["as", "asse", "ace", "âce", "âsse"],
        "ar": ["ar", "arre", "are", "âre", "ard"],
        "av": ["av", "ave", "âve"],
        "ash": ["ash", "ach", "ashe", "ache", "âche", "aches"],
        "at": ["ate", "âte"],
        "ad": ["ade", "ad"],
        "ay": ["aille", "aye", "aïe", "ail"],
        "ak": ["aque", "ack"],
        "ane": ["anne", "ane", "âne"],
        "ab": ["abe"],
        "af": ["aphe", "afe"],
        "am": ["ame", "âme"],
        "az": ["aze"],

        "el": ["el", "elle", "èle", "aile"],
        "èt": ["ète", "aite", "ette", "ête"],
        "ez": ["aise", "èse", "èze"],
        "èr": ["aire", "ère", "ere", "erre", "ert", "erf", "mer", "fier",
            "hamster", "ver"],
        "èn": ["aine", "ène", "enne", "eine", "êne", "aigne", "aines"],
        "èy": ["eille", "eil"],
        "ed": ["aide", "ède", "eide"],
        "èv": ["ève", "eve", "aive"],
        "èk": ["eque", "ec"],
        "èsh": ["aiche", "aîche", "èche", "êche", "eiche", "eche"],
        "èj": ["ège", "ege", "eige", "eiges"],
        "èm": ["emme", "ème", "ême"],
        "èp": ["eppe", "eppes"],

        "euv": ["euve"],
"euz": ["euse", "euses", "euz", "euze"],
        "eur": ["eur", "eure", "eurre"],
        "euy": ["euil"],
        "eum": ["sum"],
        "eun": ["eune"],

        "ans": ["anse", "ense", "ance", "ence"],
        "ant": ["ante", "ente"],
        "and": ["ande"],
        "amp": ["ampe"],

        "ik": ["ique", "ic"],
        "il": ["ile", "tranquille", "ril", "Nil", "ill", "tile", "vile",
                "vil"],
        "iy": ["tille", "nille", "guille", "rille"],
        "ine": ["pine", "tine", "quine", "yne", "inne", "fine", "dine",
                "ouine", "mine", "ligne", "nigne"],
        "ins": ["ins", "ince"],
        "id": ["id", "ide", "ides"],
        "iv": ["iv", "ive", "ïve"],
        "ite": ["ite", "ites"],
        "is": ["isse", "ice"],
        "if": ["if", "iphe", "ïf"],
        "im": ["ime", "imme", "îme"],
        "ib": ["ibe", "ïbe", "ïbes"],
        "ish": ["ish"],
        "ir": ["pire", "tire", "cire"],
        "iz": ["cise", "rise"],
        "ix": ["yx"],

        "os": ["céros", "osse", "ausse"],
        "oz": ["ose", "oz"],
        "ob": ["ob", "obe"],
        "ok": ["oque", "oq", "ock"],
        "or": ["or", "orc", "ore"],
        "om": ["ome", "ôme"],
        "ol": ["ole", "nol", "ôle"],
        "of": ["of", "ophe"],
        "op": ["ope", "aupe"],
        "ot": ["otte", "otl"],
        "od": ["ode"],
        "aud": ["aude"], # different from "od" in parisian french...
        "og": ["ogue"],

        "oul": ["ool", "oule", "oul"],
        "ouz": ["ouse", "ouz", "ouses"],
        "our": ["our", "oure", "ourd"],
        "ous": ["ouce", "ous", "ousse"],
        "ouv": ["ouve"],
        "ouk": ["ouc"],
        "ouy": ["ouille"],
        "oush": ["ouche"],
        "ouj": ["ouge"],
        "out": ["oûte", "oute"],

        "oit": ["oite"],
        "oir": ["oir", "oire"],
        "oiz": ["oise"],
        "oide": ["oide"],

        "ond": ["onde"],
        "onne": ["onne", "one", "aune"],
        "onj": ["onge"],

        "ut": ["ute", "uth"],
        "ur": ["ur", "ure", "ûre"],
        "ul": ["cule", "ul", "dule", ],
        "ush": ["uche"],
        "us": ["usse"],
        "uz": ["duse", "buse", "fuse"],
        "uk": ["duc"],

        "ind": ["inde"],
        "inx": ["ynx"],
        "inj": ["inge"],

        # 3-syll sounds
        "able": ["able"],
        "alm": ["alm", "alme"],
        "ansh": ["ansh", "anch", "anshe", "anche"],
        "arj": ["arge", "arje"],
        "ard": ["arde"],
        "ast": ["aste", "ast"],
        "akt": ["acte", "act"],
        "atr": ["atre", "âtre", "âtres"],
        "ask": ["asque"],
        "arp": ["arpe"],

        "egr": ["ègre", "aigre"],
        "esk": ["esque"],
        "ern": ["erne", "èrne", "airne"],
        "erl": ["erle"],
        "est": ["este"],
        "erb": ["erbe"],
        "ebr": ["èbre"],
        "evr": ["èvre"],

        "euvr": ["euvre"],

        "ist": ["ist", "iste", "ïste", "ïst"],
        "ibl": ["ible"],
        "ibr": ["ibre"],
        "idr": ["idre", "ydre"],
        "ikt": ["ict", "icte"],
        "igr": ["tigre"],
        "itsh": ["itsch"],

        "imbl":["umble", "imble"],

        "opr": ["opre"],
        "ourb": ["ourb", "ourbe"],
        "ourd": ["ourde"],
        "onbr": ["ombre", "onbre"],
        "orm": ["orme", "orm"],
        "ompt": ["ompte", "ompt"],
        "obl": ["oble"],
        "orf": ["orf", "orphe"],
        "olt": ["olt", "olte"],
        "okr": ["ocre"],
        "ork": ["orque"],
        "orj": ["orge"],

        "ust": ["ust", "uste"],
        "upt": ["upt", "upte"],
        "ult": ["ult", "ulte"],

        # 4-syll sounds
        "andr": ["andre"],

        "estr": ["estre"],
        "euvr": ["euvre"],

        "oulp": ["oulpe"],
        "outr": ["outre"],

        "urn": ["urne"]

        }

def match(suffix, alist):
    matching = []
    for name in alist:
        if name.endswith(tuple(suffix)):
            matching.append(name)
    return matching

def find_matching(options, lista, listb):
    sound = sounds[random.choice(list(sounds.keys()))]
    if options.debug:
        print(sound)

    matching_lista = match(sound, lista)
    matching_listb = match(sound, listb)
    if matching_lista and matching_listb:
        return matching_lista, matching_listb
    else:
        return find_matching(options, lista, listb)
