from distutils.core import setup
setup(
  name = 'termshape',         
  packages = ['termshape'],   
  version = '0.0.1',      
  license='MIT',
  description = 'Tremshape is a minimalistic Python packgage, that only prints basic shapes on terminal.',   
  author = 'Zvi Bazak',
  author_email = 'zvibazak@gmail.com',
  url = 'https://github.com/zvibazak/termshape',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['terminal', 'shape'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
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
