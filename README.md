# schools.by-parser
Этот скрипт на питоне парсит отметки с schools.by и выводит их в виде таблицы

## Authors

- [TimTProd](https://github.com/TImTProd)


## Как сделать шобы работало
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
### Конфигурация файла четверть.txt
- 1 строка: год начала четверти
- 2 строка: месяц начала четверти (без 0 в начале)
- 3 строка: день начала четверти (без 0 в начале)
- 4 строка: id четверти
- 5 строка: id шкильника
- 6 строка: логин
- 7 строка: пароль
<!-- end of the list -->
**Для 2 и 3 строки: если четверть начинается, например, в апреле, а это 4 месяц года, то надо указывать не 04, а просто 4, то же самое и с днями.**
**Для 4 строки:**
чтобы узнать, какой id у данной четверти, нужно сделать следующее:
1. Открываем консоль на дневнике *(если не знаете как то загуглите)*:
- ![консоль](/images/Снимок экрана 2022-06-16 в 15.12.43.png)
2. Нажимаем на эту кнопку:
- картинка 
3. Наводим и нажимаем на стрелочку переключения недели:
- картинка
4. Смотрим id:
- картинка
<!-- end of the list -->
**Для 5 строки:** id можно узнать в адресной строке на профиле:
- картинка

