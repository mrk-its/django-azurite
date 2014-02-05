from django.conf import settings

AZURITE = {
    'ACCOUNT_NAME': None,
    'ACCOUNT_KEY': None,
    'CONTAINER': None,
    'STATIC_CONTAINER': None,
    'CDN_HOST': None,
    'USE_SSL': False,
    'COMPRESS_CONTENT_TYPES': (),
}

if hasattr(settings, 'AZURITE'):
    AZURITE.update(settings.AZURITE)
