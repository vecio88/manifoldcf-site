# pelicanconf.py
#SITE_METADATA = {
#    'name': 'Apache ManifoldCF Website',
#    'description': 'The official website of Apache ManifoldCF',
#    'domain': 'manifoldcf.apache.org',
#    'logo': '/extra/favicon.ico',
#    'repository': 'https://github.com/apache/manifoldcf-site/blob/main/content/',
#    'trademarks': 'Apache ManifoldCF, Apache, and the Apache feather logo are trademarks of The Apache Software Foundation.',
#}

SITENAME = 'Apache ManifoldCF Website'
DEFAULT_DATE = '2024-01-21'

THEME = 'theme/apache'

LANGUAGES = {
    'en': ('English', 'en_US'),
    'ja': ('日本語', 'ja_JP'),
    'zh': ('中文', 'zh_CN'),
}

IGNORE_FILES = ['README.md', '*.sh', '*.py', '*.html']

STATIC_PATHS = ['extra', 'css', 'js', 'highlight', 'images', 'fonts']

PAGE_PATHS = ['pages']
PAGE_SAVE_AS = '{path}/{lang}/{slug}.html'
PAGE_URL = '{path}/{lang}/{slug}.html'

# OUTPUT_PATH = '/output'
# GENID_UNSAFE = True