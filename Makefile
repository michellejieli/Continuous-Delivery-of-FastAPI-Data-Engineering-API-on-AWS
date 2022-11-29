install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	echo "Not implemented yet"
	python -m pytest -vv test_*.py

format:
	black *.py 
	#hlib/*.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py 

refactor: format lint

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 681238067355.dkr.ecr.us-east-1.amazonaws.com
	docker build -t recipe_ideas .
	docker tag recipe_ideas:latest 681238067355.dkr.ecr.us-east-1.amazonaws.com/recipe_ideas:latest
	docker push 681238067355.dkr.ecr.us-east-1.amazonaws.com/recipe_ideas:latest
all: install lint test
