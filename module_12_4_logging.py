import logging
import unittest
from idlelib.iomenu import encoding


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_wolk(self):
        try:
            self.TestRunner = Runner('test_runner', speed=-5)
            for _ in range(10):
                self.TestRunner.walk()
            self.assertEqual(self.TestRunner.distance,50)
            logging.info('test_walk выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.TestRunner = Runner(124)
            for _ in range(10):
                self.TestRunner.run()
            self.assertEqual(self.TestRunner.distance,100)
            logging.info('test_run выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.TestRunner1 = Runner('test_runner1')
        self.TestRunner2 = Runner('test_runner2')
        for _ in range(10):
            self.TestRunner1.run()
            self.TestRunner2.walk()
        self.assertNotEqual(self.TestRunner1.distance,self.TestRunner2.distance)


logging.basicConfig(filename='module_12_4_logging.log', filemode='w', level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", encoding='UTF-8')

if __name__ == '__main__':
    unittest.main()
