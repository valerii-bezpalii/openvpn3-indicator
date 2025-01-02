from openvpn3_indicator.application import Application
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
import subprocess

def create_tray_icon():
    app = QApplication([])

    # Создаем иконку в трее
    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon("icon.png"))  # Убедитесь, что у вас есть иконка

    # Создаем меню
    menu = QMenu()

    # Добавляем пункт меню для запуска VPN
    start_vpn_action = QAction("Запустить VPN")
    start_vpn_action.triggered.connect(start_vpn)
    menu.addAction(start_vpn_action)

    # Добавляем другие пункты меню, если необходимо
    # ...

    # Устанавливаем меню для иконки
    tray_icon.setContextMenu(menu)

    # Показываем иконку
    tray_icon.show()

    app.exec_()

def start_vpn():
    try:
        # Запуск openvpn3
        subprocess.run(["openvpn3", "session-start", "--config", "your-config.ovpn"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске VPN: {e}")

if __name__ == "__main__":
    create_tray_icon()

