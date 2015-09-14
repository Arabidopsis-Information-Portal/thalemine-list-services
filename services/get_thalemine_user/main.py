import services.common.tools as tools
import json

def search(args):
    """
    Return information about the current ThaleMine user
    """

    token = args['_token']
    response = tools.do_request('user', token)

    print json.dumps(response['user'], indent=2)
    print '---'

def list(args):
    """
    Return information about the current ThaleMine user
    """

    token = args['_token']
    response = tools.do_request('user', token)

    print json.dumps(response['user'], indent=2)
    print '---'
