# import threading
# from flask.templating import render_template
# from flask import Flask, Response, _app_ctx_stack
# from flask_cors import CORS

# from database import models
# from database.database import SessionLocal, engine, Base
# from sqlalchemy.orm import scoped_session
from bot_config import Config
import pyrogram
from pyrogram import idle

# app = Flask(__name__)


# @app.teardown_appcontext
# def remove_session(*args, **kwargs):
#     app.session.remove()


# @app.route('/', methods=['GET', 'POST'])
# def wake():
#     return Response('ok', status=200)

if __name__ == "__main__":
    # models.Base.metadata.create_all(bind=engine)
    # CORS(app)
    # app.session = scoped_session(
    #     SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)
    # Base.query = app.session.query_property()

    # threading.Thread(target=app.run, args=(
    #     "0.0.0.0", Config.PORT), daemon=True).start()
    plugins = dict(
        root="plugins"
    )
    bot = pyrogram.Client(
        "Me",
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )

    bot.start()
    idle()
    bot.stop()

