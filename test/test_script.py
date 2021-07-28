from unittest import TestCase
from script_engine.script import Script


class TestCondition(TestCase):
    def test_next_step(self):
        script = Script()
        script.next_step({'TEST': 1})
