from nicegui import ui
from dotenv import load_dotenv
import body_content
import os

load_dotenv()
bg_color = '#4BF8FD'
menu_classes = 'fixed top-0 right-0 m-3 p-6 rounded-full'
footer_classes = f'flex flex-row justify-center bg-gray-100 w-full fixed bottom-0 left-0'
footer_brand = True
font_color = '#737373'
font_size = '13.5vw'
main_font_size = '6.5vw'
font_family = 'Prata, serif'
sans_serif = 'Urbanist, sans-serif'
main_font = sans_serif
title = 'Scideology'
app_name = 'Scideology'
main_data = 'Welcome, to the blog of blogs. For content creators. To create autonomy. With content.'
sample_content = 'Content Subscription App.'
main_content = f'Welcome, to {app_name} for content creators.'
page_data = {'main': f'{main_data}'}
main_page_data = page_data['main']
head_html = '''<link rel="preconnect" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prata&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@500&display=swap" rel="stylesheet">
    <style>
        :root {
            --nicegui-default-padding: 0rem;
            --nicegui-default-gap: 0rem;
        }
    </style>'''
body_html = ''''''
pages = os.getenv("PAGES").split(',')
page_dict = {page: sample_content for page in pages}
# page_data.update(page_dict)


async def page_content(pagename: str):
    global page_dict
    with ui.row().classes('flex flex-row justify-center'):
        if pagename in page_dict.keys():
            ui.label(f'{pagename}').style(replace=f'font-family: {font_family}; font-size: {font_size}; '
                                                  f'color: {font_color}')
        # await body_content.get(pagename, page_dict)


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


# Function to generate dynamic content for a page
async def generate_content(pagename: str):
    # call a function to get the content
    await page_content(pagename)
    await page_body(pagename)
    await page_footer(pagename)


@ui.page('/')
async def main():
    # Styling and fonts
    ui.add_head_html(f'''
    {head_html}
    ''')

    async def dynamic_page(pagename: str):
        @ui.page(f'/{pagename.lower()}')
        async def page():
            print(pagename.lower())
            await generate_content(pagename.lower())

    async def menu_list(pagename):
        ui.menu_item(f'{pagename}', lambda: ui.open(f'{pagename.lower()}'), auto_close=True)

    ui.query('body').style(replace=f'background-color: {bg_color};')
    ui.image('static/images/Home.svg').style(replace='width: 100%; height: 100%;')

    with ui.row().classes('w-full h-full absolute top-0 left-0'):
        with ui.button(icon='menu', color=f'{font_color}').classes(f'{menu_classes}'):
            with ui.menu() as menu:
                for page in page_dict.keys():
                    await menu_list(page)
                ui.separator()
                ui.menu_item('Close', on_click=menu.close)
            for page in page_dict.keys():
                await dynamic_page(page)
    with ui.row().classes('flex flex-row'):
        ui.label(f'{main_page_data}').style(replace=f'font-family: {main_font}; font-size: {main_font_size}; '
                                                    f'color: {font_color}').classes('ml-5')

ui.run(title=f'{title}', storage_secret='secret_key', dark=False)
