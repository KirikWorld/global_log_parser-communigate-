Для работы с парсером нужно закинуть файл с логом в директорию с exe программы (по умолчанию exe находится в папке dist)


Алгоритм решения задачи:

1. Считываем лог-файл построчно.
2. Для каждой строки используем регулярное выражение, чтобы извлечь следующую информацию: момент времени, идентификатор сессии и тип сессии (XIMSS или IMAP).
3. Если сессия является XIMSS, то добавляем идентификатор в словарь сессий, если сессия является IMAP, то удаляем идентификатор из словаря.
4. Для каждого момента времени сортируем идентификаторы сессий по типу сессии и по времени их начала/завершения.
5. Для каждого момента времени считаем количество активных сессий каждого типа и выводим результат.
6. В процессе подсчета сохраняем информацию о максимальном количестве активных сессий и соответствующих моментах времени.

Заивисимостей нет, в качестве упаковщика использован pyinstaller

<h1>Отчет в файле C1.pdf</h1>
