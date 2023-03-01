# ProjectT
Клиент для работы с Swagger API на базе DRF

## Фунционал
Поддерживает ручки
- https://go.teachbase.ru/api-docs/index.html#/courses/get_courses - список курсов
- https://go.teachbase.ru/api-docs/index.html#/courses/get_courses__id - детальное представление курса
- https://go.teachbase.ru/api-docs/index.html#/users/post_users_create - создание пользователя
- https://go.teachbase.ru/api-docs/index.html#/course_sessions/post_course_sessions__session_id__register - запись пользователя на сессию
- https://go.teachbase.ru/api-docs/index.html#/course_sessions/get_courses__course_id__course_sessions - сессии курсов

Так же ручки для работы с БД
- Список всех курсов - /courses/
- Детальное представление курса - /courses/<id>

## Стек
  Django 4.1, Django RestFramework 3.14, Postgres
