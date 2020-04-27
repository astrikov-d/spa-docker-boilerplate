help:
	@echo "isort-check - check code by iSort"
	@echo "isort - iSorting all code"
	@echo "lint - run flake8 linter"
	@echo "test - run py.test with coverage plugin"
	@echo "makemigrations - make django migrations"
	@echo "migrate - run django migrations"
	@echo "shell - open python shell on running backend container"
	@echo "bash - open bash on running backend container"

isort-check:
	docker exec -it sample-project-django isort -rc -c app
	docker exec -it sample-project-django isort -rc -c tests
	docker exec -it sample-project-django isort -rc -c conf
	docker exec -it sample-project-django isort -rc -c srv

isort:
	docker exec -it sample-project-django isort -rc app
	docker exec -it sample-project-django isort -rc tests
	docker exec -it sample-project-django isort -rc conf
	docker exec -it sample-project-django isort -rc srv

lint:
	docker exec -it sample-project-django flake8 app tests conf srv

test:
	docker exec -it sample-project-django py.test --nomigrations --ds conf.settings ./tests

makemigrations:
	docker exec -it sample-project-django python manage.py makemigrations

migrate:
	docker exec -it sample-project-django python manage.py migrate

shell:
	docker exec -it sample-project-django python manage.py shell

bash:
	docker exec -it sample-project-django /bin/bash
