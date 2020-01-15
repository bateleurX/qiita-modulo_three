#!/usr/bin/env python3

from automata.fa.dfa import DFA
import sys

input = sys.argv[1]

if not input.isnumeric:
    print("引数には数値を指定してください")
    sys.exit(1)


modulo = DFA(
    states = {'q0', 'q1', 'q2'},
    input_symbols = {'0', '1'},
    transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q1', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q0'}

)

# inputで入力値を指定する
print(input)

# bin()関数でも良さそうに見えるが、bin()だと頭に0bがついてしまうため、formatを使う
entry = format(int(input),'b')

# accepd_inputで受理するか判定
if modulo.accepts_input(entry):
    print("Result: Accepted")
else:
    print("Result: Rejected")

# 遷移はread_input_stepwiseで表示可能
print("Transitions")
for i in modulo.read_input_stepwise(entry):
    print(i)
