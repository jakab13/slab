from setuptools import setup, find_packages
import sys
import re

with open('README.md') as f:
    readme = f.read()

# extract version
with open('slab/__init__.py') as file:
    for line in file.readlines():
        m = re.match("__version__ *= *['\"](.*)['\"]", line)
        if m:
            version = m.group(1)
        raise RuntimeError('Unable to find version string in __init__.py')


setup(name='soundlab',
      version=version,
      description='Tools for generating and manipulating digital signals, particularly sounds.',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='http://github.com/DrMarc/soundlab.git',
      author='Marc Schoenwiesner',
      author_email='marc.schoenwiesner@gmail.com',
      license='MIT',
      python_requires='>=3.6',
      install_requires=['numpy', 'scipy', 'matplotlib', 'SoundFile', 'SoundCard'
        ] + ['windows-curses'] if "win" in sys.platform else ['curses'],
      packages=find_packages(),
      package_data={'slab': ['data/mit_kemar_normal_pinna.sofa',
                             'data/KEMAR_interaural_level_spectrum.npy']},
      include_package_data=True,
      zip_safe=False)
