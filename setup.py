from distutils.core import setup

setup(
        name = 'code_clone_detection',
        packages = ['code_clone_detection'],
        version = '0.1',
        description = 'Code clone detection for Python and C using abstract syntax trees',
        author = 'Prashant Baisla, Vivek Agarwal, Abhijit Katiyar, Aashish Thyagarajan',
        author_email = 'prashantbaisla@gmail.com',
        url = 'https://github.com/panchdevs/code-clone-detection',
        download_url = 'https://github.coim/panchdevs/code-clone-detection/archive/v0.1.0.tar.gz',
        keywords = ['code', 'clone', 'detection', 'syntax', 'tree'],
        install__requires = ['pycparser']
        )
