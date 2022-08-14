import os

from rentalunits import log, config
from db.database import create_db_and_tables

logger = log()

def main():
    logger.info("I am in main")

    app_config = config()
    app_settings = app_config['SECTION 1']
    user = app_settings['user']
    color = os.environ.get('color', 'YELLOW')
    print(user, color)


if __name__ == '__main__':
    main()
