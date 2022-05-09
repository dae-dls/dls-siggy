
PYTHONPATH=src:../dls-hazzathread/src:../dls-mainiac/src:../dls-logging-formatter/src

# ------------------------------------------------------------------
# Tests.

test-01-sigint:
	python3 -m pytest -sv tests/test_01_sigint.py
test-02-sigint2:
	python3 -m pytest -sv tests/test_02_sigint2.py

# ------------------------------------------------------------------
# GitLab CI.

gitlab_ci_test:
	python3 -m pytest -sv -rfp --capture=no --cov=dls_signals_lib \
		tests/test_01_sigint.py

pytest:
	PYTHONPATH=$(PYTHONPATH) python3 -m pytest --capture=no 

test-ci:
	PYTHONPATH=$(PYTHONPATH) make -s gitlab_ci_test

gitrun-unittest:
	gitlab-runner exec docker unittest 2>&1 | tee gitrun-unittest.log

# ------------------------------------------------------------------
# Utility.

.PHONY: list
list:
	@awk "/^[^\t:]+[:]/" Makefile | grep -v ".PHONY"

show-version:
	PYTHONPATH=$(PYTHONPATH) python3 -m dls_signals_lib.version --json
	PYTHONPATH=$(PYTHONPATH) python3 -m dls_signals_lib.version

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
	