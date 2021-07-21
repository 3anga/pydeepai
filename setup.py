from setuptools import setup, find_packages

setup(
    name="PyDeepAI",
    version='0.1.0',
    author="Mikhail Serebryakov a.k.a Zanga",
    author_email="<rayman.channel@yandex.ru>",
    description='Unofficial DeepAI python module',
    long_description_content_type="text/markdown",
    long_description='A package that allows to easy to use the DeepAI API.',
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'image api', 'video api', 'requests', 'http'],
    classifiers=[
        "Development Status :: 3",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
