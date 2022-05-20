# Validation

We can use the same script we use in github actions to locally validate experiment files. This script can be found
in `utils/validation/scripts/validation.py` in this repository.

Calling
```
python utils/validation/scripts/validation.py --file experiments/test.yaml
```
we will be validating as experiment the contents of `test.yaml`.

Calling the script without --file will validate all the yaml files contained in `experiments/` folder that were
changed in the current working tree and the main branch tree. We use this functionality in the github action
validation pipeline.

## Validation schema

Accepeted
The schema against which we validate our experiment is as follows
`keywords`: Array accepting keyword values present in `utils/validation/keywords.yaml`
Work in progress...