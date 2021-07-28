from enum import Enum
from typing import Any


class ConditionOperator(Enum):
    eq = 'eq'  # ==
    gt = 'gt'  # >
    ge = 'ge'  # >=
    lt = 'lt'  # <
    le = 'le'  # <=
#     'ne': '!=',
#     'include': '({0} != null && {1}.toString().toLowerCase().indexOf({2}.toString().toLowerCase()) >= 0 ? true : false)',
#     'exclude': '({0} != null && {1}.toString().toLowerCase().indexOf({2}.toString().toLowerCase()) == -1 ? true : false)',
#     'startsWith': '({0} != null && {1}.toString().toLowerCase().startsWith({2}.toString().toLowerCase()))',
#     'notStartsWith': '({0} != null && {1}.toString().toLowerCase().startsWith({2}.toString().toLowerCase()) == false)',
#     'endsWith': '({0} != null && {1}.toString().toLowerCase().endsWith({2}.toString().toLowerCase()))',
#     'notEndsWith': '({0} != null && {1}.toString().toLowerCase().endsWith({2}.toString().toLowerCase()) == false)',
#     'empty': '(boolean) ({0} == null || {0} == "" || {0} == Integer.MIN_VALUE '
#     '|| {0} == "__date::1970-01-01" || {0} == "__time::00:00:00.999999" '
#     '|| {0} == "__datetime::1970-01-01T00:00:00.000000+0000")',
#
#
# 'notEmpty': '(boolean) ({0} != null && {0} != "" && {0} != Integer.MIN_VALUE '
# '&& {0} != "__date::1970-01-01" && {0} != "__time::00:00:00.999999" '
# '&& {0} != "__datetime::1970-01-01T00:00:00.000000+0000")'


class Condition:
    def __init__(self):
        self.__operator_map = {
            ConditionOperator.eq: self.__eq,
            ConditionOperator.gt: self.__gt
        }

    @staticmethod
    def __eq(left_value: Any, right_value: Any) -> bool:
        return left_value == right_value

    @staticmethod
    def __gt(left_value: Any, right_value: Any) -> bool:
        if not left_value or not right_value:
            return False

        return left_value > right_value

    def compare(self, left_value: Any, operator: ConditionOperator, right_value: Any = None) -> bool:
        condition = self.__operator_map[operator]

        return condition(left_value, right_value)
