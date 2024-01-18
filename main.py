from nicegui import ui
import body_content
import os
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
# pages = os.getenv("PAGES").split(',')
pages = ['About', 'Contact', 'Social']
page_dict = {page.lower(): sample_content for page in pages}
print(page_dict)
print(pages)
# page_data.update(page_dict)


async def page_content(pagename: str):
    global page_dict
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
            print(page_name.lower())
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
