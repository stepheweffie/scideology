from nicegui import ui
from dotenv import load_dotenv
import os
load_dotenv()
pages = os.getenv("PAGES").split(',')


async def render(render_list: list):
    for item in render_list:
        ui.label(f'{item}')


async def get(page: str, data: dict):
    global pages
    with ui.row().classes('flex flex-row justify-center'):
        if page in pages:
            if len(data) > 1:
                content = data[f'{page}']
                await render(content)


async def post(page: str, data: dict):
    global pages
    with ui.row().classes('flex flex-row justify-center'):
        content = data[f'{page}']
        # post_render(content)


async def put(page: str, data: dict):
    global pages
    with ui.row().classes('flex flex-row justify-center'):
        content = data[f'{page}']
        # put_render(content)


async def delete(page: str, data: dict):
    global pages
    with ui.row().classes('flex flex-row justify-center'):
        content = data[f'{page}']
        # delete_render(content)