var distro_name;
var distro_name;
var es_url;
var index_name;

function preInit() {
    indexes = {};
    axios.get('meta_data.json')
        .then(function(response) {
            let versions = response.data['versions'];
            distro_name = response.data['distro'];
            es_url = response.data['es_url'];
            index_name = response.data['index_name'];
            let url = new URL(window.location.href);
            let searchText = url.searchParams.get('search-term');
            let version = url.searchParams.get('version');
            console.log(versions);
            let selectOptions = [];
            for (let i = 0; i < versions.length; i++) {
                console.log('data_' + versions[i]);
                selectOptions.push(`<option value="${versions[i]}">${versions[i]}</option>`);
            }
            $('select').html(selectOptions);
            if (version) {
                $('select').val(version);
            }
        })
        .catch(function(error) {
            console.log(error);
            alert("Something went wrong!");
        });
}


let onSearch = function(searchText) {
    return new Promise(function(resolve, reject) {
        let url = `http://${es_url}/${index_name}/doc_content/_search?size=10000`;
        let query = {
            "query": {
                "bool": {
                    "must": [{
                            "match": {
                                "distro": distro_name
                            }
                        },
                        {
                            "match": {
                                "version": $('select').val()
                            }
                        }
                    ],
                    "should": [{
                            "match": {
                                "title": searchText
                            }
                        },
                        {
                            "match": {
                                "content": searchText
                            }
                        }
                    ]
                }
            }
        }
        this.axios.post(url, query).then(function(response) {
            let results = response.data.hits.hits.map(function(value) { return { doc: value._source }; })
            resolve(results);
        });
    });
}

initPlugin(preInit, onSearch);