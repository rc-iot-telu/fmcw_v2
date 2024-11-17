import pickle

from nicegui import ui

from fmcw.contrib import CARD_STYLE


@ui.page("/setting")
def settings_page():
    with ui.header():
        ui.label("Pengaturan Aplikasi")

    ui.button('Kembali', icon="arrow_back", on_click=lambda: ui.navigate.back())

    with ui.card().props(CARD_STYLE).classes("w-full"):
        with ui.grid(columns="auto").classes("w-full p-3"):

            ui.input(label='Nomor Port Radar', placeholder='COM3')
            ui.textarea(label='Daftar Port Terdeteksi')

            with ui.row():
                ui.button('Save Settings', icon="save")
                ui.button('Refresh Port', icon="refresh", color="gray")
