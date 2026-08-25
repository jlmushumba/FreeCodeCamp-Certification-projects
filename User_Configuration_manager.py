def add_setting(setting_dict, key_value_tuple):
    key, value = key_value_tuple[0].lower(), key_value_tuple[1].lower()
    if key in setting_dict.keys():
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")

    else:
        setting_dict.update({key : value})
        return (f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(setting_dict, key_value_tuple):
    key, value = key_value_tuple[0].lower(), key_value_tuple[1].lower()
    if key in setting_dict.keys():
        setting_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    elif not key in setting_dict.keys():
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(setting_dict,key):
    key = key.lower()
    if key in setting_dict.keys():
        del setting_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
    
def view_settings(setting_dict):

    if not setting_dict:
        return "No settings available."
    else:
        output = "Current User Settings:\n"
        for key, value in setting_dict.items():
            output += f"{key.capitalize()}: {value}\n"
        return output 

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "language": "english",
    "autosave": "true"
}   




  