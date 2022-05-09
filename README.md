# dls-signals

## Summary

Python class enhancing signal handling.

The software development group needs a simple high level API to capture and report unix signals, such as control-C.
This reduces development time to create and test a signal handling in command line and gui programs.
This library provides a signal class with state and counting, as well as a global (module) instance of it.

This is a Python library with API for high level unix signal handling.

## Usage
Please see the tests for more working examples.

```python
from dls_signals_lib.global_signals import global_sigint
...
# Activate the signal handling.
global_sigint.activate()
...
# Check if signals have happened.
assert global_sigint.count() == 2
```


## FAQ

____________________________________________________________________________
#### How do you update the version?

```semver bump patch```  
```semver bump minor```  
```semver bump major```   

See https://gitlab.maxiv.lu.se/kits-maxiv/app-maxiv-semver

____________________________________________________________________________
#### What remains to be done?

- A simple bare-bones test.
- Ability to insert custom signal handling
- Change module level global_signals to true singleton object.

