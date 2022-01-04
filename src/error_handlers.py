def register_validation_error(error):
    rv = dict({'message': error.messages})
    return rv, 400
