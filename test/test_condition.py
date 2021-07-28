from unittest import TestCase
from script_engine.condition import Condition, ConditionOperator


class TestCondition(TestCase):
    def test_eq(self):
        condition = Condition()
        op = ConditionOperator['eq']

        self.assertEqual(condition.compare(1, op, 2), False)
        self.assertEqual(condition.compare(2, op, 2), True)
        self.assertEqual(condition.compare(2, op, 1), False)
        self.assertEqual(condition.compare(None, op, 2), False)
        self.assertEqual(condition.compare(None, op, None), True)
        self.assertEqual(condition.compare('test', op, 'test'), True)
        self.assertEqual(condition.compare('test', op, 'testtest'), False)
        self.assertEqual(condition.compare('testtest', op, 'test'), False)
        self.assertEqual(condition.compare('1', op, 1), False)

    def test_gt(self):
        condition = Condition()
        op = ConditionOperator['gt']

        self.assertEqual(condition.compare(1, op, 2), False)
        self.assertEqual(condition.compare(2, op, 2), False)
        self.assertEqual(condition.compare(2, op, 1), True)
        self.assertEqual(condition.compare(None, op, 2), False)
        self.assertEqual(condition.compare(None, op, None), False)
        self.assertEqual(condition.compare('test', op, 'test'), False)
        self.assertEqual(condition.compare('test', op, 'testtest'), False)
        self.assertEqual(condition.compare('testtest', op, 'test'), True)
        # self.assertEqual(condition.compare('1', op, 1), False)
