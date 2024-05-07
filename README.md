# angry-test

#### Запуск тестов:

1. настроить виртуальное окружение

```commandline
python3.11 -m venv venv
source venv/bin/activate
```

2. Установить зависимости:

```commandline
pip install poetry
poetry update
```

3. Запустить тесты

```commandline
poetry run pytest
```

#### Запус приложения может производиться двумя способами:

1) Используя gunicorn (пример команды описан в .deploy/Dockerfile:CMD)
2) Стандартным через запуск main-файла

```commandline
python3 main.py
```

также при запуске доступны cli-аргументы посмотреть которые можно выполнив:

```commandline
python3 main.py --help
```

