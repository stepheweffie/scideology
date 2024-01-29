from nicegui import ui
from pymongo import MongoClient
import datetime


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


mongo_uri = "your_mongodb_connection_uri"
client = MongoClient(mongo_uri)
db = client["your_database_name"]

# Sample route to fetch data from the database


@ui.page('/get_data')
def get_data(data_dict):
    data = db.your_collection.find(data_dict)
    return {'result': list(data)}


@ui.page('/post_data')
def post_data(data_dict):
    data_dict["created_at"] = datetime.datetime.now()
    data = db.your_collection.insert_one(data_dict)
    return {'result': str(data.inserted_id)}

