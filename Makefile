create_venv:
	python3 -m venv venv
install:
	pip3 install -r requirements.txt
freeze:
	pip3 freeze > requirements.txt
test:
	python3 -m unittest tests/question_A/tests.py
	python3 -m unittest tests/question_B/tests.py
start_server_question_C:
	export FLASK_ENV=development
	export FLASK_APP=chalenge/question_C/server.py
	flask run