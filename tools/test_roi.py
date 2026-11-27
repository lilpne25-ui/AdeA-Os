import unittest
from dataclasses import replace
from roi import PLANS

class TestROI(unittest.TestCase):
    def test_base(self):
        for plan, expected in zip(PLANS, [53.8, 47.3, 9.1]):
            self.assertAlmostEqual(plan.calculate()["roi"], expected, places=1)
    def test_half_realization(self):
        for plan in PLANS:
            self.assertLess(replace(plan, realization=plan.realization/2).calculate()["roi"], 0)
    def test_no_benefit(self):
        self.assertIsNone(replace(PLANS[0], realization=0).calculate()["payback"])
    def test_costs(self):
        self.assertEqual([p.calculate()["cost"] for p in PLANS], [152000,344000,800000])

if __name__ == "__main__":
    unittest.main()
