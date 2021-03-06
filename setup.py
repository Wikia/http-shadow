from setuptools import setup

setup(
    name='http_shadow',
    version='0.1',
    description='',
    url='https://github.com/macbre/http-shadow',
    author='macbre',
    author_email='macbre@wikia-inc.com',
    install_requires=[
        'requests==2.19.1',
        'wikia-common-kibana==2.2.5',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'get_urls=http_shadow.bin.get_urls:main',  # query elasticsearch and emit found URLs to stdout
            'check_urls=http_shadow.bin.check_urls:main',  # send requests and compare HTTP responses from two backends
        ],
    }
)
