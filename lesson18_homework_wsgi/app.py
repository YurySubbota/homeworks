from data_base import data_from_db


def app(environ, start_response):
    if 'error' in environ['PATH_INFO'].lower():
        raise Exception('Detect "error" in URL path')
    users_list = data_from_db()
    users = ''
    for user in users_list:
        users += '\n'
        for key in user.keys():
            users += f'{key}: {user[key]}, '

    count = f'{users}'.encode('utf-8')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [count]
