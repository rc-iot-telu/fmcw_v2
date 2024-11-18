import pickle
from turtle import onclick

from nicegui import ui

from serial.tools.list_ports import comports

from fmcw.contrib import (
    CARD_STYLE, DB_PATH,
    SETTING_FILE_NAME, read_setting
)


def save_setting(data: dict):
    with open(DB_PATH.joinpath(SETTING_FILE_NAME), "wb") as f:
        pickle.dump(data, f)

    ui.notify("Berhasil Menyimpan Setting")


def list_com_port(get_first_port: bool = False) ->  str:
    """
    Scan all COM port available on the device,
    and return it as a string
    """
    ports = comports()

    if not ports:
        return "Tidak ada port yang terdeteksi!"

    ports = ["{}: {} [{}]\n".format(port, desc, hwid) for port, desc, hwid in sorted(ports)]
    ports = "".join(ports)

    if not get_first_port:
        return ports

    return ports.split(":")[0]



@ui.page("/setting")
def settings_page():
    settings_data = read_setting()
    ports_number = {"LIST_ALL_COM_PORT": list_com_port()}

    with ui.header():
        ui.label("Pengaturan Aplikasi")

    ui.button('Kembali', icon="arrow_back", on_click=lambda: ui.navigate.back())

    with ui.card().props(CARD_STYLE).classes("w-full"):
        with ui.grid(columns="auto").classes("w-full p-3"):

            ui.input(
                    label='Nomor Port Radar',
                    placeholder='COM3',
                    on_change=lambda e: settings_data.update({"PORT_NUMBER": e.value})
            ).bind_value(settings_data, "PORT_NUMBER")

            ui.textarea(
                    label='Daftar Port Terdeteksi',
                    value="Tidak ada port yang terdeteksi!"
            ).bind_value(ports_number, "LIST_ALL_COM_PORT")

            with ui.row():
                ui.button('Save Settings', icon="save", on_click=lambda: save_setting(settings_data))
                ui.button('Refresh Port', icon="refresh", color="gray", on_click=lambda: ports_number.update({"LIST_ALL_COM_PORT": list_com_port()}))
