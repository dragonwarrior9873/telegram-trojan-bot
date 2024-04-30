from env_loading import load_env_variable

# API_TOKEN = load_env_variable("7046437476:AAHH8OsG9-96xGwqi30-mwwN2GQUfobioZg")
API_TOKEN = "7046437476:AAHH8OsG9-96xGwqi30-mwwN2GQUfobioZg"
API_URL = f'https://api.telegram.org/bot{API_TOKEN}' + '/{method_name}'
CSV_MIME_TYPE = 'text/csv'
TARGET_CHANNEL = '@solana_trojanbot'