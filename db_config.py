import os

def get_mysql_config():
    config = {
        'host': os.getenv('MYSQL_HOST'),
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'database': os.getenv('MYSQL_DATABASE')
    }
    # Check if SSL mode is set
    ssl_mode = os.getenv('MYSQL_SSL_MODE')
    if ssl_mode:
        config['connect_args'] = {'sslmode': ssl_mode}
    return config

def create_engine():
    config = get_mysql_config()
    engine = create_engine(**config)  # Unpack dictionary as arguments
    return engine
