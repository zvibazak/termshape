from setuptools import setup
import codecs
import os.path

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
  name = 'termshape',         
  packages = ['termshape'],   
  version = get_version("termshape/termshape.py"),      
  license='MIT',
  description = 'Tremshape is a minimalistic Python packgage, that only prints basic shapes on terminal.',   
  long_description=long_description,
  long_description_content_type="text/markdown",  
  author = 'Zvi Bazak',
  author_email = 'zvibazak@gmail.com',
  url = 'https://github.com/zvibazak/termshape',
  download_url = 'https://github.com/zvibazak/termshape/archive/v_0.0.2.tar.gz',
  keywords = ['terminal', 'shape'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
