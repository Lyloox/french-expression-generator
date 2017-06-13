from generator import print_animals, print_expressions
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--number", type="int", dest="n", default=1,
        help="print n number of french expressions", metavar="NUMBER")
parser.add_option("-c", "--category", type="choice", dest="category", action="store",
        default="animals", choices=["animals", "expression"],
        help="choose a sentence category to generate", metavar="STRING")
parser.add_option("-d", "--debug", dest="debug", action="store_true",
        help="print debug messages", metavar="BOOLEAN")
(options, args) = parser.parse_args()

if __name__ == "__main__":
    if options.category == "animals":
        print_animals(options)
    else:
        print_expressions(options)
