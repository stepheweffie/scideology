from nicegui import ui
from dotenv import load_dotenv
import os

load_dotenv()
animate_css = os.getenv("ANIMATE_CSS")
bg_color = '#4BF8FD'

# List of pages
pages = ['About', 'Contact', 'Social']


async def page_content(pagename: str):
    with ui.row().classes('flex flex-row justify-center'):
        ui.label(f'{pagename}').style(replace=f'font-family: Prata, serif; font-size: 13.5vw; color: ')


# Function to generate dynamic content for a page
async def generate_content(pagename: str):
    # call a function to get the content
    await page_content(pagename)


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
    # ui.add_head_html(animate_css)
    ui.add_head_html('''
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prata&display=swap" rel="stylesheet">
    <style>
        :root {
            --nicegui-default-padding: 0rem;
            --nicegui-default-gap: 0rem;
        }
    </style>
    ''')

    def menu_list(page_list_item):
        return ui.menu_item(f'{page_list_item}', lambda: ui.open(f'{page_list_item.lower()}'), auto_close=True)

    ui.query('body').style(replace=f'background-color: {bg_color};')
    ui.image('static/images/Home.svg').style(replace='width: 100%; height: 100%;')
    with ui.row().classes('w-full h-full absolute top-0 left-0'):
        with ui.button(icon='menu', color='#737373').classes('absolute top-0 left-0 m-3 p-3 rounded-full'):
            with ui.menu() as menu:
                for page in pages:
                    await page_iter(page)
                    menu_list(page)
                ui.separator()
                ui.menu_item('Close', on_click=menu.close)


ui.run(title='Scideology', storage_secret='secret_key', dark=False)
