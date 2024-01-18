from typing import List
from nicegui import ui


quote_classes = 'm-3 p-6 bg-blue-100 rounded-lg animate__animated animate__fadeInUp'
    quote_p_classes = 'font-serif italic text-lg text-gray-700 leading-snug mb-1'
    quote_span_classes = 'text-sm text-gray-500'

    def quot_row():
        with ui.element('div').classes('flex flex-row no-wrap'):
            def quoti(quot: str, auth: str):
                with ui.element('div').classes(quote_classes):
                    # exploded mapping or hashed map what do you call this?
                    ui.label(f"{quot}").classes(quote_p_classes)
                    ui.label(f"- {auth}").classes(quote_span_classes)

            quot_queue = [
                          ]

            auth_queue = [
                          ]

            for i in range(len(quot_queue)):
                quoti(quot_queue[i], auth_queue[i])
            # add to the row here with this template
            ui.html(f'''{row_html}''')
            # ui.html('<br>')  doesn't work

    quot_row()