# yacut
Проект реализует сервис предоставления коротких ссылок.
## Автор:
Алексей Наумов ( algena75@yandex.ru )
## Используемые технолологии:
* Flask
* SQLAlchemy
* RegEx
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:


```
git clone git@github.com:Algena75/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Как запустить проект:
```
flask run
```
