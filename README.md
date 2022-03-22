# 📝 qclist - Quick Check List
- Date: 3-22-2022

## About:
- We all have a list of websites and applications we check on a daily basis. But, sometimes its a pain to open all those links and apps as well as remember what those links and apps are. This is were qclist comes in. Make a json file with with your links/sources and run the python script to automate your daily check list of websites and apps.

## Requirements:
- OS Supported:
    - MacOS
    - Linux Distros:
        - Ubuntu
        - most other distros should work...
- Software:
    - Python 3
    - any browser...

## How To Use:
0) Make sure your doing this on a Unix based system (MacOS or Linux).
1) Git clone this repo and cd into this repo.
2) Make sure the *targets/* directory is in the repo you cloned. If not, create that directory with the following command:
    ```
    mkdir targets
    ```
3) Go into the **targets/**. Here, you will create a json file with all the sources (links and/or applications) you want to "quickly check"/open. Here is the format the json file should be in:
    - type layout:
        ```
        <list> [
            <string>,
            ...
        ]
        ```
    - real layout example:
        ```
        [
            "https://github.com/",
            "https://gitlab.com/"
        ]
        ```
4) After you created/edited your json files in **targets/**, please take a look at the **config.json** file. In this file, please set the *open_command* value eqaul to your operating system's "open" command. The open command is a commend used by the terminal to open a file or directory though your OS's gui. Here are some of the "open" commands for certain operating systems:
    - MacOS: "open"
    - Ubuntu: "xdg-open"
5) After setting your operating system's "open" command in the config.json file, you can change the *print_source_info* from true to false if you don't want the terminal to print stuff when qclist is running.
6) After all these steps, run the main.py script to run qclist:
    ```
    python3 main.py
    ```
7) (optional) If you want, you can make an alias for qclist and save that alias to your zshrc or bashrc file. Here is a possible alias/command you can add to your zshrc/bashrc file:
    ```
    qclist () {
        python3 <path_to_dir>/qclist/main.py
        exit
    }
    ```

