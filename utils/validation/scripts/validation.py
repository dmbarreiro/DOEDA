import yamale
from git import Repo
import re

try:
    experiment_schema = yamale.make_schema("utils/validation/schemas/experiment.yaml")
    repo = Repo(".")
    files = repo.git.execute(["git", "diff", "main", "HEAD", "--name-only"]).split("\n")
    experiments_re = re.compile(r"^experiments\/.+")
    experiments_files = list(
        filter(lambda filename: bool(experiments_re.match(filename)), files)
    )
    for experiment in experiments_files:
        experiment_data = yamale.make_data(experiment)
        yamale.validate(experiment_schema, experiment_data)
    print("Validation success! 👍")
except Exception as e:
    print("Validation failed!\n%s" % str(e))
    exit(1)
