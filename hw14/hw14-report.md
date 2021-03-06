### Python Homework 14

>  Создать сотрудника Mary, пользуясь классом Employee и перенести его в другую программу, используя модуль Pickle и файловую систему.
Узнать про + и - модуля Pickle.

hw14-from.py создает сотрудника и сохраняет на диск.
hw14-to.py считывает файл с диска и воссоздает объект сотрудника.

Попытка запуска hw14-to без предварительного запуска hw14-from приводит к FileNotFoundError.

Запуск hw14-from.py:
```
Employee Alice Wonderland gets 19999 Rubles
+7(999)999-9999
Alice Wonderland is FIRED!!!
```
На диске появляется файл alice.
Запуск hw14-to.py:
```
Employee Alice Wonderland gets 19999 Rubles
+7(999)999-9999
Alice Wonderland is FIRED!!!
```

Плюсы Pickle:
1. Входит в стандартную библиотеку Python.
2. Позволяет сериализовать и десериализовать пользовательские типы, а не только встроенные, как marshal и json.
3. Обратно совместим с предыдущими версиями Python (c Python 2 совместимы не все версии протоколов).
4. Отслеживает уже сериализованные объекты, что позволяет избежать повторной сериализации и позволяет сериализовать рекурсивные объекты.
5. Позволяет использовать сжатие, в результате чего сериализованные объекты занимают меньше места на диске.

Минусы Pickle:
1. Специфичен для Python, переносить данные в программы на других языках (как при использовании json) нельзя.
2. Формат сериализованного объекта не читается человеком.
3. Необходимо следить за соответствием версий используемых протоколов при сериализации и десериализации.
4. Не сериализует некоторые типы объектов (соединения с базами данных, открытые сокеты, лямбда-функции).
5. При сериализации встроенных типов Python работает медленнее json и marshal.
6. Позволяет выполнить произвольный код при десериализации объекта, включая выполнение команд os.system(), что является весьма небезопасным.