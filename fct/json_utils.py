
def insert_to_json(target_json, key, value, key_type, key_mode, key_upper):
    node_list = key_upper.split("/")
    try:
        if key_upper == "" or node_list[1] == "":
            target_json = set_value(target_json, key, value, key_type)
            return target_json
        else:
            if not is_node_exist(target_json, "/"+node_list[1]):
                target_json[node_list[1]] = {}
            else:
                pass
            new_key_upper = key_upper[len(node_list[1]) + 1:]
            target_json[node_list[1]] = insert_to_json(target_json[node_list[1]], key, value, key_type, key_mode, new_key_upper)
            return target_json
    except Exception as e:
        return target_json


def is_node_exist(target_json, node):
    if node == "/":
        return True
    node_list = node.split("/")
    try:
        if len(node_list) == 2:
            return node_list[1] in target_json.keys()
        else:
            if node_list[1] in target_json.keys():
                node = node[len(node_list[1])+1:]
                return is_node_exist(target_json[node_list[1]], node)
            else:
                return False
    except Exception as e:
        return False


def set_value(target_json, key, value, key_type):
    if key_type == "obj":
        if is_node_exist(target_json, "/"+key):
            return
        else:
            target_json[key] = {}
    elif key_type == "int":
        target_json[key] = int(value)
    elif key_type == "str":
        target_json[key] = value
    elif key_type == "bool":
        target_json[key] = True if key_type in ("True", "true") else False
    elif key_type == "null":
        target_json[key] = None
    else:
        target_json[key] = value
    return target_json
