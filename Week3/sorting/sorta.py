#!/usr/bin/env python3
#sorting practice

coastal = ['Atlanta', 'Vegas', 'Portland', 'San F', 'San Jose', 'NYC']

print('Sorting stuff!!!!', sorted(coastal))

print('Reverse sorting stuff!!!!', sorted(coastal, reverse=True))

print('\nOur list can be sorted with a key=len', sorted(coastal, key=len))
