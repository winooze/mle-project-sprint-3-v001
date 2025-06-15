# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
```python
# команды создания виртуального окружения
# и установки необходимых библиотек в него
python -m venv .venv 
source .venv/bin/activate

# команда перехода в директорию
cd services/ml_service/

# команда запуска сервиса с помощью uvicorn
uvicorn main:app --reload --port 8000 --host 0.0.0.0
```
### Для просмотра документации API и совершения тестовых запросов 

http://127.0.0.1:8000/docs 

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/score_estate/?id=124' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d ' { "is_apartment": false, "studio": false, "has_elevator": true, "building_type_int": 4, "floor": 5, "kitchen_area": 8.0, "living_area": 56.0, "rooms": 2, "total_area": 52.0, "build_year": 2007, "latitude": 55.72347640991211, "longitude": 37.903202056884766, "ceiling_height": 2.740000009536743, "flats_count": 376, "floors_total": 11 }'
```


## 2. FastAPI микросервис в Docker-контейнере

```bash
# команда перехода в нужную директорию
cd services 

# подтягиваем переменные 
export $(grep -v '^#' .env | xargs)

# собираем образ 
docker build . --tag sprint_3_project:0

# запускаем приложение из контейнера 
docker container run \
--publish ${APP_PORT}:${APP_PORT} \
--env-file .env \
--volume=./models:/services/models \
sprint_3_project:0

# команда для запуска микросервиса в режиме docker compose
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/score_estate/?id=124' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d ' { "is_apartment": false, "studio": false, "has_elevator": true, "building_type_int": 4, "floor": 5, "kitchen_area": 8.0, "living_area": 56.0, "rooms": 2, "total_area": 52.0, "build_year": 2007, "latitude": 55.72347640991211, "longitude": 37.903202056884766, "ceiling_height": 2.740000009536743, "flats_count": 376, "floors_total": 11 }'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <...> запросов в течение <...> секунд ...

```
# команды необходимые для запуска скрипта
...
```

Адреса сервисов:
- микросервис: http://localhost:<port>
- Prometheus: ...
- Grafana: ...