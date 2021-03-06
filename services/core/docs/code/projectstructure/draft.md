# Описание структуры проекта

```
/assets
- Здесь находятся различные файлы-ресурсы, которые необходимы в процессе работы(например, файлы с переводами ошибок, ключ-файл для взаимодействия с Google Play IAP и другое).

===========================

/docs
- Различная документация конкретно по службе "core".

===========================

$ /src
- Основные файлы исходного кода.

$ /src/bootstrap
- Файлы, отвечающие за начальную инициализую приложения(например, инициализация подключения к БД, к S3-сервису, к SMSC, инициализация API-сервера и так далее).

$ /src/configs
- Файлы, в которых хранятся различные настройки, параметры, а также "загрузчики" переменных окружений из файла(-ов) в переменные кода.

$ /src/internal
- Основные составляющие приложения, где находятся API-серверы, бизнес-логика, модели, провайдеры данных(запросы к БД) и так далее

$ /src/entities
- Все сущности приложения

$ /src/entities/biz
- "Бизнес-сущности"(аккаунты, объявления) и, соответственно, бизнес-логика(авторизация, регистрация, создание/редактирование/получение/удаление объявлений и другое в том же духе)

$ /src/entities/biz/accs
- Бизнес-сущность "Аккаунты". Здесь находятся модели, связанные с данной сущностью, и бизнес-логика, связанная с авторизацией, регистрацией, редактированием аккаунта, сменой пароля и так далее.

$ /src/entities/biz/accsproviders
- Различные поставщики данных для бизнес-сущности "Аккаунты". Исходники с запросами к БД.

$ /src/entities/extra
- Дополнительные сущности системы, которые не связаны напрямую с основной бизнес-логикой приложения. Например, загрузка файлов, работа с геолокацией и так далее.

$ /src/entities/service
- Служебные сущности системы, предназначенные прежде всего для разработчиков. Например, статистика, метрика, специальные логгеры и прочее.

$ /src/instances
- Экземпляры инициализованных драйверов(то есть посредники между драйверами и бизнес-логикой). Например, объект для работы с БД, SMSC-службой, S3-сервисом и так далее.

$ /src/servers
- Здесь находятся исходники, связанные с различными серверами(HTTP, WS, TCP, другое)

$ /src/servers/http
- Исходники, связанные с HTTP-серверами: роуты(контроллеры) и их обработчики

$ /src/lib
- Необходимые внутренние(свои, не PIP) модули.
- Подробности ниже.

$ /src/lib/drivers
- Драйверы для инициализации объектов для работы с различными сторонними службами(например, для взаимодействия с БД, с S3-сервисом, с сервисом для отправки СМС-сообщений "SMSC").
- Важное замечание: в коде бизнес-логики с этими классами/методами нельзя работать напрямую(исключение: процесс начальной инициализации приложения), необходимо создавать их экземпляры и помещать в $ /src/internal/instances.

$ /src/lib/utils
- Различные вспомогательные утилиты(например, утилита для генерации какой-нибудь рандомной строки по определённым правилам).
- Важное замечание: для работы с ними НЕ надо создавать экземпляры этих самых утилит, методы утилит можно вызывать напрямую из кода бизнес-логики.

===========================

app.py
- Исходный файл, являющийся "точкой входа" приложения.

requirements.txt
- Список модулей-зависимостей для установки через PIP.
```