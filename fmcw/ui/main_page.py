from nicegui import app, ui

from fmcw.contrib import CARD_STYLE

from .settings_page import settings_page

@ui.page("/")
def main_page():

    with ui.header():
        ui.label("Pengambilan Data")

    with ui.grid(columns="auto 1fr").classes("absolute-full m-3"):

        # Control panel
        with ui.card().props(CARD_STYLE):
            with ui.column().classes("h-full"):
                ui.label("Control Panel")

                ui.button('Start Radar', icon="play_arrow")
                ui.button('Stop Radar', color="red", icon="stop").set_enabled(False)
                ui.button('Save Data', icon="save").set_enabled(False)
                ui.space()

                ui.button('Settings', icon="settings", on_click=lambda: ui.navigate.to(settings_page))
                ui.button('Keluar', icon="close", on_click=lambda: app.shutdown(), color="gray")

        # Plot UI
        with ui.grid(columns=1, rows=2):
            with ui.card().props(CARD_STYLE):
                ui.label("Magnitude")

            with ui.card().props(CARD_STYLE):
                ui.label("Phase")


