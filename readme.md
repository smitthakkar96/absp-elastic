# ABSP Elastic Search Indexer

## What is this?
This is an extension to [AsciiBinder Search Plugin](https://github.com/gluster/ascii_binder_search_plugin)
which can help you to index data to elastic search and implement search in frontend by calling elastic search api.

## Installation instructions
1. Make sure you have a working installation of python3

1. Create a virtualenv

        python3 -m venv <name of virtualenv>

1. Activate the virtualenv

        source <name of virtualenv>/bin/activate

1. Install

        pip install git+https://github.com/smitthakkar96/absp-elastic


## Usage
After successful installation it's time to give this plugin a try. Use **elastic-indexer** when specifiying indexer with flag ``` -i ```.

#### Example:

```
ascii_binder_search -i elastic_search -e <elastic_search_url> --index-name <index_name>
```
