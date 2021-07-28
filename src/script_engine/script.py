from script_engine.condition import Condition, ConditionOperator


class Script:
    def __init__(self):
        self.current_step = 1
        self.variables = {'TEST': 1}
        self.conditions = [
            {'left_type': 'value', 'left_value': 1, 'operator': 'eq', 'right_type': 'variable', 'right_value': 'TEST'},
            {'left_type': 'value', 'left_value': 1, 'operator': 'gt', 'right_type': 'value', 'right_value': 2},
            {'left_type': 'value', 'left_value': 2, 'operator': 'eq', 'right_type': 'value', 'right_value': 1}
        ]

    def next_step(self, variables):
        self.variables.update(variables)
        for item in self.conditions:
            if item['left_type'] == 'variable':
                item['left_value'] = self.variables.get(item['left_value'])

            if item['right_type'] == 'variable':
                item['right_value'] = self.variables.get(item['right_value'])

            operator = ConditionOperator[item['operator']]

            print(Condition().compare(item['left_value'], operator, item['right_value']))
