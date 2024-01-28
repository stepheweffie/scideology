from nicegui import ui


async def affiliate():
    with ui.row().classes('w-full h-full justify-center'):
        with ui.column().classes('w-full h-full'):
            with ui.card().classes('w-full h-full'):
                with ui.row().classes('w-full h-full justify-center'):
                    with ui.column().classes('w-full h-full'):
                        with ui.label('Our Built-in Affiliate Program').classes('text-4xl'):
                            pass
                        # Serverless function


# doctl serverless functions invoke sample/emails -p
# from:user@do.com to:user@gmail.com subject:Sammy content:Good Morning from Sammy.
# curl -X PUT -H 'Content-Type: application/json' {your-DO-app-url} -d
# '{"from":"user@do.com", "to":"user@gmail.com", "subject": "Sammy", "content":"Good Morning from Sammy!"}'