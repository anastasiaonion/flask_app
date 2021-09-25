from flask import Flask, render_template
import uuid
import time
import datetime
from functools import wraps

app = Flask(__name__)


def count_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        data = func()
        end = time.monotonic()
        execution_time = end - start
        data['execution_time'] = execution_time
        return data
    return wrapper


@count_execution_time
def generate_data():
    time.sleep(1)
    return {'uuid': uuid.uuid4(),
            'execution_time': None,
            'date': datetime.datetime.now()}


@app.route("/get_data/<int:request_count>")
def get_data(request_count=1):
    data_list = []
    for _ in range(request_count):
        data = generate_data()
        data_string = f'{data["uuid"]}:{data["execution_time"]} s:{data["date"]}'
        data_list.append(data_string)
    return render_template('get_data.html', data_list=data_list)
