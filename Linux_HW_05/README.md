В данной директории расположены python и bash скрипты.

Python script определяет директории в которой находится access.log
Шаблоны поиска регулярных выражений присвоены переменным regex1-4
Количество запросов ищем открытием файла и применением шаблона поиска, количество найденный совпадений 
прибавляем к переменными all, get, post, put и записываем в файл с помощью контекстного менеджера.

Bash скрипт использует регулярные выражения grep и подсчётом количества совпадений по линиям или словам с помощью 
ключа wc, первая строка перезаписывает новый файл, все последующие добавляют новые строки.

Bash скрипт на выходе записывает файл 'output.txt'
Python скрипт на выходе записывает файл 'export.txt'
Файлы сохраняются в ту же директорию в которой они расположены.