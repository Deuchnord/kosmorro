#!/usr/bin/env python3

#    Kosmorro - Compute The Next Ephemerides
#    Copyright (C) 2019  Jérôme Deuchnord <jerome@deuchnord.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pathlib
from setuptools import setup, find_packages

from kosmorrolib.core import VERSION

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='kosmorro',
    version=VERSION,
    author='Jérôme Deuchnord',
    author_email='jerome@deuchnord.fr',
    url='https://kosmorro.astronewbie.space',
    license='AGPL-3.0',
    description='A program that computes the ephemerides.',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords='kosmorro astronomy ephemerides ephemeris',
    packages=find_packages(),
    scripts=['kosmorro'],
    install_requires=['skyfield>=1.13.0,<2.0.0', 'tabulate', 'numpy>=1.17.0,<2.0.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    python_requires='>=3.7'
)