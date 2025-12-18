def deep_update(base_dict, update_dict):
    for k, v in update_dict.items():
        if isinstance(v, dict):
            base_dict_value = base_dict.get(k)

            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, v)
            else:
                base_dict[k] = v
        else:
            base_dict[k] = v
    return base_dict