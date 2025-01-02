import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.openvpn3_indicator")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        # Создаем простое окно
        window = Gtk.ApplicationWindow(application=app)
        window.set_title("OpenVPN3 Indicator")
        window.set_default_size(400, 300)

        # Создаем вертикальный контейнер
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        window.add(vbox)

        # Добавляем метку
        label = Gtk.Label(label="Управление OpenVPN3")
        vbox.pack_start(label, True, True, 0)

        # Кнопка для подключения
        connect_button = Gtk.Button(label="Подключиться")
        connect_button.connect("clicked", self.on_connect_clicked)
        vbox.pack_start(connect_button, True, True, 0)

        # Кнопка для отключения
        disconnect_button = Gtk.Button(label="Отключиться")
        disconnect_button.connect("clicked", self.on_disconnect_clicked)
        vbox.pack_start(disconnect_button, True, True, 0)

        # Показываем все виджеты в окне
        window.show_all()

    def on_connect_clicked(self, button):
        print("Подключение к VPN...")

    def on_disconnect_clicked(self, button):
        print("Отключение от VPN...")

    def run(self):
        # Запуск приложения
        super().run(None) 