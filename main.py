from nicegui import app, ui

# app.native.window_args['resizable'] = False
app.native.start_args['debug'] = True
app.native.settings['ALLOW_DOWNLOADS'] = True

ui.add_css('''
    :root {
        --nicegui-default-: 0.5rem;
        --nicegui-default-gap: 3rem;
    }
''')


@ui.page("/")
def main_page():
    CARD_STYLE = "flat bordered"

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

                ui.button('Keluar', icon="close", on_click=lambda: app.shutdown(), color="gray")

        # Plot UI
        with ui.grid(columns=1, rows=2):
            with ui.card().props(CARD_STYLE):
                ui.label("Magnitude")

            with ui.card().props(CARD_STYLE):
                ui.label("Phase")

ui.run(
        native=True,
        reload=True,
        title='FMCW Radar | PUI-PT Intelligent Sensing-IoT',
)
