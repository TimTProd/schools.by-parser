# schools.by-parser
Этот скрипт на питоне парсит отметки с schools.by и выводит их в виде таблицы

- [Как сделать что бы всё работало](#как-сделать-что-бы-всё-работало)
- [Конфигурация файла четверть.txt](#конфигурация-файла-четвертьtxt)

## Authors

- [TimTProd](https://github.com/TImTProd)


## Как сделать что бы всё работало
- изначально у вас должен быть установлен python
1. Cкопируйте репозиторий: `git clone https://github.com/TImTProd/schools.by-parser.git`
2. Зайдите в папку репозитория: `cd schools.by-parser`
3. Затем надо скачать **virtualenv** с помощью **pip**: 
- на Windows: `py -m pip install --user virtualenv`
- на UNIX/macOS: `python3 -m pip install --user virtualenv`
4. Создаем окружение:
- на Windows: `py -m venv venv`
- на UNIX/macOS: `python3 -m venv venv`
5. Активируем окружение:
- на Windows: `.\env\Scripts\activate`
- на UNIX/macOS: `source env/bin/activate`
6. Теперь надо проверить, активировалось оно:
- на Windows: делаем команду `where python`, должно вывести `...\venv\Scripts\python.exe`
- на UNIX/macOS: делаем команду `which python`, должно вывести `.../env/bin/python`
7. Теперь мы можем установить библиотеки:
- на Windows: `py -m pip install -r requirements.txt` **или** *(если не работает прошлое)*:
    ```
    py -m pip install mechanize
    py -m pip install bs4
    py -m pip install rich
    ```
- на UNIX/macOS: `python3 -m pip install -r requirements.txt` **или** *(если не работает прошлое)*:
    ```
    py -m pip install mechanize
    py -m pip install bs4
    py -m pip install rich
    ```
<!-- end of the list -->
## Конфигурация файла четверть.txt
- 1 строка: год начала четверти
- 2 строка: месяц начала четверти (без 0 в начале)
- 3 строка: день начала четверти (без 0 в начале)
- 4 строка: id четверти
- 5 строка: id шкильника
- 6 строка: логин
- 7 строка: пароль
<!-- end of the list -->
**Для 2 и 3 строки: если четверть начинается, например, в апреле, а это 4 месяц года, то надо указывать не 04, а просто 4, то же самое и с днями.**
<!-- end of the list -->
**Для 4 строки:**
чтобы узнать, какой id у данной четверти, нужно сделать следующее:
1. Открываем консоль на дневнике *(если не знаете как то загуглите)*:
<img src="https://github.com/TImTProd/schools.by-parser/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-16%20%D0%B2%2015.12.43.png">
2. Нажимаем на эту кнопку:
<img src="https://github.com/TImTProd/schools.by-parser/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-16%20%D0%B2%2015.12.431.png">
3. Наводим курсор на стрелочку переключения недели и нажимаем на нее:
<img src="https://github.com/TImTProd/schools.by-parser/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-16%20%D0%B2%2015.22.28.png">
4. Смотрим id четверти:
<img src="https://github.com/TImTProd/schools.by-parser/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-16%20%D0%B2%2015.27.32.png">
<!-- end of the list -->

**Для 5 строки:** id можно узнать в адресной строке на профиле:
![ссылка](https://github.com/TImTProd/schools.by-parser/blob/main/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-06-16%20%D0%B2%2015.51.56.png)

