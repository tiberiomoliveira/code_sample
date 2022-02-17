CODE_SAMPLE_DIR = $(abspath ../../../)
include $(CODE_SAMPLE_DIR)/common/gen_py_venv.mk

TESTS := $(wildcard tests/test_*.py)

.PHONY: check lint-check all

all: check lint-check

check: $(VENV_DONE) $(TESTS)
	coverage run -m unittest discover -b -v -s tests
	coverage report --fail-under=95
	coverage html -d .html_coverage

lint-check: $(VENV_DONE) *.py $(TESTS)
	pylint $^ --reports=no
