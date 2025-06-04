# Makefile — underwriting-uap
PYBIN ?= python      # use venv’s python

.PHONY: ingest upload-kb

ingest:
	$(PYBIN) -m scripts.ingest kb/raw kb/processed

upload-kb:
	$(PYBIN) -m scripts.contextual_sdk kb/processed
