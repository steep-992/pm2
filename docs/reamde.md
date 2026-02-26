# PM2 — Flask + MySQL

Учебный проект по ПМ.02.  
Реализован REST API на Flask с записью данных в базу данных MySQL.

## Стек
- Python
- Flask
- MySQL
- PyMySQL
- Postman

## Структура проекта

pm2/
├─ app.py # Flask API
├─ requirements.txt
├─ .gitignore
├─ docs/
│ ├─ create_table.sql
│ └─ report.md 
└─ postman/
└─ flask_tests.json


## Что было сделано

### 1. Создание базы данных
База данных создана вручную в MySQL.  
Созданы таблицы:
- users — хранение пользователей
- logs — журнал действий

SQL-скрипт находится в `docs/create_table.sql`.

### 2. Реализация API
Реализован REST API на Flask.

Метод:
- POST `/users` — приём JSON-данных, валидация и запись пользователя в БД

### 3. Проверка и валидация
- Проверка наличия JSON
- Проверка обязательных полей `username`, `email`

### 4. Отладка
Отладка выполнена с использованием debug-режима Flask.

### 5. Тестирование
Тестирование API выполнено в Postman.  
Коллекция запросов сохранена в `postman/flask_tests.json`.

### 6. Хранение кода
Исходный код и все вспомогательные файлы загружены в репозиторий GitHub.

## Запуск проекта

1. Установить зависимости:
```bash
pip install -r requirements.txt

python app.py