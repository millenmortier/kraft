from setuptools import setup, find_packages
import glob
import os

with open('requirements.txt') as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#")]

from kraft import __version__, __description__, __program__

setup(
    name = __program__,
    version = __version__,
    packages = find_packages(),
    description = __description__,
    url = 'https://github.com/unikraft/kraft.git',
    author = 'Alexander Jung',
    author_email = 'a.jung@lancs.ac.uk',
    entry_points = """
        [console_scripts]
        {program} = kraft.kraft:kraft
        """.format(program = __program__),
    scripts = [
        'scripts/qemu-guest',
        'scripts/xen-guest',
        'scripts/kraft-net'
    ],
    keywords = [],
    tests_require = ['pytest', 'coveralls'],
    zip_safe = False,
    install_requires = required,
    include_package_data=True
)
