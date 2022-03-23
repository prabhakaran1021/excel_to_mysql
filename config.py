from environs import Env
env = Env()
env.read_env()
DB_ENGINE = env.str('DB_ENGINE')
DB_NAME = env.str('DB_NAME')
DB_LOCAL=env.str('DB_LOCAL')
DB_LOCAL_USER=env.str('DB_LOCAL_USER')
DB_LOCAL_PASS=env.str('DB_LOCAL_PASS')
DB_LOCAL_PORT=env.str('DB_LOCAL_PORT')
class DATABASE:
         ENGINE= DB_ENGINE
         NAME= DB_NAME
         USER= DB_LOCAL_USER
         PASSWORD= DB_LOCAL_PASS
         HOST= DB_LOCAL
         PORT= DB_LOCAL_PORT

