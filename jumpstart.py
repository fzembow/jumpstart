#!/usr/bin/env python

import sys, os, json, shutil, pyratemp
import messages

current_dir = os.getcwd() + "/"
script_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
templates_dir = script_dir + "templates/"

def init():

    #check for no arguments
    if len(sys.argv) == 1:
        list_apps()
        sys.exit(1)

    #check for command
    app_name = sys.argv[1].lower()

    #get name of desired app
    if not os.path.exists(templates_dir + app_name):
        print messages.non_existent_app
        list_apps()
        sys.exit(1)

    app_dir = templates_dir + app_name + "/"

    #load configuration
    try:
        fp = open(app_dir + "jumpstart.json", "r")
    except IOError:
        print messages.missing_conf % app_name
        sys.exit(1)

    #parse configuration into dictionary
    try:
        conf = json.load(fp)
    except ValueError:
        print messages.invalid_conf % (app_dir + "jumpstart.json")
        sys.exit(1)

    #process the configuration and create the new app
    process_app(conf, app_dir)

def process_app(conf, app_dir):

    #get the name from the user
    print "please provide a name for your application (default: %s)" % conf["name"]
    name = raw_input("> ")
    if len(name) == 0:
        name = conf['name']
    
    params = process_variables(conf)
    params['name'] = name

    #create destination folder
    dest_dir = current_dir + params['name'] + "/"
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    #process files that should be created
    try:
        for file in conf["create_files"]:

            #see if the file has a name derived from a variable
            try:
                try:
                    name = file["name"] % params["name"]
                except TypeError:
                    name = file["name"]
            except KeyError:
                name = file["template"]

            file_name = file["template"]
            if os.path.exists(app_dir + file_name):
                #copy existing file
                t = pyratemp.Template(filename=app_dir + file_name)
                result = t(**pyratemp.dictkeyclean(params))

                f = open(dest_dir + name, "w")
                f.write(result.encode("utf-8"))
                f.close()
            else:
                #create blank file
                f = open(dest_dir + name, "w")
                f.write("")
                f.close()
    except KeyError:
        pass

def process_variables(conf):

    params = {}
    try:
        for var in conf["variables"]:
            #process boolean variables
            if var['type'] == "Boolean":
                if var["default"] == "True":
                    default_str = "y"
                    default_bool = True
                else:
                    default_str = "n"
                    default_bool = False
                accepted_inputs = {"y":True,"yes":True,"n":False,"no":False,"": default_bool}
                val = None
                while val not in accepted_inputs.keys():
                    print var["description"] + " (y/n) (default: %s)" % default_str
                    val = raw_input("> ")
                params[var['name']] = accepted_inputs[val]
            elif var['type'] == "String":
                print var["description"] + " (default: %s)" % var["default"]
                val = raw_input("> ")
                if val == "":
                    val = var["default"]
                params[var['name']] = val

    except KeyError:
        pass

    return params

def create_new_app():
    pass

def list_apps():
    print messages.list_apps
    folders = os.listdir(templates_dir)
    for folder in folders:
        print folder
    print

if __name__ == "__main__":
    init()
