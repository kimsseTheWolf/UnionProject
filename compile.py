import os

compile_file_list = [
    "about_eventTrigger.py",
    "category_list_eventTrigger.py",
    "category_properties_eventTrigger.py",
    "create_category_eventTrigger.py",
    "create_file_eventTrigger.py",
    "create_project_eventTrigger.py",
    "export_category_eventTrigger.py",
    "file_list_eventTrigger.py",
    "finished_project_eventTrigger.py",
    "import_file_eventTrigger.py",
    "modify_category_eventTrigger.py",
    "modify_project_eventTrigger.py",
    "project_list_eventTrigger.py",
    "project_properties_eventTrigger.py",
    "settings_eventTrigger.py"
]

for i in compile_file_list:
    command = "pyinstaller -i .\\GUI\\Others\\Icon\\logo.ico -n "+i+" -w -F .\\"+i
    os.system(command)