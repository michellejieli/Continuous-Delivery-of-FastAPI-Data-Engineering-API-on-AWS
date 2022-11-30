install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=logic test_*.py

format:
	black *.py 

lint:
	pylint --disable=R,C *.py

refactor: format lint

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 681238067355.dkr.ecr.us-east-1.amazonaws.com
	docker build -t recipe_ideas .
	docker tag recipe_ideas:latest 681238067355.dkr.ecr.us-east-1.amazonaws.com/recipe_ideas:latest
	docker push 681238067355.dkr.ecr.us-east-1.amazonaws.com/recipe_ideas:latest

all: install lint test format deploy
