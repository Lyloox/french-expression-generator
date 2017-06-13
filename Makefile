
animal:
	python3 generator/__init__.py -n 10

expression:
	python3 generator/__init__.py -c "expression" -n 10

format:
	cd data; python3 format.py

init:
	pip install -r requirements.txt

test:
	python3 -m unittest tests/test_generator.py
