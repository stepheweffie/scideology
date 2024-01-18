from nicegui import ui
from settings import *


async def page_content(pagename: str):
    global page_dict
    desc = ui.label(f'{page_dict[pagename.lower()]}').style(replace=f'font-family: {sans_serif};'
                                                                    f'color: {font_color}').classes('text-xl')
    desc.classes('animate__animated animate__fadeInDown')
    with ui.row().classes('flex flex-row justify-center'):
        if pagename in pages:
            ui.label(f'{pagename}').style(replace=f'font-family: {font_family}; font-size: {font_size}; '
                                                  f'color: {font_color}')


async def page_body(pagename: str):
    if pagename in pages:
        ui.add_body_html(f'''{body_html}''')


async def page_footer(pagename: str):
    # footer is closed by default
    with ui.footer(value=True).classes(f'{footer_classes}').style(replace=f'color: {font_color};'):
        with ui.column().classes('flex flex-row'):
            if pagename in pages:
                for page in pages:
                    with ui.column().classes('flex flex-row'):
                        ui.label(f'{page}').style(replace=f'font-family: {font_family}; font-size: 3.5vw; color: light'
                                                          f'{font_color}')
            if footer_brand is True:
                ui.label(f'{app_name}').style(replace=f'font-family: {font_family}; font-size: 13.5vw; '
                                                      f'color: {font_color}')


async def page_menu(pagename: str):
    def menu_list(page_list_item):
        item = ui.menu_item(f'{page_list_item}', lambda: ui.open(f'{page_list_item.lower()}'), auto_close=True)
        item.classes('text-xl')

    with ui.row().classes('w-full h-full no-wrap top-0 left-0'):
        with ui.button(icon='menu', color='#737373').classes('absolute top-0 right-0 m-3 p-3 rounded-full'):
            with ui.menu() as menu:
                for page in pages:
                    if page != pagename:
                        menu_list(page)
                ui.separator()
                home = ui.menu_item('Home', on_click=lambda: ui.open(f'/'))
                home.classes('text-xl')


async def generate_content(pagename: str):
    # call a function to get the content
    await page_menu(pagename)
    await page_content(pagename)
    await page_body(pagename)
    await page_footer(pagename)


async def page_iter(page_name):
    if page_name in pages:
        # Create a page for each item in pages
        @ui.page(f'/{page_name.lower()}')
        async def dynamic_page():
            await generate_content(page_name)
    else:
        return ui.label(f'Page {page_name} not found in menu.')


@ui.page('/')
async def main():
    # Styling and fonts
    ui.add_head_html(f'''
    {head_html}
    ''')

    for page in pages:
        await page_iter(page)

    with ui.row().classes('w-full h-full top-0 left-0 justify-end'):
        with ui.button(icon='menu', color='#737373').classes('relative top-0 m-3 p-3 rounded-full'):
            with ui.menu() as menu:
                menu.classes(f'text-xl')
                for page in pages:
                   ui.menu_item(f'{page}', lambda: ui.open(f'{page.lower()}'), auto_close=True)
        ui.query('body').style(replace=f'background-color: {bg_color};')
        ui.image('static/images/Home.svg').style(replace='width: 100%; height: 100%;')
        ui.label(f'{main_page_data}').style(replace=f'font-family: {main_font}; font-size: {main_font_size}; '
                                                    f'color: {font_color}').classes('ml-5')

ui.run(title=f'{title}', storage_secret='secret_key', dark=False)
