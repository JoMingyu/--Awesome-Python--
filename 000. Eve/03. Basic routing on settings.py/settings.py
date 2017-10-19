DOMAIN = {
    'user': {
        'schema': {
            'id': {
                'type': 'string',
                'unique': True
            },
            'pw': {
                'type': 'string'
            },
            'name': {
                'type': 'string'
            }
        }
    }
}

RESOURCE_METHODS = ['GET', 'POST']
# Avoid 405 METHOD NOT ALLOWED
