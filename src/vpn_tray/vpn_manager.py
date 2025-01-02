import subprocess
import os

def start_vpn(_):
    config_dir = os.path.expanduser("~/.vpn_configs/")
    config_file = os.path.join(config_dir, "example.ovpn")  # Замените на логику выбора файла

    if not os.path.exists(config_file):
        print(f"Конфигурационный файл {config_file} не найден.")
        return

    try:
        # Запуск openvpn3
        subprocess.run(["openvpn3", "session-start", "--config", config_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске VPN: {e}")

def stop_vpn(_):
    try:
        # Остановка openvpn3
        subprocess.run(["openvpn3", "session-manage", "--disconnect"], check=True)
        print("VPN-сессия остановлена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при остановке VPN: {e}")

def view_logs(_):
    try:
        # Просмотр логов openvpn3
        result = subprocess.run(["openvpn3", "log", "list"], capture_output=True, text=True, check=True)
        print("Логи VPN-сессии:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при просмотре логов: {e}") 