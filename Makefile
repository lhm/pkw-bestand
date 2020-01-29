download: venv
	./venv/bin/python scripts/download.py

data/pkw-bestand-20190101.csv: venv download
	./venv/bin/python scripts/process.py

datapackage.json: venv data/pkw-bestand-20190101.csv
	./venv/bin/python scripts/create-package.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv
	rm -rf files/*.xlsx
	rm ./datapackage.json

clean-venv:
	rm -rf venv

clean-cache:
	rm .cache.sqlite

.PHONY: clean clean-venv download
