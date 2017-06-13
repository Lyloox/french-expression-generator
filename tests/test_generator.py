#!/user/bin/env python
import sys
sys.path.insert(0, "generator")
import generator

import unittest
import random
from functools import partial

class Options:
    debug = None
    n = 10
    category = "animals"

    def __init__(self, debug=None, n=10, category="animals"):
        self.debug = debug
        self.n = n
        self.category = category

class TestGenerator(unittest.TestCase):

    random.seed(42)

    def assert_length(self, func, n_tests=50, name=None):
        options = Options()
        for i in [random.randrange(10, 1000) for _ in range(n_tests)]:
            options.n = i
            print("Generating " + str(i) + " samples", end="")
            print((" for %s test..." % name) if name else "...")
            self.assertEqual(len(func(options)), options.n)

    def test_length_animals(self):
        """
        Test lengths of generated animals lists
        """
        self.assert_length(partial(generator.generate_animals),
                name="animals")

    def test_length_expressions(self):
        """
        Test lengths of generated expressions lists
        """
        self.assert_length(partial(generator.generate_expressions),
                name="expressions")

    if __name__ == "__main__":
        unittest.main()
