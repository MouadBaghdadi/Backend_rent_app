from pydantic import BaseSettings
import datetime


class Settings(BaseSettings):
    APP_ENV: str = 'devs'
    GOOGLE_CLIENT_ID: str = '825602672601-3n7ofvpt6k7pqau121msgdstblpmofct.apps.googleusercontent.com'
    GOOGLE_SECRET: str = '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'
    GOOGLE_URL: str = 'https://accounts.google.com/o/oauth2/v2/auth'
    SECRET: str = 'OulLJiqkldb436-X6M11hKvr7wvLyG8TPi5PkLf4'
    authjwt_secret_key: str = 'bknb_9A{A|.JJlHUA5VdO0yd#hjct#KYVD?e}4=Q#Q2qQ|uqHP-w-->/UAF |o[Q'
    authjwt_token_location: set = {'cookies'}
    authjwt_cookie_csrf_protect: bool = False

    class Config:
        env_file = 'dev.env'
