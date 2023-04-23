from datetime import datetime, timedelta

# Считываем лог из файла
filename = input("Введи название файла логов (должен быть в директории с проектом): ")
with open(filename, "r", encoding="utf-8") as f:
    log_lines = f.readlines()

# Словарь для хранения количества активных сессий в каждый момент времени
sessions_dict = {}

# Проходим по всем строкам лога
for line in log_lines:
    # Извлекаем дату и время из строки лога
    date_str = line.split()[0]
    time_str = line.split()[1]
    datetime_str = date_str + " " + time_str
    log_datetime = datetime.strptime(datetime_str, "%H:%M:%S.%f %w")

    # Извлекаем идентификатор сессии из строки лога
    session_id = line.split()[3]

    # Если это начало сессии, добавляем идентификатор в словарь сессий
    if "logged in" in line or "connected" in line:
        if log_datetime not in sessions_dict:
            sessions_dict[log_datetime] = set()
        sessions_dict[log_datetime].add(session_id)
    # Если это завершение сессии, удаляем идентификатор из словаря сессий
    elif "closed" in line or "disconnected" in line:
        if log_datetime in sessions_dict:
            sessions_dict[log_datetime].discard(session_id)

# Находим период максимальной активности
max_sessions_count = 0
max_sessions_period_start = None
max_sessions_period_end = None

current_sessions_count = 0
current_period_start = None
current_period_end = None

for log_datetime, sessions_set in sorted(sessions_dict.items()):
    if current_period_start is None:
        current_period_start = log_datetime

    current_sessions_count += len(sessions_set)

    if current_sessions_count > max_sessions_count:
        max_sessions_count = current_sessions_count
        max_sessions_period_start = current_period_start
        max_sessions_period_end = log_datetime

    if len(sessions_set) == 0:
        current_period_end = log_datetime
        print(f"{current_period_start} - {current_period_end}: {current_sessions_count} sessions")
        current_sessions_count = 0
        current_period_start = None
        current_period_end = None

# Выводим период максимальной активности
print(f"Max sessions count: {max_sessions_count}")
print(f"Max sessions period: {max_sessions_period_start} - {max_sessions_period_end}")
input("Нажмите Enter для выхода")