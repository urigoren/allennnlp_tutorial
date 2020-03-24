rm -r output
allennlp train experiments/demo.jsonnet -s output --include-package src
