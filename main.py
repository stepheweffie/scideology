from nicegui import ui
from dotenv import load_dotenv

load_dotenv()
bg_color = '#4BF8FD'
footer_classes = f'flex flex-row justify-center bg-gray-100 w-full fixed bottom-0 left-0'
footer_brand = True
font_color = '#737373'
title = 'Scideology'
app_name = 'Scideology'
font_family = 'Prata, serif'
# List of pages
pages = ['About', 'Contact', 'Social']


async def page_content(pagename: str):
    with ui.row().classes('flex flex-row justify-center'):
        ui.label(f'{pagename}').style(replace=f'font-family: {font_family}; font-size: 13.5vw; color: {font_color}')


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
                ui.label(f'{app_name}').style(replace=f'font-family: {font_family}; font-size: 13.5vw; color: {font_color}')


# Function to generate dynamic content for a page
async def generate_content(pagename: str):
    # call a function to get the content
    await page_content(pagename)
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
    ui.add_head_html('''
    <link rel="preconnect" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
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
    ui.image('static/images/Home.svg').style(replace='width: 100%; height: 100%;').classes('animate__animated '
                                                                                           'animate__fadeInDown')
    with ui.row().classes('w-full h-full absolute top-0 left-0'):
        with ui.button(icon='menu', color='#737373').classes('absolute top-0 left-0 m-3 p-3 rounded-full'):
            with ui.menu() as menu:
                for page in pages:
                    await page_iter(page)
                    menu_list(page)
                ui.separator()
                ui.menu_item('Close', on_click=menu.close)


ui.run(title=f'{title}', storage_secret='secret_key', dark=False)
