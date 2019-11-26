from setuptools import setup, find_packages

setup(name='c_test',
      version='0.1',
      description='Система сбора информации',
      long_description="README.txt",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
        'Framework :: Django',
      ],
      keywords='сбор информации загрузка процессора',
      url='http://github.com/iminlan/c_test',
      author='Anny',
      author_email='Ann.bakhteeva@gmail.com',
      license='',
      packages=find_packages(),
      install_requires=[
          '',
      ],
      include_package_data=True,
      zip_safe=False)