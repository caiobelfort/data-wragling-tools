from setuptools import setup

setup(
    name='data-wragling-tools',
    version='0.0.1',
    description='Utils for pipeline creation with pandas',
    author='Caio Belfort',
    author_email='caiobelfort90@gmail.com',
    license='GPL',
    py_modules=['data_wragling_tools'],
    zip_safe=False,
    install_requires=['pandas'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Database :: Data Engineering',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Operation System :: POSIX'
    ]
)
