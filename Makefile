# Path for testing if these dependencies are not installed.
PYTHONPATH=src:../dls-hazzathread/src:../dls-mainiac/src:../dls-logform/src

# ------------------------------------------------------------------
# Tests.

test-01-sigint:
	python3 -m pytest -sv tests/test_01_sigint.py
test-02-sigint2:
	python3 -m pytest -sv tests/test_02_sigint2.py

# ------------------------------------------------------------------
# GitLab CI.

pytest:
	PYTHONPATH=$(PYTHONPATH) python3 -m pytest

# ------------------------------------------------------------------
# Utility.

.PHONY: list
list:
	@awk "/^[^\t:]+[:]/" Makefile | grep -v ".PHONY"

show-version:
	PYTHONPATH=$(PYTHONPATH) python3 -m dls_siggy_lib.version --json
	PYTHONPATH=$(PYTHONPATH) python3 -m dls_siggy_lib.version

# ------------------------------------------------------------------
# Version bumping.  Configured in setup.cfg. 
# Thanks: https://pypi.org/project/bump2version/
bump-patch:
	bump2version --list patch

bump-minor:
	bump2version --list minor

bump-major:
	bump2version --list major
	
bump-dryrun:
	bump2version --dry-run patch
	