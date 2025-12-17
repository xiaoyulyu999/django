import yaml

def yaml_coerce(stream):

    if type(stream) == str:
        return yaml.safe_load(f'dummy: {stream}')['dummy']
    return stream