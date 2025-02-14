
import yaml
import os
import json
def make_yaml():
    query = [{'treename': {'nominal': 'modified'}, 'filter_name': ['lbn']}]
    with open(os.path.join(os.environ.get("CONFIG_LOC"), "reco.yaml"), 'w') as reco:
        yaml.dump(query, reco, default_flow_style=False)
    