from setuptools import setup, find_packages

setup(
        name="polygrid",
        version="0.1",
        author="Luke Macken",
        author_email="lmacken@redhat.com",
        install_requires=[
            'knowledge',
            'tw2.jquery',
        ],
        packages=find_packages(exclude=['ez_setup']),
        zip_safe=True,
      )
