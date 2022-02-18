PYTHON := /usr/bin/python3
SHELL := /bin/bash # Make sure SHELL is bash as source is being used - It failed on GitHub runners
VENV_PATH := $(CODE_SAMPLE_DIR)/.venv
VENV_DONE := $(CODE_SAMPLE_DIR)/.venv.sentinel

$(VENV_DONE): $(CODE_SAMPLE_DIR)/common/venv_requirements.txt
	@echo Creating Python venv
	$(PYTHON) -m venv $(VENV_PATH) --system-site-packages
	source $(VENV_PATH)/bin/activate && \
		pip install -r $<
	touch $@

export VIRTUAL_ENV := $(VENV_PATH)
export PATH := $(VIRTUAL_ENV)/bin:$(PATH)
