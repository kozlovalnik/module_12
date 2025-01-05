import unittest
import module_12_1_testRunner
import module_12_2_testRunnerPlus

runner_tstSuite = unittest.TestSuite()
runner_tstSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1_testRunner.RunnerTest))
runner_tstSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_testRunnerPlus.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_tstSuite)
