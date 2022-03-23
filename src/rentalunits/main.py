import os

from rentalunits import log, config

logger = log()

def main():
    logger.info("I am in main")

    app_config = config()
    app_settings = app_config['SECTION 1']
    user = app_settings['user']

    color = os.environ.get('COLOR')
    print(user, color)


if __name__ == '__main__':
    main()


