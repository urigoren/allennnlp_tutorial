import json, shutil, sys, os
from allennlp.commands import main

experiment_name = "demo"

config_file = "experiments/{e}.jsonnet".format(e=experiment_name)
serialization_dir = "target/{e}".format(e=experiment_name)

if not os.path.exists("target"):
    os.mkdir("target")

# Assemble the command into sys.argv
sys.argv = [
    "allennlp",  # command name, not used by main
    "train", config_file,
    "-s", serialization_dir,
    "--include-package", "src",
]

if __name__=="__main__":
    shutil.rmtree(serialization_dir, ignore_errors=True)
    main()
