import urllib.request, json
 
def api():
    # if (request.method == "POST"):
        url = 'https://jsonplaceholder.typicode.com/todos/1'
        # payload = jsonify(json)
        # payload.status_code = 200
        # return payload
        response = urllib.request.urlopen(url)
        data = response.read()
        # this converts string JSON data to python operational data
        return json.loads(data)
    # else: 
    #   return jsonify({'hi': 'yo'})