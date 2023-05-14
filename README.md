[![api_yamdb workflow](https://github.com/askwlc/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/askwlc/yamdb_final/actions/workflows/yamdb_workflow.yml)

# Проект YaMDb 

![Logo](https://cdn-irec.r-99.com/sites/default/files/product-images/399872/EOXOqQkXnjTMTRnIpMUSvQ.jpg)

Команда разработки: 

- ✅ [Nikita Shinkov (в роли Python-разработчика Тимлид)](https://github.com/askwlc/)
- ✅ [Igor Merkushev (в роли Python-разработчика)](https://github.com/#)
- ✅ [Sergei Tregubov (в роли Python-разработчика)](https://github.com/SergeiTregubov/)

[Описание](#описание) /
[Техническое описание](#Техническое_описание_проекта_YaMDb) /
[Развернуть локально](#Как_запустить_проект)

## Описание

Проект YaMDb

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Стек технологий использованный в проекте:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=043A6B)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=ffffff&color=043A6B)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=ffffff&color=043A6B)](https://gunicorn.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=ffffff&color=043A6B)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=ffffff&color=043A6B)](https://cloud.yandex.ru/)

## Техническое описание проекта YaMDb:

### Ресурсы API YaMDb:
- auth: аутентификация.
- users: пользователи.
- titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано только к одной категории.
- genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
- comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.

### Пользовательские роли:
Аноним, Аутентифицированный пользователь, Модератор, Администратор, Суперюзер.

Реализована самостоятельная регистрация пользователей через эндпоинт /api/v1/auth/signup/ с последующим получением JWT-токена.

## Как запустить проект:

Клонировать репозиторий
```
git clone https://github.com/askwlc/infra_sp2.git
```

Перейти в папку:
```
cd infra
```
Развернуть контейнеры:
```
docker-compose up 
```
Сделать миграции, суперпользователя и собрать статику:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
Заполнить базу данными из копии:
```
docker-compose exec web python manage.py loaddata ../infra/fixtures.json 
```

#### Подробную документацию можно посмотреть по [ссылке](http://127.0.0.1:8000/redoc/) после запуска сервера с проектом.
#### Временный тестовый сервер для проверки работоспособности [ссылке](http://51.250.80.143/api/)