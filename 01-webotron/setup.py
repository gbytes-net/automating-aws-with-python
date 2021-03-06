from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Robon Norwood',
    author_email='robin@acloud.guru',
    description='Webotron 80 is a tool to deploy a static website to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/ACloudGuru/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
