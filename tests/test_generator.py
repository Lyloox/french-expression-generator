#!/user/bin/env python
import unittest
import sys
sys.path.insert(0, "generator")
import generator
import random

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

    def test_length(self):
        """
        Test length(s) of generated list(s)
        """
        n_tests = 50
        options = Options()
        for i in [random.randrange(10, 1000) for _ in range(n_tests)]:
            options.n = i
            print("Generating " + str(i) + " samples...")
            liste = generator.generate_animals(options)
            self.assertEqual(len(liste), options.n)

    if __name__ == "__main__":
        unittest.main()
