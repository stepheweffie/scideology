

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
sample_content = 'Customize A Content Subscription App Deployed For You.'
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
