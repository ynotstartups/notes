# Cheat Sheet Pytest

## Reminder

- IMPORTANT! MOCK WHERE THE VARIABLE IS IMPORTED!

## Mocking Constants

```python
from unittest import mock

class Foo:
    @mock.patch("project.modules.foo.BAR")
    def test_foo(self): # <-- Notice, there is NO mock_bar here
        ....
```

## Useful pytest options

`-k PATTERN` - run test matching PATTERN

`--pdbcls=IPython.terminal.debugger:TerminalPdb` - to use IPython debugger 

`-vvv` - stop pytest cutting off long assert failures

`--pdb` - open debug session when an error is raised

`--randomly-seed` - to reproduce the test output, useful for debugging flaky tests

```
================================ test session starts =================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
django: settings: foo.settings (from env)
Using --randomly-seed=3336252275 <--------- HERE ---------
rootdir: /home/foo/bar, configfile: setup.cfg
plugins: cov-2.12.1, fireman-2.12.1, user-client-0.4.0, django-3.10.0, Faker-9.8.2, i18n-client-0.1.6, lyst-data-dictionary-schemas-0.16.14, randomly-3.4.1, time-machine-2.4.0, django-heimdall-0.20.0
collected 10 items  
```

See other options in [official docs](https://docs.pytest.org/en/6.2.x/reference.html#command-line-flags)
