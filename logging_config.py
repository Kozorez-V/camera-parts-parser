LOGGING = {
    'version': 1,
    'disabled_existing_loggers': False,
    'formatters': {
        'standart': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{'
        }
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'standart',
            'filename': '../camera-parts-parser/logs.log'
        }
    },
    'loggers': {
        'call': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}
