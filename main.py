# created by TimTProd(GitHub) on 2021 - 2022
"""
Парсер отметок с сайта schools.by
=================================================
Библиотеки: mechanize
            bs4 (BeautifulSoup4)
            rich
Все эти библиотеки есть на PyPI

Еще нужен файл "Четверть.txt" в директории проекта со следующим содержанием:
            1 строка: год начала четверти
            2 строка: месяц начала четверти (без 0 в начале)
            3 строка: день начала четверти (без 0 в начале)
            4 строка: id четверти
            5 строка: id шкильника
            6 строка: логин
            7 строка: пароль
=================================================
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from datetime import datetime

from rich.console import Console
from rich.table import Table
from bs4 import BeautifulSoup
from mechanize import Browser

console = Console()

with console.status("[bold red]In process...") as status:
    # начало четверти
    file = open('Четверть.txt', 'r')
    filel = file.readlines()
    yearq = int(filel[0].strip())
    monthq = int(filel[1].strip())
    dayq = int(filel[2].strip())
    quarter = filel[3].strip()
    userID = filel[4].strip()
    login = filel[5].strip()
    password = filel[6].strip()
    yearqp = int(filel[8].strip())
    monthqp = int(filel[9].strip())
    dayqp = int(filel[10].strip())
    quarterp = int(filel[11].strip())

    pastLessons = []
    it = 12
    t = filel[it].strip()
    while t != "0":
        it += 1
        pastLessons.append(t)
        t = filel[it].strip()

    file.close()
    # импорт печенек
    # import http.cookiejar
    console.log('[chartreuse3]Logging in...')
    status.update(spinner='dots12')
    br = Browser()  # создание браузера
    # печеньки
    # cj = http.cookiejar.LWPCookieJar()
    # br.set_cookiejar(cj)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Version/11.1.2 Safari/605.1.15')]
    br.set_handle_robots(False)  # обход robots.txt
    br.open('https://schools.by/login')
    # форма с логином
    br.select_form(nr=0)
    br.form["username"] = login  # логин
    br.form["password"] = password  # пароль
    br.submit()  # отправка
    """ ПАРСЕР """

    # месяцы
    monthlength = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # дата сегодня
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day


    def openurl(d, m, yr, q):
        x = str(d)
        if len(x) == 1:
            x = '0' + x
        y = str(m)
        if len(y) == 1:
            y = '0' + y
        br.open(
            f"https://gymn31.schools.by/pupil/{userID}/dnevnik/quarter/{q}/week/{yr}-{y}-{x}")


    openurl(dayqp, monthqp, yearqp, quarterp)
    # br.factory.encoding = 'utf8_encoding'

    Русяз = []
    Руслит = []
    Физкизд = []
    Матем = []
    Англяз = []
    Трудобуч = []
    Искусство = []
    Биология = []
    Всемирист = []
    География = []
    Химия = []
    Физика = []
    Беляз = []
    Беллит = []
    ИстБел = []
    Информ = []
    Обществов = []
    ЧЗС = []

    console.log('[chartreuse3]Collecting marks...')


    def readweekmarks(ispast):
        b = 0
        remove_digits = str.maketrans('', '', '1234567890.')
        bsoup = BeautifulSoup(br.response(), 'html5lib', from_encoding="utf8")
        days = bsoup.find_all('div', class_='db_day')
        for i in days:
            trs = i.find_all('tr')
            for tr in trs:
                marks = tr.find_all('div', class_='mark_box')
                lessons = tr.find_all('td', class_='lesson')
                for lesson in lessons:
                    a = lesson.text.strip().replace(' ', '').translate(remove_digits)
                    for mark in marks:
                        b = mark.text.strip()
                    if len(b) != 0:
                        if 'Русяз' in a:
                            if not ispast or ('Русяз' in pastLessons):
                                Русяз.append(b)
                        elif 'Руслит' in a:
                            if not ispast or ('Руслит' in pastLessons):
                                Руслит.append(b)
                        elif 'Физкизд' in a:
                            if not ispast or ('Физкизд' in pastLessons):
                                Физкизд.append(b)
                        elif 'Матем' in a:
                            if not ispast or ('Матем' in pastLessons):
                                Матем.append(b)
                        elif 'Англяз' in a:
                            if not ispast or ('Англяз' in pastLessons):
                                Англяз.append(b)
                        elif 'Трудобуч' in a:
                            if not ispast or ('Трудобуч' in pastLessons):
                                Трудобуч.append(b)
                        elif 'Искусство' in a:
                            if not ispast or ('Искусство' in pastLessons):
                                Искусство.append(b)
                        elif 'Биология' in a:
                            if not ispast or ('Биология' in pastLessons):
                                Биология.append(b)
                        elif 'Всемирист' in a:
                            if not ispast or ('Всемирист' in pastLessons):
                                Всемирист.append(b)
                        elif 'География' in a:
                            if not ispast or ('География' in pastLessons):
                                География.append(b)
                        elif 'Химия' in a:
                            if not ispast or ('Химия' in pastLessons):
                                Химия.append(b)
                        elif 'Физика' in a:
                            if not ispast or ('Физика' in pastLessons):
                                Физика.append(b)
                        elif 'Беляз' in a:
                            if not ispast or ('Беляз' in pastLessons):
                                Беляз.append(b)
                        elif 'Беллит' in a:
                            if not ispast or ('Беллит' in pastLessons):
                                Беллит.append(b)
                        elif 'ИстБел' in a:
                            if not ispast or ('ИстБел' in pastLessons):
                                ИстБел.append(b)
                        elif 'Информ' in a:
                            if not ispast or ('Информ' in pastLessons):
                                Информ.append(b)
                        elif 'Обществов' in a:
                            if not ispast or ('Обществов' in pastLessons):
                                Обществов.append(b)
                        else:
                            ЧЗС.append(b)


    while True:
        # noinspection PyBroadException
        try:
            if dayqp <= monthlength.get(int(monthqp)):
                openurl(dayqp, monthqp, yearqp, quarterp)
                readweekmarks(True)
                dayqp += 7
            else:
                dayqp = (dayqp - monthlength.get(int(monthqp)))
                monthqp += 1
        except:
            break

    while True:
        # noinspection PyBroadException
        try:
            if dayq <= monthlength.get(int(monthq)):
                openurl(dayq, monthq, yearq, quarter)
                readweekmarks(False)
                dayq += 7
            else:
                dayq = (dayq - monthlength.get(int(monthq)))
                monthq += 1
        except:
            break


    def av(x):
        a = 0
        temp = 0
        for i in x:
            if len(i) > 2:
                i = i.split('/')
                for y in i:
                    a += int(y)
                temp += 1
            else:
                a += int(i)
        if len(x) != 0:
            if (a / (len(x) + temp)) % 1 == 0:
                return int(a / (len(x) + temp))
            else:
                return a / (len(x) + temp)
        else:
            return ''


    def vav(x):
        if x != '':
            return int(x + 0.5)
        else:
            return ''


    def listext(x):
        a = ''
        for i in x:
            a = a + i + ' '
        return a


    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def count_min(x, y):
        if x == '':
            return ''
        elif isfloat(x):
            if x - int(x) == 0.5:
                return round(1 + int(x))
            else:
                mark = x
                sumt = mark * y + 11
                out = 11
                while round(mark) <= round(sumt / (y + 1)):
                    out -= 1
                    sumt = mark * y + out
                return out + 1
        else:
            mark = x
            sumt = mark * y + 11
            out = 11
            while round(mark) <= round(sumt / (y + 1)):
                out -= 1
                sumt = mark * y + out
            return out + 1


    table = Table(row_styles=['on grey19', ''])
    table.add_column('Урок', justify='left', style='cyan', no_wrap=True)
    table.add_column('Средняя(окр.)', style='bold bright_red')
    table.add_column('Отметки', style='green', justify='left')
    table.add_column('Мин. Отм.', style='green')
    table.add_column('Средняя', style='white')

    table.add_row('Русяз', str(vav(av(Русяз))), listext(Русяз), str(count_min(av(Русяз), len(Русяз))), str(av(Русяз)))
    table.add_row('Руслит', str(vav(av(Руслит))), listext(Руслит), str(count_min(av(Руслит), len(Руслит))),
                  str(av(Руслит)))
    table.add_row('Физкизд ', str(vav(av(Физкизд))), listext(Физкизд), str(count_min(av(Физкизд), len(Физкизд))),
                  str(av(Физкизд)))
    table.add_row('Матем', str(vav(av(Матем))), listext(Матем), str(count_min(av(Матем), len(Матем))), str(av(Матем)))
    table.add_row('Англяз', str(vav(av(Англяз))), listext(Англяз), str(count_min(av(Англяз), len(Англяз))),
                  str(av(Англяз)))
    table.add_row('Трудобуч', str(vav(av(Трудобуч))), listext(Трудобуч), str(count_min(av(Трудобуч), len(Трудобуч))),
                  str(av(Трудобуч)))
    table.add_row('Искусство', '', listext(Искусство))
    table.add_row('Биология', str(vav(av(Биология))), listext(Биология), str(count_min(av(Биология), len(Биология))),
                  str(av(Биология)))
    table.add_row('Всемирист', str(vav(av(Всемирист))), listext(Всемирист),
                  str(count_min(av(Всемирист), len(Всемирист))), str(av(Всемирист)))
    table.add_row('География', str(vav(av(География))), listext(География),
                  str(count_min(av(География), len(География))), str(av(География)))
    table.add_row('Химия', str(vav(av(Химия))), listext(Химия), str(count_min(av(Химия), len(Химия))), str(av(Химия)))
    table.add_row('Физика', str(vav(av(Физика))), listext(Физика), str(count_min(av(Физика), len(Физика))),
                  str(av(Физика)))
    table.add_row('Беляз', str(vav(av(Беляз))), listext(Беляз), str(count_min(av(Беляз), len(Беляз))), str(av(Беляз)))
    table.add_row('Беллит', str(vav(av(Беллит))), listext(Беллит), str(count_min(av(Беллит), len(Беллит))),
                  str(av(Беллит)))
    table.add_row('ИстБел', str(vav(av(ИстБел))), listext(ИстБел), str(count_min(av(ИстБел), len(ИстБел))),
                  str(av(ИстБел)))
    table.add_row('Информ', str(vav(av(Информ))), listext(Информ), str(count_min(av(Информ), len(Информ))),
                  str(av(Информ)))
    table.add_row('Обществов', str(vav(av(Обществов))), listext(Обществов),
                  str(count_min(av(Обществов), len(Обществов))), str(av(Обществов)))
    table.add_row('ЧЗС', str(vav(av(ЧЗС))), listext(ЧЗС), str(count_min(av(ЧЗС), len(ЧЗС))), str(av(ЧЗС)))
    console.log('[chartreuse3]Done!')
console.print(table)
