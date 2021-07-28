from unittest import TestCase
from script_engine.engine import test


class TestExample(TestCase):
    def test(self):
        self.assertEqual(test(), True)
