from gi.repository import Gtk
import shutil
import os

def select_config(_):
    dialog = Gtk.FileChooserDialog(
        title="Выберите конфигурацию",
        action=Gtk.FileChooserAction.OPEN
    )
    dialog.add_buttons(
        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_OPEN, Gtk.ResponseType.OK
    )

    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        selected_file = dialog.get_filename()
        print(f"Выбранный файл: {selected_file}")

        # Директория для хранения конфигураций
        config_dir = os.path.expanduser("~/.vpn_configs/")
        os.makedirs(config_dir, exist_ok=True)

        # Копируем выбранный файл в директорию конфигураций
        try:
            shutil.copy(selected_file, config_dir)
            print(f"Файл скопирован в {config_dir}")
        except Exception as e:
            print(f"Ошибка при копировании файла: {e}")

    dialog.destroy() 