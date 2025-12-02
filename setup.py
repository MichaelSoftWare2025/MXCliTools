from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='MXCliTools',
  version='0.0.1',
  author='Michael D',
  author_email='studiosoftware7@gmail.com',
  description='Easy create cli apps.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  #install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='cli',
  #project_urls={
  #  'GitHub': 'your_github'
  #},
  python_requires='>=3.11'
)