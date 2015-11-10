from setuptools import setup

setup(name='arduino_reddit',
      version='1',
      description='Program to Check for new Reddit messages and output to LED on Arduino',
      url='https://github.com/hemanth42/Arduino-Reddit',
      author='Hemanth A',      
      license='MIT',
      packages=['arduino_reddit'],
      install_requires=[
          'praw','pyserial'],
      zip_safe=False)
