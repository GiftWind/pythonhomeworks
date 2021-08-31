### Python homework 19
> Написать dns сервер.
    Сервер должен принимать соединения по протоколу udp.
    Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
    * Доп задание: иметь возможность переопределять записи клиентами:
    * ADD my.google.com:228.228.228.228

Сервер содержит упрощенные DNS записи в виде словаря {'hostname': 'address'}.
Сервер создает сокет, привязывает его к адресу и в непрерывном цикле считавает из него данные. Данные разбираются на запрос и адрес сокета, с которого этот запрос отправлен. Запрос обрабатывается, на адрес отправляется ответ. 
Если запись для hostname содержится в словаре, то отправлется значение по ключу hostname.
Если запись отсутствует, то адрес запрашивается с помощью метода ```socket.gethostbyname()``` из модуля socket, в словарь добавляется запись, адрес отправляется сокету, с которого поступил запрос.
Если в тексте запроса содержится ADD, то в словарь добавляется новая запись, либо переопределяется старая.
Все этапы работы сервера выводятся на консоль и сохраняются в лог.

#### Демонстрация:
Запросы от клиента:
![View from client](https://github.com/GiftWind/pythonhomeworks/blob/master/hw19/clients_console_view.jpg)

Работа сервера :
![Server console](https://github.com/GiftWind/pythonhomeworks/blob/master/hw19/server_console_view.jpg)
Аналогичные записи в логе:
> 2021-08-31 22:31:28
Server started.
===============
2021-08-31 22:31:56
Request from ('127.0.0.1', 42354): google.com
google.com was not found in hosts. Resolving...
Add record for google.com: 173.194.73.100
Send 173.194.73.100 to ('127.0.0.1', 42354)
===============
2021-08-31 22:32:09
Request from ('127.0.0.1', 39180): microsoft.com
microsoft.com was not found in hosts. Resolving...
Add record for microsoft.com: 40.112.72.205
Send 40.112.72.205 to ('127.0.0.1', 39180)
===============
2021-08-31 22:32:17
Request from ('127.0.0.1', 41651): aws.amazon.com
aws.amazon.com was not found in hosts. Resolving...
Add record for aws.amazon.com: 65.9.46.70
Send 65.9.46.70 to ('127.0.0.1', 41651)
===============
2021-08-31 22:32:42
Request from ('127.0.0.1', 44931): ADD my.google.com 228.228.228.228
Add new address 228.228.228.228 for my.google.com
===============
2021-08-31 22:32:51
Request from ('127.0.0.1', 42773): google.com
google.com was in hosts. Send 173.194.73.100 to ('127.0.0.1', 42773)
===============
2021-08-31 22:33:02
Request from ('127.0.0.1', 37831): my.google.com
my.google.com was in hosts. Send 228.228.228.228 to ('127.0.0.1', 37831)
===============
2021-08-31 22:33:19
Request from ('127.0.0.1', 45661): ADD microsoft.com 10.10.10.10
Add new address 10.10.10.10 for microsoft.com
===============
2021-08-31 22:33:24
Request from ('127.0.0.1', 36130): microsoft.com
microsoft.com was in hosts. Send 10.10.10.10 to ('127.0.0.1', 36130)
===============