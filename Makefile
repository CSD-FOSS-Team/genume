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
	@pycodestyle --ignore=E501,E402 bash_helpers/
	@echo OK

.phony: git
git:
	git remote add upstream https://github.com/CSD-FOSS-Team/genume || true
	git remote -v

.phony: update
update: git
	git fetch upstream
	git rebase -i upstream/master

.phony: contributors
contributors:
	./authors.sh > AUTHORS
	cp AUTHORS scripts/about/

.phony: install
install:
	python3 setup.py install

.phony: help
help:
	@echo "Usage: make [run|lint|git|update|contributors|install]"
