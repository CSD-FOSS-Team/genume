# Utility makefile for python shortcuts

.phony: run
run:
	python3 -m genume

.phony: lint
lint:
	pep8 --ignore=E501,E402 genume/

.phony: help
help:
	@echo "Usage: make [run|lint]"
