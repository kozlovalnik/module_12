class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 5)
        self.runner3 = Runner('Ник', 3)

#    @classmethod
    def tearDown(self):
        print(self.all_results)

    def test_Tournament1(self):
        self.all_results = Tournament(90, self.runner1, self.runner3).start()
        self.assertTrue(self.all_results[len(self.all_results)] == 'Ник')


    def test_Tournament2(self):
        self.all_results = Tournament(90, self.runner2, self.runner3).start()
        self.assertTrue(self.all_results[len(self.all_results)] == 'Ник')

    def test_Tournament3(self):
        self.all_results = Tournament(90, self.runner1, self.runner2, self.runner3).start()
        self.assertTrue(self.all_results[len(self.all_results)] == 'Ник')

if __name__ == '__main__':
    unittest.main()
