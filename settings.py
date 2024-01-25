from nicegui import ui
import pandas as pd
menu_classes = f'fixed top-0 right-0 m-3 p-6 rounded-full'
footer_classes = f'flex flex-row justify-center bg-gray-100 w-full fixed bottom-0 left-0'
footer_brand = True
serif_font_color = '#737373'
# sans_serif_color = '#737373'
serif_font_size = '13.5vw'
main_font_size = '6.5vw'
title = 'Settings'
body_html = ''''''


@ui.page('/setup')
async def setup():
    with ui.row().classes('w-full h-full top-0 left-0 wrap justify-end'):
        ui.label('Settings & Setup').classes('text-4xl text-gray-700')
    with ui.row().classes('w-full h-full wrap justify-center'):
        app_name = ui.input(label='App or Brand Name').classes('text-4xl bg-gray-100')
        app_title = ui.input(label='Title, e.g. can be same as App or Brand Name').classes('text-4xl bg-gray-100')
        with ui.row().classes('w-full h-full justify-center'):
            with ui.column():
                one = ui.input(label='Page One, i.e. About').classes('text-4xl bg-gray-100')
                two = ui.input(label='Page Two, i.e. Contact').classes('text-4xl bg-gray-100')
                three = ui.input(label='Page Three, i.e. Social').classes('text-4xl bg-gray-100')
            with ui.column():
                main_detail = ui.input(label='Main Detail Text').classes('text-4xl bg-gray-100')
                top_detail = ui.input(label='Top Detail Text').classes('text-4xl bg-gray-100')
                bottom_detail = ui.input(label='Bottom Detail Text').classes('text-4xl bg-gray-100')
            with ui.row().classes('w-full h-full justify-center'):
                serif_link = ui.input(label='Serif Font Link').classes('text-4xl bg-gray-100')
                serif_font = ui.input(label='Serif Name').classes('text-4xl bg-gray-100')
                sans_serif_link = ui.input(label='Sans Serif Font Link').classes('text-4xl bg-gray-100')
                sans_serif = ui.input(label='Sans Serif Name').classes('text-4xl bg-gray-100')
            with ui.row().classes('w-full h-full wrap justify-center'):
                header_image = ui.upload(label='Upload Transparent (or not) Home Background Header').classes(
                    'text-4xl bg-gray-100')
            with ui.row().classes('w-full h-full wrap justify-center'):
                head_links = ui.input(label='Head HTML Links').classes('text-4xl bg-gray-100')
            with ui.row().classes('w-full h-full wrap justify-center'):
                with ui.column():
                    bg_color = ui.color_input(label='Home Page Background Color').classes('text-4xl bg-gray-100')
                    serif_color = ui.color_input(label='Serif Font Color').classes('text-4xl bg-gray-100')
                    sans_serif_color = ui.color_input(label='Sans Serif Font Color').classes('text-4xl bg-gray-100')
                    footer_bg_color = ui.color_input(label='Footer Background Color').classes('text-4xl bg-gray-100')
                    menu_bg_color = ui.color_input(label='Menu Background Color').classes('text-4xl bg-gray-100')
            with ui.column():
                logo_upload = ui.upload(label='Upload Logo').classes('text-4xl bg-gray-100')
                image_upload = ui.upload(label='Upload Images').classes('text-4xl bg-gray-100')
                video_upload = ui.upload(label='Upload Videos').classes('text-4xl bg-gray-100')
            with ui.column():
                html_upload = ui.upload(label='Upload HTML Files').classes('text-4xl bg-gray-100')
                css_upload = ui.upload(label='Upload CSS Files').classes('text-4xl bg-gray-100')
                js_upload = ui.upload(label='Upload JS Files').classes('text-4xl bg-gray-100')

    app_name = app_name.value
    # 'Scideology'
    app_title = app_title.value
    serif_font = serif_font.value
    serif_font_family = "Prata, serif"
    # 'Prata, serif'
    serif_link = serif_link.value
    sans_serif = sans_serif.value
    sans_serif_link = sans_serif_link.value
    serif_color = serif_color.value
    sans_serif_color = sans_serif_color.value

    footer_bg_color = footer_bg_color.value
    menu_bg_color = menu_bg_color.value

    # 'Urbanist, sans-serif'
    main_detail = main_detail.value
    # 'Welcome, to the blog of blogs. For content creators. To create autonomy. With content.'
    top_detail = top_detail.value
    # 'Customize A Content Subscription App Deployed For You.'
    bottom_detail = bottom_detail.value
    bg_color = bg_color.value
    # '#4BF8FD'
    page_data = {'main': f'{main_detail}'}
    main_page_data = page_data['main']
    pages = [one.value, two.value, three.value]
    page_dict = {page.lower(): top_detail for page in pages}
    # <link href="https://fonts.googleapis.com/css2?family=Prata&display=swap" rel="stylesheet">
    # <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@500&display=swap" rel="stylesheet">
    head_links = f''' '''
    google_fonts = f''' 
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            {serif_link}
            {sans_serif_link}
            '''
    serif_font_family = ''
    sans_font_family = ''
    head_html = google_fonts + '''
            <style>
                :root {
                    --nicegui-default-padding: 0rem;
                    --nicegui-default-gap: 0rem;
                }
            </style>'''

    async def submit():
        df = pd.DataFrame(data={
            'App Name': [app_name],
            'App Title': [app_title],
            'Serif Font': [serif_font],
            'Serif Link': [serif_link],
            'Serif Color': [serif_color],
            'Sans Serif': [sans_serif],
            'Sans Serif Link': [sans_serif_link],
            'Serif Font Family': [serif_font_family],
            'Sans Serif Font Family': [sans_font_family],
            'Font Size': [main_font_size],
            'Sans Serif Color': [sans_serif_color],
            'Menu Background Color': [menu_bg_color],
            'Footer Background Color': [footer_bg_color],
            'Background Color': [bg_color],
            'Body HTML': [body_html],
            'Footer Classes': [footer_classes],
            'Footer Brand': [footer_brand],
            'Head Links': [head_links],
            'Main Detail': [main_detail],
            'Top Detail': [top_detail],
            'Bottom Detail': [bottom_detail],
            'Page One': [one.value],
            'Page Two': [two.value],
            'Page Three': [three.value],
            'Main Page Data': [main_page_data],
            'Head HTML': [head_html],
            'Google Fonts': [google_fonts],
        })
        df.to_csv('settings.csv')
        df.to_json('settings.json', orient='index', indent=2)
        return df

    with ui.row().classes('w-full h-full wrap justify-center'):
        ui.button('Submit', on_click=submit).classes('text-4xl')


ui.run(title=f'{title}', storage_secret='secret_key', dark=False)
