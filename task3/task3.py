import json
import queue
with open('tests.json', 'r') as json_tests_file:
    tests = json.load(json_tests_file)

with open('values.json', 'r') as json_values_file:
    values = json.load(json_values_file)['values']




values_upgraded = dict()
for i in values:
    values_upgraded[i['id']] = i['value']
values = values_upgraded

stack = [tests['tests']]


while stack:
    test = stack.pop()
    for i in test:
        if 'value' in i:
            i['value'] = values[i['id']]
        if 'values' in i and i['values']:
            stack.append(i['values'])


new_file = open('report.json', 'w')
json.dump(tests, new_file)
new_file.close