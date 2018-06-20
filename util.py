import json
import io
import os


def load_json(file):
    global curr_state
    global state_file
    if not os.path.isfile(file):
        open(file, 'w').close()
        curr_state = {'users': {}, 'questions': {}}
    else:
        with open(file, 'r') as f:
            curr_state = json.loads(f.read())
    state_file = file


def update_state_file():
    global curr_state
    global state_file
    with io.open(state_file, 'w') as out:
        json.dump(curr_state, out, indent=2)


def add_user(user_id):
    global curr_state
    global state_file
    if user_id in curr_state['users'].keys():
        print('user already exists')
        return {'status': 'error', 'error_msg': 'user already exists'}
    curr_state['users'][user_id] = {}
    update_state_file()
    return {'status': 'success'}


def add_response(user_id, question_id, response):
    global curr_state
    global state_file
    if user_id not in curr_state['users'].keys():
        return {'status': 'error', 'error_msg': 'user not found'}
    if question_id in curr_state['users'][user_id].keys():
        curr_state['users'][user_id][question_id].append(response)
    else:
        curr_state['users'][user_id][question_id] = [response]
    update_state_file()
    return {'status': 'success'}


def parse_email(email_body):
    email_break = ["<br>"]  # TODO use regex!! Add to consts?
    response = {}
    for line in email_body:
        if line in email_break:
            break
        else:
            question_id = 1  # TODO parse line to get via regex
            answer = 2       # TODO parse line to get via regex
            response[question_id] = answer
    if response:
        return {'status': 'success', 'response': response}
    else:
        return {'status': 'error'}
