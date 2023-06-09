# Домашнее задание на тему DRF
## TODO api
Продолжение предыдущего дз, на закрепление понимания django rest framework. Нужно дополнить управление задачами с помощью rest api с использованием drf.

Ожидаются вот такие методы для управления задачами

- GET /api/tasks - получть список всех задач
- GET /api/tasks/{id} - получть одну конкретную задачу
- POST /api/tasks - создать задачу
- PUT (или PATCH) /api/tasks/{id} - отредактировать существующую задачу
- DELETE /api/tasks/{id} - удалить одну задачу

При этом обязательно:
- Использовать фильтрацию для поиска задачи по заголовку (запрос GET может быть дополнен query-параметром ?title=...)
- Использовать фильтрацию для поиска активных\неактривных задач (запрос GET может быть дополнен query-параметром ?is_active=...)
- Должна быть пагинация при GET-запросе (любая)
- Должна быть возможность упорядочить результат GET - запроса (запрос GET может быть дополнен query-параметром ?ordering=...)

## Требования:
- Написать приложение используя фреймворк django и библиотеку django-rest-framework.
- используйте requirements.txt для указания сторонних зависимостей и их версий
- используйте результат своего предыдущего дз
- Форматирование учитывается. Используйте black

## Ожидаемый результат
Реализуйте программу согласно требованиям описанным выше.
Ответом на задание будет считаться ссылка на ваш Merge Request в вашем репозитории. Убедитесь, что проверяющий может комметировать ваш Merge Request чтобы вы смогли получить обратную связь по сделанному заданию.

# Решение задания:
Зависимости в файле **req.txt**.
- Использована реляционная субд SQLite.
- Использован фреймворк django и django-rest-framework. 
- Создана модель согласно заданию.
- Управление задачами доступно из админки (user:user). 
- фильтрацию для поиска задачи по заголовку ( ?title=...)
- фильтрацию для поиска активных\неактривных задач ( ?completed=...)
- пагинация при GET-запросе
- возможность упорядочить результат GET - запроса ( ?ordering=...)
                     
 
Запуск:
```
 python manage.py runserver
```
