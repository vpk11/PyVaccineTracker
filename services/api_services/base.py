class Base(object):
    def __init__(self):
        print('Base API Service')

    def handle_error(self, error):
        return {'error': error}
