class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

import unittest

class RunnerTest(unittest.TestCase):
    def test_wolk(self):
        self.TestRunner = Runner('test_runner')
        for _ in range(10):
            self.TestRunner.walk()
        self.assertEqual(self.TestRunner.distance,50)

    def test_run(self):
        self.TestRunner = Runner('test_runner')
        for _ in range(10):
            self.TestRunner.run()
        self.assertEqual(self.TestRunner.distance,100)

    def test_challenge(self):
        self.TestRunner1 = Runner('test_runner1')
        self.TestRunner2 = Runner('test_runner2')
        for _ in range(10):
            self.TestRunner1.run()
            self.TestRunner2.walk()
        self.assertNotEqual(self.TestRunner1.distance,self.TestRunner2.distance)

if __name__ == '__main__':
    unittest.main()
