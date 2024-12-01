import re
import statistics
from typing import List

# Сворованный из интернета шаблон для парсинга строк логов Nginx
log_pattern = re.compile(r'(?P<remote_addr>[\d\.]+) - - \[(?P<time>[^\]]+)\] "(?P<method>\w+) (?P<url>[^\s]+) HTTP/[\d\.]+" (?P<status>\d{3}) (?P<body_bytes_sent>\d+)')

# Массив времени ответа
response_times: List[int] = []

# Чтение и парсинг файла
with open('access.log') as log_file:
    for line in log_file:
        match = log_pattern.match(line)
        if match:
            response_time = int(match.group('body_bytes_sent'))
            response_times.append(response_time)

# Вычисление статистики
if response_times:
    average_time: float = statistics.mean(response_times)  # pylint: disable=invalid-name
    median_time: float = statistics.median(response_times) # pylint: disable=invalid-name
    max_time: int = max(response_times)  # pylint: disable=invalid-name
    min_time: int = min(response_times)  # pylint: disable=invalid-name
else: average_time = median_time = max_time = min_time = 0

print(f"Среднее время ответа: {average_time}", "мс")
print(f"Медианное время ответа: {median_time}", "мс")
print(f"Максимальное время ответа: {max_time}", "мс")
print(f"Минимальное время ответа: {min_time}", "мс")
