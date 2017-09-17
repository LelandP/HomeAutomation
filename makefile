.PHONY: nodes tools clean
.DEFAULT_GOAL: help

clean: nodes.clean tools.clean server.clean
	rm -rf output

virtualenv:
	if [ ! -d "output" ]; then \
        mkdir -p output;\
		pip install virtualenv;\
		virtualenv output/testenv;\
    fi

#this section is for the tools make scripts

tools.clean:
	rm -rf tools/dist
	rm -rf tools/build
	rm -rf tools/OSHA_tools.egg-info

tools: tools.clean
	(cd tools;\
	python setup.py bdist_wheel)

#this section is for the server make scripts

server.clean:
	rm -rf server/dist
	rm -rf server/build
	rm -rf server/OSHA_server.egg-info

server: server.clean tools
	(. output/testenv/bin/activate; \
	cd server;\
	python setup.py bdist_wheel;\
	pip uninstall -y OSHA_tools;\
	pip install ../tools/dist/*;\
	pip uninstall -y OSHA_server;\
	pip install dist/*)

server.run: virtualenv server
	(. output/testenv/bin/activate; \
	OSHA-Server)


#this section is for the node makescript

nodes.clean:
	rm -rf nodes/dist
	rm -rf nodes/build
	rm -rf nodes/OSHA_nodes.egg-info

nodes: nodes.clean tools
	(. output/testenv/bin/activate; \
	cd nodes;\
	python setup.py bdist_wheel;\
	pip uninstall -y OSHA_tools;\
	pip install ../tools/dist/*;\
	pip uninstall -y OSHA_nodes;\
	pip install dist/*)

nodes.run: virtualenv nodes
	(. output/testenv/bin/activate; \
	OSHA-Hue)

help:
	@echo "TO-DO Help"