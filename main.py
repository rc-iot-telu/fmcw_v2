from nicegui import app, ui

app.native.start_args['debug'] = True
app.native.settings['ALLOW_DOWNLOADS'] = True

from fmcw.ui import *

ui.run(
        native=True,
        reload=True,
        title='FMCW Radar | PUI-PT Intelligent Sensing-IoT',
)
