db_info = {'host': 'dpg-ch79c6rhp8u9bo5u6ffg-a.oregon-postgres.render.com',
           'database': 'test_book',
           'psw': '4RC1sqQUyVBQudzO4Ttz68LOyrofao8n',
           'user': 'test_book_user',
           'port': ''}

class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

