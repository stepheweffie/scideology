from nicegui import ui, events
import pandas as pd

menu_classes = f'fixed top-0 right-0 m-3 p-6 rounded-full'
footer_classes = f'flex flex-row justify-center bg-gray-100 w-full fixed bottom-0 left-0'
footer_brand = True
serif_font_color = '#737373'
sans_serif_color = '#737373'
serif_font_size = '13.5vw'
main_font_size = '6.5vw'
title = 'Settings'
body_html = ''''''
# '#4BF8FD'


async def create_setup() -> None:
    @ui.page('/setup')
    async def setup():
        with ui.row().classes('w-full h-full top-0 left-0 wrap justify-end'):
            ui.label('Settings & Setup').classes('text-4xl text-gray-700')

        with ui.row().classes('w-full h-full wrap justify-center'):
            app_name = ui.input(label='App or Brand Name').classes('text-4xl bg-gray-100')
            app_title = ui.input(label='Title, e.g. can be same as App or Brand Name').classes('text-4xl bg-gray-100')

            with ui.row().classes('w-full h-full justify-center'):
                with ui.column():
                    one = ui.input(label='Page One, i.e. Content').classes('text-4xl bg-gray-100')
                    two = ui.input(label='Page Two, i.e. Forum').classes('text-4xl bg-gray-100')
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

                    with ui.dialog().props('full-width') as dialog:
                        with ui.card():
                            content = ui.markdown()

                    def allowed_image_file(filename):
                        return '.' in filename and \
                            filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif', 'svg']

                    def allowed_video_file(filename):
                        return '.' in filename and \
                            filename.rsplit('.', 1)[1].lower() in ['mov', 'mp4', 'webm']

                    async def handle_upload(args: events.UploadEventArguments):
                        if allowed_image_file(args.name):
                            file_path = 'static/images/' + args.name
                            with open(file_path, 'wb') as f:
                                f.write(args.content.read())
                            ui.notify(f'File uploaded: {args.name}')

                        if allowed_video_file(args.name):
                            file_path = 'static/videos/' + args.name
                            with open(file_path, 'wb') as f:
                                f.write(args.content.read())
                            ui.notify(f'File uploaded: {args.name}')
                        else:
                            ui.notify('File format not allowed', level='error')

                    header_image = ui.upload(multiple=False, auto_upload=True,
                                             label='Upload Home Background Header Image',
                                             on_upload=lambda e: handle_upload(e)).classes('text-4xl bg-gray-100')

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
                    logo_upload = ui.upload(label='Upload Logo', on_upload=lambda e: handle_upload(e)
                                            ).classes('text-4xl bg-gray-100')
                    video_upload = ui.upload(label='Upload Trailer', on_upload=lambda e: handle_upload(e)
                                             ).classes('text-4xl bg-gray-100')

        page_data = {'main': f'{main_detail}'}
        main_page_data = page_data['main']

        head_links = f''' '''
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

        def submit():
            df = pd.DataFrame(data={
                'Setup': True,
                'Trailer': False,
                'App Name': [app_name.value],
                'App Title': [app_title.value],
                'Serif Font': [serif_font.value],
                'Serif Link': [serif_link.value],
                'Serif Color': [serif_color.value],
                'Sans Serif': [sans_serif.value],
                'Sans Serif Link': [sans_serif_link.value],
                'Font Size': [main_font_size],
                'Sans Serif Color': [sans_serif_color.value],
                'Menu Background Color': [menu_bg_color.value],
                'Footer Background Color': [footer_bg_color.value],
                'Background Color': [bg_color.value],
                'Body HTML': [body_html],
                'Footer Classes': [footer_classes],
                'Footer Brand': [footer_brand],
                'Head Links': [head_links],
                'Main Detail': [main_detail.value],
                'Top Detail': [top_detail.value],
                'Bottom Detail': [bottom_detail.value],
                'Page One': [one.value],
                'Page Two': [two.value],
                'Page Three': [three.value],
                'Main Page Data': [main_page_data],
                'Head HTML': [head_html],
                'Google Fonts': [google_fonts],
            })

            # Drop defaults and check for any values
            if df.drop(['Setup', 'Trailer'], axis=1).notna().any().any():
                # Drop any rows value NaN
                df_cleaned = df.dropna(how='all')
                # Save changed data without overwriting with blank data
                df_cleaned.to_json('settings.json', orient='index', indent=2)
                ui.open('/')
                return df

        with ui.row().classes('w-full h-full wrap justify-center'):
            ui.button('Submit', on_click=submit).classes('text-4xl')


@ui.page('/setup/assets')
async def setup_assets():
    with ui.column():
        html_upload = ui.upload(label='Upload HTML Files').classes('text-4xl')
        css_upload = ui.upload(label='Upload CSS Files').classes('text-4xl')
        js_upload = ui.upload(label='Upload JS Files').classes('text-4xl')


ui.run(title=f'{title}', storage_secret='secret_key', dark=False)
