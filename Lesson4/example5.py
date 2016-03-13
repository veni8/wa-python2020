def get_message(status_code):
    if status_code == 200:
        return 'OK'
    elif status_code == 401:
        return 'Not authorized'
    elif status_code == 403:
        return 'Forbidden'
    elif status_code == 404:
        return 'Not found'
    elif status_code == 500:
        return 'Internal server error'


print(get_message(200))
