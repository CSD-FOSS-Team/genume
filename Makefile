# Utility makefile for python shortcuts

PYTHON := $(shell command -v python3 > /dev/null && echo python3 || echo python)

.phony: run
run:
	@$(PYTHON) -m genume

.phony: sudorun
sudorun:
	@sudo $(PYTHON) -m genume

.phony: lint
lint:
	@$(PYTHON) -m compileall -fq genume
	@pycodestyle --ignore=E501,E402 genume/
	@echo OK

.phony: git
git:
	git remote add upstream https://github.com/CSD-FOSS-Team/genume
	git remote -v

.phony: help
help:
	@echo "Usage: make [run|lint|git]"
