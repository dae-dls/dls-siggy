# dls-siggy

## Summary

Python class enhancing signal handling.

The software development group needs a simple high level API to capture and report unix signals, such as control-C.
This reduces development time to create and test a signal handling in command line and gui programs.
This library provides a signal class with state and counting, as well as a global (module) instance of it.

This is a Python library with API for high level unix signal handling.

## Usage
Please see the tests for more working examples.

```python
from dls_siggy_lib.global_signals import global_sigint
...
# Activate the signal handling.
global_sigint.activate()
...
# Check if signals have happened.
assert global_sigint.count() == 2
```

## Installation
```
pip3 install git+https://github.com/david-a-erb/dls-siggy.git@develop
```

## FAQ

____________________________________________________________________________
#### How do you update the version?

```make bump-patch```  
```make bump-minor```  
```make bump-major```   

____________________________________________________________________________
#### What remains to be done?

- Ability to insert custom signal handling.
- Handle more signals than just sigint.
- Change module level global_signals to true singleton object.

