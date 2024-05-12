
import nmap


def scan_network(target):
    """Функция для выполнения сканирования сети с использованием nmap."""
    nm = nmap.PortScanner(
        '/Users/nntspector/desktop/ИБ/nmap')  # Укажите путь к исполняемому файлу nmap
    nm.scan(hosts=target, arguments='-sP')  # Сканирование Ping (-sP)
    return nm.all_hosts()


def main():
    target = input(
        "Введите целевую сеть для сканирования (например, '192.168.1.0/24'): ")
    print(f"Выполняется сканирование сети {target}...")
    hosts = scan_network(target)
    if hosts:
        print("Найденные устройства в сети:")
        for host in hosts:
            print(host)
    else:
        print("Нет обнаруженных устройств в сети.")


if __name__ == "__main__":
    main()
