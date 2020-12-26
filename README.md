# Poll API
API для системы опросов пользователей

##### Функционал для администратора системы:
- авторизация в системе (без регистрации)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

##### Функционал для пользователей системы:
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

#### Установка:
1. Склонируйте репозиторий
2. Создайте и войдите в вирутальное окружение
3. Установите зависимости:
    - `pip install -r requirements.txt`
4. Проведите миграции
    - `python manage.py makemigrations`
    - `python manage.py migrate`
5. Создайте суперпользователя
    - `python manage.py createsuperuser`
6. Запустите тестовый сервер
    - `python manage.py runserver`
    
#### Документация по API
   
##### Алгоритм авторизации пользователей
1. Пользователь отправляет запрос с параметрами `username` и `password` на `/api/token/`, в ответе на запрос ему приходит `token` (JWT-токен) в поле access.
2. При отправке запроса передавайте токен в заголовке Authorization: Bearer <токен>
(Для включения авторизации по JWT токену раскомментируйте раздел REST_FRAMEWORK в settings.py)

##### Добавление опросов (POST)
- Права доступа: `Администратор`
- URL: `/api/polls/`
- QUERY PARAMETERS: `name`, `end_date`, `description`
###### Изменение/удаление опросов (PUT, DELETE)
- Права доступа: `Администратор`
- URL: `/api/polls/<poll_id>/`

##### Добавление вопросов к опросу (POST)
- Права доступа: `Администратор`
- URL: `/api/polls/<poll_id>/questions/`
- QUERY PARAMETERS: `text`, `type_question`(text_field or radio or check_boxes), `poll`
###### Изменение/удаление вопросов (PUT, DELETE)
- Права доступа: `Администратор`
- URL: `/api/polls/<poll_id>/questions/<question_id>/`
##### Добавление и просмотр вариантов ответа к вопросу (POST, GET)
- Права доступа: `Администратор`
- URL: `/api/polls/<poll_id>/questions/<question_id>/choices/`
- QUERY PARAMETERS: `text`

##### Получение списка активных опросов (GET)
- Права доступа: `Любой пользователь`
- URL: `/api/active_polls/`

##### Прохождение опроса (POST)
- Права доступа: `Авторизованный пользователь`
- URL: `/api/polls/<poll_id>/questions/<question_id>/answers/`

##### Получение пройденных пользователем опросов (GET)
- Права доступа: `Авторизованный пользователь`
- URL: `/api/my_polls/`
