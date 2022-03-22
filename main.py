import os.path
import pathlib
import json
import os

# load config file for this script!
config = {}
CONFIG_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "config.json")
with open(str(CONFIG_PATH), 'r') as file:
    config = json.load(file)

def load_json(path):
    if os.path.exists(str(path)) == True:
        with open(str(path), 'r') as file:
            data = json.load(file)
        return data
    else:
        return None

def open_cmd(arg):
    output = -1
    try:
        cmd = str(config["open_command"]) + " " + str(arg)
        output = os.system(cmd)
    except:
        pass
    return output

def loop_open_cmd(data, json_file_name):
    if type(data) == list:
        for i in data:
            code = open_cmd(i)
            if config["print_source_info"] == True:
                print("Filename: " + str(json_file_name))
                print("Channel:  " + str(i))
                print("Status:   " + str(code))
                print()
    else:
        print("loop_open_cmd() : error, invalid param type provided!")

def filter_list(data, contains):
    output = []
    if type(data) == list:
        for line in data:
            if str(contains) in line:
                output.append(line)
    
    if len(output) != 0:
        return output
    else:
        return None

if __name__ == "__main__":
    try:
        script_dir = pathlib.Path(__file__).parent.resolve()
        script_dir = os.path.join(script_dir, "targets")
        all_files = os.listdir(script_dir)
        json_file_names = filter_list(all_files, "json")
        if json_file_names != None:
            for jfile in json_file_names:
                path = os.path.join(script_dir, jfile)
                if os.path.isfile(path):
                    data = load_json(path)
                    if data != None:
                        loop_open_cmd(data, jfile)
    except KeyboardInterrupt:
        pass



