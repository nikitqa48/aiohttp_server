## Билд проекта
```
docker build -t aiohttp_server .
```

### Запустить проект
```
docker run -p 8080:8080 aiohttp_server
```


### Запустить тесты
Убедитесь что контейнер запущен. Из корня проекта выполните команду
```
pytest src/tests/main.py
```
