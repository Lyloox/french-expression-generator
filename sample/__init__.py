from generator import generate_animals, generate_expressions
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--number", type="int", dest="n",
        help="print n number of french expressions", metavar="NUMBER")
parser.add_option("-c", "--category", type="string", dest="category",
        help="what do you want to generate? possibilities : 'animals' and 'expression'", metavar="STRING")
parser.add_option("-d", "--debug", dest="debug", action="store_true",
        help="print debug messages", metavar="BOOLEAN")
(options, args) = parser.parse_args()

if not options.n:
    options.n = 1

if not options.category:
    options.category = "animals"

if __name__ == "__main__":
    if options.category == "animals":
        generate_animals(options)
    else:
        generate_expressions(options)
