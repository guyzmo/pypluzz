from setuptools import setup
import os
import sys

if sys.version_info.major != 3:
    raise Exception("Sorry this package only works with python3.")

def read(*names):
    values = dict()
    for name in names:
        if os.path.isfile(name):
            with open(name) as f:
                value = f.read()
        else:
            value = ''
        values[name.split('.')[0]] = value
    return values

long_description = """

{README}

""".format(**read('README.md'))

setup(name='pyvod.pluzz',
      version='1.5',
      description="PyVOD pluzz browser",
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved',
          'Operating System :: Unix',
      ],
      keywords='download tv show',
      author='Bernard `Guyzmo` Pratz',
      author_email='pypluzz@m0g.net',
      url='http://m0g.net',
      license='GPLv3',
      packages=['vod.pluzz'],
      zip_safe=False,
      install_requires=[
          'pyvod.pluzz',
          'pyvod',
          'lxml',
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      pypluzz = vod.pluzz.pluzz:main
      """,
      )

if "install" in sys.argv:
    print("""
Python Pluzz VOD downloader is now installed!
""")
