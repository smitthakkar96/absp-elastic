from setuptools import setup


setup(
    name="ascii_binder_search_elastic_search",
    version="0.0.1",
    author="smit thakkar",
    author_email="smitthakkar96@gmail.com",
    description=("A small utility that would help you to get search in asciibinder"),
    packages=[
                'ascii_binder_search',
                'ascii_binder_search.indexers',
            ],
    license="BSD",
    keywords="Asciibinder, ascii_binder_search, ascii_binder_search_elastic_search",
    url="https://github.com/smitthakkar96/ascii_binder_search_plugin",
    install_requires=['lxml', 'pyyaml', 'xmltodict', 'beautifulsoup4', 'xmltodict', 'elasticsearch'],
    include_package_data=True,
    zip_safe=False,
    namespaces=[
        'ascii_binder_search.indexers'
    ],

)