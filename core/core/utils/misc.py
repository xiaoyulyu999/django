import yaml

def yaml_coerce(stream):

    if type(stream) == str:
        return yaml.load(f'dummy: {stream}', Loader=yaml.FullLoader)['dummy']
    return stream