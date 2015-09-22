import services.common.tools as tools
import json

def search(args):
    """
    Create a list with the specified name and type
    """

    token = args['_token']

    # filter the list name for special characters
    filtered_name = tools.filter_name(args['name'])

    payload = { 'name': filtered_name, 'type': args['type'] }

    # create the list
    response = tools.do_request_post('lists', token, args['data'], **payload)
    print json.dumps(response, indent=2)
    print '---'

def list(args):
    """
    Return all of the lists for which the current user has access
    """

    token = args['_token']
    response = tools.do_request('lists', token)

    for result in response['lists']:
        print json.dumps(result, indent=2)
        print '---'
