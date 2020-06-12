import pathlib
from setuptools import setup

CWD = pathlib.Path(__file__).parent
README = (CWD / 'README.md').read_text()

setup(
    name='quantconnect-lean',
    version='0.1.2',
    description='API and Python type definitions for the Lean algorithmic trading engine',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/QuantConnect/quantconnect-lean',
    author='QuantConnect Corp.',
    author_email='support@quantconnect.com',
    license='Apache 2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License'
    ],
    packages=[
        'QuantConnect',
        'QuantConnect.Data',
        'QuantConnect.Securities',
        'QuantConnect.Algorithm',
    ],
    package_data={
        'QuantConnect': ['py.typed', '*.pyi'],
        'QuantConnect.Data': ['py.typed', '*.pyi'],
        'QuantConnect.Securities': ['py.typed', '*.pyi'],
        'QuantConnect.Algorithm': ['py.typed', '*.pyi'],
    },
    install_requires=['matplotlib', 'pandas', 'requests'],
    python_requires='>=3.6'
)

