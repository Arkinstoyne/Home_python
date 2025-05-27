import datetime

# Получаем текущий datetime (имитация получения из API)
dt = datetime.datetime.now()
print("Текущая дата и время:", dt)

# Получаем отдельные компоненты даты
print("Год, месяц, день:", dt.year, dt.month, dt.day)

# Получаем отдельные компоненты времени
print("Час, минута, секунда:", dt.hour, dt.minute, dt.second)

# Получаем объект даты
print("Объект даты:", dt.date())

# Получаем объект времени
print("Объект времени:", dt.time())

# Преобразуем datetime в timestamp (секунды с плавающей точкой)
second = dt.timestamp()
print("Timestamp (секунды с долями):", second)

# Преобразуем timestamp в int (без долей)
print("Timestamp (int):", int(second))

# Преобразуем обратно из секунд в datetime
dt_from_sec = datetime.datetime.fromtimestamp(second)
print("Datetime из timestamp:", dt_from_sec)

# Получаем строку из datetime в формате дд.мм.гггг чч:мм
print("Строка из datetime:", dt_from_sec.strftime('%d.%m.%Y %H:%M'))

# Считаем сколько дней до 1 января 2026
future_dt = datetime.datetime.strptime('01.01.2026', '%d.%m.%Y')
delta = future_dt - dt
print("Дней до 01.01.2026:", delta.days)

# Получаем объект datetime из date и time + интервал
date_today = datetime.date.today()
time_obj = datetime.time(23, 55)
delta_30min = datetime.timedelta(minutes=30)
combined_dt = datetime.datetime.combine(date_today, time_obj) + delta_30min
print("Объединение date и time + 30 минут:", combined_dt)

# Преобразование строки с датой в объект datetime
date_str1 = 'Fri, 24 Apr 2021 16:22:54 +0000'
format1 = '%a, %d %b %Y %H:%M:%S +0000'
dt_parsed1 = datetime.datetime.strptime(date_str1, format1)
print("Парсим строку даты #1:", dt_parsed1)

date_str2 = '24.12.2020 16:22'
format2 = '%d.%m.%Y %H:%M'
dt_parsed2 = datetime.datetime.strptime(date_str2, format2)
print("Парсим строку даты #2:", dt_parsed2)

# Подсчет дней до события 6 декабря 2024 (пример)
today = datetime.datetime.now()
event_date = datetime.datetime(2024, 12, 6)
delta_event = event_date - today
print("Дней до 06.12.2024:", delta_event.days)

# Дата через 3 недели и 5 дней
delta_ws = datetime.timedelta(weeks=3, days=5)
date_ws = today + delta_ws
print("Дата через 3 недели и 5 дней:", date_ws.day, date_ws.month, date_ws.year)

# Дата 100 дней назад
delta_100d = datetime.timedelta(days=100)
date_100d_ago = today - delta_100d
print("Дата 100 дней назад:", date_100d_ago.day, date_100d_ago.month, date_100d_ago.year)

# Время через 1 час 30 минут и 45 секунд
delta_time = datetime.timedelta(hours=1, minutes=30, seconds=45)
date_plus_time = today + delta_time
print("Время через 1ч 30м 45с:", date_plus_time.hour, date_plus_time.minute, date_plus_time.second)
