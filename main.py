import util

# Global vars
state_file = ''
curr_state = {'users': {},
              'questions': {},
              }


def main():
    util.load_json('state.json')


def load(file):
    util.load_json(file)


def send():
    print("Do we really need this?")


def receive(user_id, email_body):
    status = util.parse_email(email_body)
    if status['status'] == 'error':
        print("error!")
        exit(1)
    else:
        for question_id in status['response'].keys():
            util.add_response(user_id, question_id, status['response'][question_id])


if __name__ == '__main__':
    main()
