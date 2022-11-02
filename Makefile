#Makefile
lint:
	poetry run flake8 brain_games
	
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
brain-prime:
	poetry run brain-prime
brain-prog:
	poetry run brain-progression

install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force

docker-build: build
	docker build -t kaziamov/brain-games .
docker-run:
	docker run -it kaziamov/brain-games:v1 /bin/sh