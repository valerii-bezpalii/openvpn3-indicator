import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .vpn_manager import start_vpn, stop_vpn, view_logs
from .config_selector import select_config

def create_tray_icon():
    tray = Gtk.StatusIcon()
    tray.set_from_icon_name("network-vpn")

    menu = Gtk.Menu()

    start_vpn_item = Gtk.MenuItem(label="Запустить VPN")
    start_vpn_item.connect("activate", start_vpn)
    menu.append(start_vpn_item)

    stop_vpn_item = Gtk.MenuItem(label="Остановить VPN")
    stop_vpn_item.connect("activate", stop_vpn)
    menu.append(stop_vpn_item)

    view_logs_item = Gtk.MenuItem(label="Посмотреть логи")
    view_logs_item.connect("activate", view_logs)
    menu.append(view_logs_item)

    select_config_item = Gtk.MenuItem(label="Выбрать конфигурацию")
    select_config_item.connect("activate", select_config)
    menu.append(select_config_item)

    menu.show_all()

    tray.connect("popup-menu", lambda icon, button, time: menu.popup(None, None, None, None, button, time))

    Gtk.main() 