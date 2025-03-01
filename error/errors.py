ALREADY_EXIST = ({'status': 402, 'msg': 'An user has existed.'}, 402)
DOES_NOT_EXIST = ({'status': 409, 'msg': 'Does not exists.'}, 409)
EMPTY = ({'status': 202, 'msg': 'None'}, 202)
HEADER_NOT_FOUND = ({'status': 999, 'msg': 'Header does not exists.'}, 999)
INVALID_INPUT = ({'status': 422, 'msg': 'Invalid input.'}, 422)
NO_INPUT = ({'status': 400, 'msg': 'No input data provided.'}, 400)
NOT_ADMIN = ({'status': 999, 'msg': 'Admin permission denied.'}, 999)
HEADER_NOT_FOUND = ({'status': 404, 'msg': 'Resource could not be found.'}, 404)
SERVER_ERROR = ({'status': 500, 'msg': 'An error occured.'}, 500)
UNAUTHORIZED = ({'status': 401, 'msg': 'Unauthorized'}, 401)
UNKNOWN_ERROR = ({'status': 403, 'msg': 'An unknown error has occured. Please try again.'}, 403)