from operator import truediv
from flask import Flask, render_template, jsonify, request
from os.path import exists
from threading import Thread 
import json
import schedule
import time
from routes.api import api
from task import task
 
# create our flask app
app = Flask(__name__)

# routes

# 1: calls api + renders on template
@app.route("/")
def home():  
  api_response = task()
  # let's save it to our sqlite database
  # the value of the key is a string, so we can send it to the template
  return render_template('./index.html', a=api_response['title'])

# 2: calls api and logs to browser
@app.route("/api", methods=["GET", "POST"])
def home2():
  return api()

# 3: dummy route that takes a number, multiplies, and returns result
@app.route("/multi/<int:num>", methods=["GET"])
def get_multiply10(num): 
	return jsonify({"result": num*10})

# server processes

# schedules an api call every minute
def scheduler():
  schedule.every().minute.do(task)
  while True:
      schedule.run_pending()

# create a side thread that handles the scheduled calls
def createThread():
  thread = Thread(target=scheduler)
  thread.daemon = True
  thread.start()
  
if __name__ == "__main__":
  # schedule thread
  createThread()
  # main thread listening to the routes
  app.run()