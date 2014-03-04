from setuptools import setup, find_packages


setup(
    name = 'PhotoGallery',
    version = '0.1',
    packages = find_packages(),

    install_requires=[
        'Django < 1.7',
        'Pillow < 2.4',
        'psycopg2 < 2.6',
        'South < 0.9',
    ],

    entry_points={
        'console_scripts': [
            'gallery = manage:main'
        ],
    }
)
