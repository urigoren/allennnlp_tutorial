import json, shutil, sys

from allennlp.commands import main

config_file = "experiments/demo.jsonnet"

CUDA_LAUNCH_BLOCKING=1
serialization_dir = "output"

# Assemble the command into sys.argv
sys.argv = [
    "allennlp",  # command name, not used by main
    "train", config_file,
    "-s", "output",
    "--include-package", "src",
]

if __name__=="__main__":
    shutil.rmtree(serialization_dir, ignore_errors=True)
    main()
