__description__

this app calls an api + displays data in 3 possible ways
- it writes to file `data/my.json` (scheduled for every minute)
- it renders to a template (when user goes to path `http://localhost:5000/`)
- it writes to the browser (when user goes to `http://localhost:5000/api`)

__to start app__

1. activate virtual env 
    on mac: `source test-env/bin/activate`
    on pc: `i forget`

2. run server: `python3 server.py`


3. finished?
    on mac: `deactivate`

__dependencies used:__ 

flask
schedule 

__resources__

create a virtual env

https://realpython.com/python-virtual-environments-a-primer/#create-it

write to a file

https://www.geeksforgeeks.org/append-to-json-file-using-python/

write to a template

make an api call in flask to python

https://www.section.io/engineering-education/integrating-external-apis-with-flask/

https://www.bogotobogo.com/python/python-REST-API-Http-Requests-for-Humans-with-Flask.php

our api

https://jsonplaceholder.typicode.com/

templates

https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/#:~:text=Templates%20are%20files%20that%20contain,display%20in%20the%20user's%20browser.

cron jobs

https://pythonsimplified.com/how-to-schedule-python-scripts-using-schedule-library/

__ways to distribute your app__
- [ ] publish to a pubic store - google play, app store, ubuntu apps directory
- [ ] publish to an enteriprise store, like itunes connect
- [x] host on your own website or file server
- [ ] physically copy installation files to devices using USB drives or sd card

