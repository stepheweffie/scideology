from nicegui import ui, app
import pandas as pd
import settings
from dotenv import load_dotenv

import os
from pathlib import Path
import affiliate
import requests

load_dotenv()
instructions_url = os.getenv('INSTRUCTIONS')

packages = Path('packages')
packages.mkdir(exist_ok=True)

static = Path('static')
static.mkdir(exist_ok=True)
app.add_static_files('/static', static)

fonts = Path('static/fonts')
fonts.mkdir(exist_ok=True)

images = Path('static/images')
images.mkdir(exist_ok=True)

videos = Path('static/videos')
images.mkdir(exist_ok=True)

media = Path('media')
media.mkdir(exist_ok=True)
app.add_media_files('/media', media)

uploads = Path('media/uploads')
uploads.mkdir(exist_ok=True)

instructions_url = f'{instructions_url}'
r = requests.get(f'{instructions_url}')
(media / 'instructions.mp4').write_bytes(r.content)

secret_key = os.getenv('SECRET_KEY')

df = pd.read_json('settings.json')

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
trailer = df[0]['Trailer']


async def page_content(pagename: str):
    desc = ui.label(f'{page_dict[pagename.lower()]}').style(replace=f'font-family: {sans_serif};'
                                                                    f'color: {sans_serif_color}').classes('text-xl')
    with ui.row().classes('flex flex-row justify-center'):
        if pagename in pages:
            ui.label(f'{pagename}').style(replace=f'font-family: {serif_font}; font-size: {font_size}; '
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
                        ui.label(f'{page}').style(replace=f'font-family: {serif_font}; font-size: 3.5vw; color: light'
                                                          f'{serif_color}')
            if footer_brand is True:
                ui.label(f'{app_name}').style(replace=f'font-family: {serif_font}; font-size: {font_size}; '
                                                      f'color: {serif_color}')


def menu_list(page_list_item):
    item = ui.menu_item(f'{page_list_item}', lambda: ui.open(f'{page_list_item.lower()}'), auto_close=True)
    item.classes('text-xl')


async def page_menu(pagename: str):
    with ui.row().classes('w-full h-full no-wrap top-0 left-0'):
        with ui.button(icon='menu', color=f'{serif_color}').classes('absolute top-0 right-0 m-3 p-3 rounded-full'):
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
    # Enable Security Lock by default before setup
    # Check for serve STATIC_SITE
    serve_static_site = os.getenv('STATIC_SITE')
    if serve_static_site is True:
        ui.open('/setup/assets')

    await settings.create_setup()
    if setup is False:
        ui.open('/setup')

    # Styling and fonts
    ui.add_head_html(f'''
    {head_html}
    ''')

    for page in pages:
        await page_iter(page)

    header_image = os.listdir('static/images')[0]

    with ui.row().classes('w-full h-full top-0 left-0 justify-end'):
        with ui.button(icon='menu', color=f'{serif_color}').classes('relative top-0 m-3 p-3 rounded-full'):
            with ui.menu() as menu:
                menu.classes(f'text-xl')
                for page in pages:
                    menu_list(page)

        ui.query('body').style(replace=f'background-color: {bg_color};')
        ui.image(f'static/images/{header_image}').style(replace='width: 100%; height: 100%;')
        # ui.label(f'{main_page_data}').style(replace=f'font-family: {main_font}; font-size: {main_font_size}; '
        #                                            f'color: {sans_serif_color}').classes('ml-5')
        if setup is False:
            with ui.row():
                ui.video('/media/instructions.mp4')
        if trailer is True:
            with ui.row():
                ui.video('/media/trailer.mp4')


@ui.page('/affiliate')
async def affiliate_page():
    await affiliate.affiliate()


ui.run(title=f'{app_title}', storage_secret=f'{secret_key}', dark=False)
