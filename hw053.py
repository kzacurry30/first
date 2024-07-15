import sys
import os

def parse_log_line(line):

    parts = line.split(' ', 3)
    if len(parts) < 4:
        return None
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path):

    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
    return logs

def filter_logs_by_level(logs, level):

    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs):

    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts):

    print("Статистика за рівнями логування:")
    for level, count in counts.items():
        print(f"{level}: {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python log_analyzer.py <шлях до файлу> [<рівень логування>]")
        return

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(file_path):
        print(f"Файл не знайдено: {file_path}")
        return

    logs = load_logs(file_path)
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()
