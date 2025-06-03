import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

tests_require = [
    'pytest>=6.0.0',
    'pytest-django>=4.1.0',
    'factory-boy>=3.0.0',
]

setuptools.setup(
      name='django_serverside_datatable',
      version='2.1.0',
      description="Simple Server-side Datatable processing view for Django",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/umesh-krishna/django_serverside_datatable",
      license="MIT",
      author="Umesh Krishna",
      author_email='umesh_krishna@outlook.com',
      install_requires=['Django>=1.11'],
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      tests_require=tests_require,
      test_suite="tests",
)
