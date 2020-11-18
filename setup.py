from setuptools import setup
setup(
    name = 'autoworkspace',
    version = '0.1.0',
    packages = ['autoworkspace'],
    entry_points = {
        'console_scripts': [
            'autoworkspace = autoworkspace.__main__:main'
        ]
    }) 