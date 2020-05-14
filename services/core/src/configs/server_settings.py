import os

HOST        = os.environ.get('HOSPITAL_SERVER_HOST')
PORT        = int(os.environ.get('HOSPITAL_SERVER_PORT'))
DEBUG       = bool(int(os.environ.get('HOSPITAL_SERVER_DEBUG')))
SSL         = None
WORKERS     = int(os.environ.get('HOSPITAL_SERVER_WORKERS'))
ACCESS_LOG  = bool(int(os.environ.get('HOSPITAL_SERVER_ACCESS_LOG')))
AUTO_RELOAD = bool(int(os.environ.get('HOSPITAL_SERVER_AUTO_RELOAD')))
