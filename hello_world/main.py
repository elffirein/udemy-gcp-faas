def hello_world(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return '', 204, headers

    headers = {
        'Access-Control-Allow-Origin' : '*'
    }
    
    requests_args = request.args
    requests_json = request.get_json(silent=True)

    if requests_args and 'name' and 'lastname' in requests_args:
        name = requests_args['name']
        lastname = requests_args['lastname']
    elif requests_json and 'name' in requests_json and 'lastname' in requests_json:
        name = requests_json['name']
        lastname = requests_json['lastname']
    else:
        name = 'world'
        lastname = ''
    return f"Hello {name} {lastname}"
