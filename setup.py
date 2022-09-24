from setuptools import setup
setup(
    name='openai_cli_test',
    version='0.0.1',
    scripts=['bash_scripts/openai_auto.sh'],
    packages=['openai_cli_test'],
    entry_points={
        'console_scripts': [
            'openai_cli_test=openai_cli_test.openai_cli_test:cli',
            'openauto=bash_scripts/openai_auto.sh'
        ]
    }
)
