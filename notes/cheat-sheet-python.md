# Cheat Sheet Python

## See the bytecode and abstract syntax tree of a function

```python
In [2]: import dis

In [8]: def cond():
   ...:     x = 3
   ...:     if x < 5:
   ...:         return "yes"
   ...:     else:
   ...:         return "no"
   ...:

In [9]: dis.dis(cond)
  2           0 LOAD_CONST               1 (3)
              2 STORE_FAST               0 (x)

  3           4 LOAD_FAST                0 (x)
              6 LOAD_CONST               2 (5)
              8 COMPARE_OP               0 (<)
             10 POP_JUMP_IF_FALSE        8 (to 16)

  4          12 LOAD_CONST               3 ('yes')
             14 RETURN_VALUE

  6     >>   16 LOAD_CONST               4 ('no')
             18 RETURN_VALUE

In [16]: import inspect

In [17]: code = inspect.getsource(cond)

In [18]: code
Out[18]: 'def cond():\n    x = 3\n    if x < 5:\n        return "yes"\n    else:\n        return "no"\n'

In [19]: import ast

In [20]: ast_tree = ast.parse(code)

In [24]: from pprint import pprint

In [25]: pprint(ast.dump(ast_tree))
("Module(body=[FunctionDef(name='cond', args=arguments(posonlyargs=[], "
 'args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), '
 "body=[Assign(targets=[Name(id='x', ctx=Store())], value=Constant(value=3)), "
 "If(test=Compare(left=Name(id='x', ctx=Load()), ops=[Lt()], "
 'comparators=[Constant(value=5)]), '
 "body=[Return(value=Constant(value='yes'))], "
 "orelse=[Return(value=Constant(value='no'))])], decorator_list=[])], "
 'type_ignores=[])')
```

## Shebang

`#!/usr/bin/env python3` - python3 shebang

## Best Practices Cookiecutter

[link](https://github.com/sourcery-ai/python-best-practices-cookiecutter)

Use this to start the next python project.

## defaultdict

`from collections import defaultdict`

## Use `help` command instead of googling

In an interactive python session, use `help` in any python objects.

For example:

```
>>> import csv
>>> help(csv)
```

## Links to this note

[Index Cheat Sheet](index-cheat-sheet.md)
