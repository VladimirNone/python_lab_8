# gRPC Glossary Application

## Установка и запуск

1. Клонируйте репозиторий:
  ```bash
  git clone https://github.com/VladimirNone/python_lab_8
  ```
2. Соберите и запустите контейнеры:

```bash
docker-compose up --build
```
3. Взаимодействие необходимо осуществлять с помощью следующего endpoint:

```bash
http://localhost:50051
```
4. Для взаимодействия с сервером реализован клиент, для его запуска необходимо выполнить следующую команду:
```bash
python client.py
```
## Методы
- ListTerms: Получить список всех терминов.
- GetTerm(TermRequest): Получить данные о конкретном термине.
- AddTerm(Term): Добавить новый термин.
- UpdateTerm (Term): Обновить существующий термин.
- DeleteTerm (TermRequest): Удалить термин.