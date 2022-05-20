Validation
==========

We can use the same script we use in github actions to locally validate experiment files. This script can be found
in ``utils/validation/scripts/validation.py`` in this repository.

Calling

.. code-block:: bash
    
    python utils/validation/scripts/validation.py --file experiments/test.yaml


we will be validating as experiment the contents of ``test.yaml``.

Calling the script without --file will validate all the yaml files contained in ``experiments/`` folder that were
changed in the current working tree and the main branch tree. We use this functionality in the github action
validation pipeline.

Validation schema
-----------------

show here the schema against which we validate our experiment
Work in progress...

Keywords validation
-------------------

To validate that all the keywords present in the experiment file are described in the glossary, we can use another validation script.
This script can be found
in ``utils/validation/scripts/keywords_validation.py`` in this repository.
Calling

.. code-block:: bash
    
    python utils/validation/scripts/keywords_validation.py

will simply notify you if any of the keywords are unexplained.