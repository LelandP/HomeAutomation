.PHONY: nodes

main.wheel:


virtualenv:
	mkdir -p output
	pip install virtualenv
	virtualenv output/testenv
	
server.run: virtualenv
	echo "server run"

nodes:
	echo "nodes"
	(. output/testenv/bin/activate; \
	cd nodes;\
	python setup.py bdist_wheel;\
	pip install dist/*)

nodes.run: virtualenv nodes
	(. output/testenv/bin/activate; \
	OSHA-Water)