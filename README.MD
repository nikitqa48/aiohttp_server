## Билд проекта
```
docker build -t aiohttp_server .
```

### Запустить проект
```
docker run -p 8080:8080 aiohttp_server
```


### Запустить тесты
Убедитесь что контейнер запущен. 

Установите все зависимости poetry
````
poetry install
````

Из корня директории проекта запустите команду

```
pytest src/tests/main.py
```
