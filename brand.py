from nicegui import ui

ui.query('body').style(replace=f'background-color: {bg_color};')
    with ui.element('div').classes('flex flex-col justify-center h-screen'):
        with ui.row().classes('flex flex-row justify-end'):
            ui.label(f'{app_name}').style(replace=f'font-family: {font}, serif; font-size: 13.5vw; color: '
                                                  f'{font_color};').classes(' animate__animated '
                                                                            'animate__fadeInDown')
