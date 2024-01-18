from nicegui import ui

menu_classes = 'fixed top-0 right-0 m-3 p-6 rounded-full'
footer_classes = f'flex flex-row justify-center bg-gray-100 w-full fixed bottom-0 left-0'
footer_brand = True
font_color = '#737373'
font_size = '13.5vw'
main_font_size = '6.5vw'
title = 'Settings'
body_html = ''''''


@ui.page('/')
async def setup():
    with ui.row().classes('w-full h-full top-0 left-0 justify-end'):
        ui.label('Settings & Setup Form').classes('text-4xl text-gray-700 animate__animated animate__fadeInDown')
    with ui.row().classes('w-full h-full top-0 left-0 justify-center'):
        app_name = ui.input(label='App or Brand Name').classes('text-4xl bg-gray-100')
        app_title = ui.input(label='Title, e.g. can be same as App or Brand Name').classes('text-4xl bg-gray-100')
        one = ui.input(label='Page One, i.e. About').classes('text-4xl bg-gray-100')
        two = ui.input(label='Page Two, i.e. Contact').classes('text-4xl bg-gray-100')
        three = ui.input(label='Page Three, i.e. Social').classes('text-4xl bg-gray-100')
        main_detail = ui.input(label='Main Detail Text').classes('text-4xl bg-gray-100')
        top_detail = ui.input(label='Top Detail Text').classes('text-4xl bg-gray-100')
        serif_link = ui.input(label='Serif Font Link').classes('text-4xl bg-gray-100')
        serif_font = ui.input(label='Sans Serif Name').classes('text-4xl bg-gray-100')
        sans_serif_link = ui.input(label='Sans Serif Font Link').classes('text-4xl bg-gray-100')
        sans_serif = ui.input(label='Sans Serif Name').classes('text-4xl bg-gray-100')
        with ui.row().classes('w-full h-full top-0 left-0 justify-center'):
            header_image = ui.upload(label='Upload Transparent (or not) Home Background Header').classes('text-4xl bg-gray-100')
            home_bg = ui.color_input(label='Home Page Background Color').classes('text-4xl bg-gray-100')
            serif_color = ui.color_input(label='Serif Font Color').classes('text-4xl bg-gray-100')
            sans_serif_color = ui.color_input(label='Sans Serif Font Color').classes('text-4xl bg-gray-100')
            image_upload = ui.upload(label='Upload Images').classes('text-4xl bg-gray-100')

    app_name = app_name.value
    # 'Scideology'
    app_title = app_title.value
    serif_font = serif_font.value
    # 'Prata, serif'
    serif_link = serif_link.value
    sans_serif = sans_serif.value
    sans_serif_link = sans_serif_link.value
    # 'Urbanist, sans-serif'
    main_font = sans_serif
    main_detail = main_detail.value
    # 'Welcome, to the blog of blogs. For content creators. To create autonomy. With content.'
    top_detail = top_detail.value
    # 'Customize A Content Subscription App Deployed For You.'
    home_bg = home_bg.value
    # '#4BF8FD'
    page_data = {'main': f'{main_detail}'}
    main_page_data = page_data['main']
    pages = [one.value, two.value, three.value]
    page_dict = {page.lower(): top_detail for page in pages}
    # <link href="https://fonts.googleapis.com/css2?family=Prata&display=swap" rel="stylesheet">
    # <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@500&display=swap" rel="stylesheet">

    google_fonts = f''' 
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        {serif_link}
        {sans_serif_link}
        '''

    head_html = google_fonts + '''
        <style>
            :root {
                --nicegui-default-padding: 0rem;
                --nicegui-default-gap: 0rem;
            }
        </style>'''


ui.run(title=f'{title}', storage_secret='secret_key', dark=False)
