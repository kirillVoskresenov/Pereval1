# Заказ от Федерации Спортивного Туризма России (ФСТР)

Компания SkillFactory получила заказ от Федерации Спортивного Туризма России (ФСТР). Заказчик хочет решить проблему, связанную с отправкой данных о перевале.

## Цели проекта

ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и iOS, которое упростит туристам задачу по отправке данных о перевале и сократит время обработки запроса до трёх дней.

### Пользователи приложения

Мобильным приложением будут пользоваться туристы, которые в горах будут вносить данные о перевале и отправлять их в ФСТР, как только появится доступ в Интернет. Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

## Этапы работы над созданием мобильного приложения

Команда SkillFactory взяла разработку мобильного приложения «под ключ». Все работы ведут студенты SkillFactory и школы дизайна Contented от SkillFactory.

1. Разработка REST API, которое будет обслуживать мобильное приложение.
2. Разработка мобильного приложения.
3. Тестирование REST API и мобильного приложения.

### Функциональные требования

- Внесение информации о новом объекте (перевале) в карточку объекта.
- Редактирование в приложении неотправленных на сервер ФСТР данных об объектах. На перевале не всегда работает Интернет.
- Заполнение ФИО и контактных данных (телефон и электронная почта) с последующим их автозаполнением при внесении данных о новых объектах.
- Отправка данных на сервер ФСТР.
- Получение уведомления о статусе отправки (успешно/неуспешно).
- Согласие пользователя с политикой обработки персональных данных в случае нажатия на кнопку «Отправить» при отправке данных на сервер.

### Данные о перевале

Пользователь с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:

- Координаты перевала и его высота.
- Имя пользователя.
- Почта и телефон пользователя.
- Название перевала.
- Несколько фотографий перевала.

## План работы

Твоя работа будет разбита на три спринта по одной неделе. Программисты с опытом обычно могут сами декомпозировать большую задачу на подзадачи. Однако так как ты только начинаешь свой путь и пришёл ко мне стажироваться, я помогу тебе в этом.

Мы будем «есть слона по частям» и использовать Agile-подход.

### Первый спринт

- Создание базы данных.
- Разработка класса по работе с БД.
- Один метод для REST API.

### Второй спринт

- Разработка ещё трёх методов для REST API.
- Задеплоить своё решение на сервере (это задание будет необязательным).

### Третий спринт

- Покрытие кода тестами (также необязательное задание).
- Подготовка документации.

## Метод POST submitData

Когда турист поднимется на перевал, он сфотографирует его и внесёт нужную информацию с помощью мобильного приложения:

- Координаты объекта и его высота.
- Название объекта.
- Несколько фотографий.
- Информацию о пользователе, который передал данные о перевале:
  - Имя пользователя (ФИО строкой).
  - Почта.
  - Телефон.
 ## Метод `submitData`

После того как турист нажмёт кнопку «Отправить» в мобильном приложении, приложение вызовет метод `submitData` Вашего REST API.

Добавь в свой REST API ещё три метода:

1. **GET /submitData/<id>** — получить одну запись (перевал) по её id.  
   Выведи всю информацию об объекте, в том числе статус модерации.

2. **PATCH /submitData/<id>** — отредактировать существующую запись (замена), если она в статусе new.  
   Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона.  
   Метод принимает тот же самый JSON, который принимал уже реализованный тобой метод submitData.

   В качестве результата верни два значения:
   - **state**:  
     1 — если успешно удалось отредактировать запись в базе данных.  
     0 — в противном случае.
   - **message**:  
     если обновить запись не удалось, напиши почему.

3. **GET /submitData/?user__email=<email>** — список данных обо всех объектах, которые пользователь с почтой `<email>` отправил на сервер.

### Описание

 
Стэк
Python 3.X
Django
Django REST framework
JSON
PostgreSQL
Swagger
Docker


Формат данных
Каждый объект в массиве имеет следующие поля:

beauty_title (string): Красивое название локации (например, "Пик Эльбруса").

title (string): Обычное название локации (например, "Эльбрус").

other_titles (string): Дополнительная информация о доступности (например, "Летом не сложно добраться").

connect (string): Дополнительные комментарии (например, "Остальное:").

add_time (string): Дата добавления информации в формате ISO 8601 (например, "2024-10-01T18:46:05.969487+03:00").

coords (object): Объект с координатами:

length (string): Широта местоположения.

width (string): Долгота местоположения.

height (integer): Высота в метрах над уровнем моря.

user (object): Объект с информацией о пользователе:

surname (string): Фамилия

name (string): Имя

patronymic (string): Отчество 

email (string): Эл. почта пользователя (например, "example@example.com").

phone_number (string): Телефон пользователя (например, "89999999999").

level (object): Уровни сложности в разные сезоны:

winter_level (string): Уровень сложности для зимы (например, "1A").

spring_level (string): Уровень сложности для весны (например, "1A").

summer_level (string): Уровень сложности для лета (например, "1A").

autumn_level (string): Уровень сложности для осени (например, "1A").

image (object): Объект, содержащий информацию о фотографии:

title (string): Название фотографии (например, "Эльбрус").

data (string($uri)): URL-адрес изображения (например, "http:example.jpg").

status (string): Статус объекта (например, "NW" - "новая запись"). Допустимые значения:

new - новая запись;
pending — если модератор взял в работу;
accepted — модерация прошла успешно;
rejected — модерация прошла, информация не принята.


Параметры запросов.
Для получения информации о локациях можно использовать следующий HTTP-запросы:

GET /api/pereval/
Получает список всех доступных локаций.

GET api/pereval/<int:pk>/
Получить одну запись (перевал) по её id. Выводится вся информацию об объекте, в том числе статус модерации.


POST /api/pereval/
Добавить новый перевал на сервер.

POST api/pereval/update/<int:pk>/
Возможность отредактировать существующую запись (замена), если она в статусе new. Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона.

Данные представлены в формате JSON и выглядят следующим образом:
```json
{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", // что соединяет, текстовое поле
  "add_time": "2021-09-22 13:18:13",
  "user": {
    "email": "qwerty@mail.ru",
    "surname: "Иванов",
    "name": "Иван",
    "patronomic": "Иванович",
    "phone_number": "+79992009574"
  },
  "coords": {
    "length": "45.3842",
    "width": "7.1525",
    "height": "1200"
  },
  "level": {
    "winter": "", // Категория трудности. В разное время года перевал может иметь разную категорию трудности
    "summer": "1А",
    "autumn": "1А",
    "spring": ""
  },
  "images": [
    {"data": "<картинка1>", "title": "Седловина"},
    {"data": "<картинка>", "title": "Подъём"}
  ]
}

