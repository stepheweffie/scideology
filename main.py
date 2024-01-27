from nicegui import ui
import pandas as pd
from settings import main_font_size
import settings

df = pd.read_json('settings.json')
print(df.head())
setup = df[0]['Setup']
sans_serif = df[0]['Sans Serif']
sans_serif_link = df[0]['Sans Serif Link']
main_font = sans_serif
main_page_data = df[0]['Main Page Data']
head_html = df[0]['Head HTML']
pages = [df[0]['Page One'], df[0]['Page Two'], df[0]['Page Three']]
page_dict = {page.lower(): df[0]['Top Detail'] for page in pages}
app_name = df[0]['App Name']
app_title = df[0]['App Title']
serif_font = df[0]['Serif Font']
serif_font_family = df[0]['Serif Font Family']
serif_link = df[0]['Serif Link']
main_detail = df[0]['Main Detail']
top_detail = df[0]['Top Detail']
bottom_detail = df[0]['Bottom Detail']
bg_color = df[0]['Background Color']
head_links = df[0]['Head Links']
google_fonts = df[0]['Google Fonts']
font_size = df[0]['Font Size']
sans_serif_color = df[0]['Sans Serif Color']
serif_color = df[0]['Serif Color']
footer_classes = df[0]['Footer Classes']
footer_brand = df[0]['Footer Brand']
body_html = df[0]['Body HTML']


async def page_content(pagename: str):
    desc = ui.label(f'{page_dict[pagename.lower()]}').style(replace=f'font-family: {sans_serif};'
                                                                    f'color: {sans_serif_color}').classes('text-xl')
    with ui.row().classes('flex flex-row justify-center'):
        if pagename in pages:
            ui.label(f'{pagename}').style(replace=f'font-family: {serif_font_family}; font-size: {font_size}; '
                                                  f'color: {serif_color}')


async def page_body(pagename: str):
    if pagename in pages:
        ui.add_body_html(f'''{body_html}''')


async def page_footer(pagename: str):
    # footer is closed by default
    with ui.footer(value=True).classes(f'{footer_classes}').style(replace=f'color: {serif_color};'):
        with ui.column().classes('flex flex-row'):
            if pagename in pages:
                for page in pages:
                    with ui.column().classes('flex flex-row'):
                        ui.label(f'{page}').style(replace=f'font-family: {serif_font_family}; font-size: 3.5vw; color: light'
                                                          f'{serif_color}')
            if footer_brand is True:
                ui.label(f'{app_name}').style(replace=f'font-family: {serif_font_family}; font-size: 13.5vw; '
                                                      f'color: {serif_color}')


def menu_list(page_list_item):
    item = ui.menu_item(f'{page_list_item}', lambda: ui.open(f'{page_list_item.lower()}'), auto_close=True)
    item.classes('text-xl')


async def page_menu(pagename: str):
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
                    menu_list(page)
        ui.query('body').style(replace=f'background-color: {bg_color};')
        ui.image('static/images/Home.svg').style(replace='width: 100%; height: 100%;')
        ui.label(f'{main_page_data}').style(replace=f'font-family: {main_font}; font-size: {main_font_size}; '
                                                    f'color: {sans_serif_color}').classes('ml-5')


@ui.page('/setup')
async def settings_setup():
    await settings.setup()


ui.run(title=f'Scideology', storage_secret='secret_key', dark=False)
