from setuptools import setup, find_packages

setup(
    name="haven",
    version='1.1.103',
    zip_safe=False,
    platforms='any',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=['events', 'netkit', 'setproctitle'],
    url="https://github.com/dantezhu/haven",
    license="MIT",
    author="dantezhu",
    author_email="zny2008@gmail.com",
    description="flask's style binary server framework",
)
