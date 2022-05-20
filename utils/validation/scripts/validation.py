import re

import yamale
from git import Repo
from yaml import YAMLError
import click


keywords_file = 'utils/validation/keywords.yaml'

@click.command()
@click.option('--file', help='Path to the file to validate.')
def validate(file):
    try:
        experiment_schema = yamale.make_schema("utils/validation/schemas/experiment.yaml")
        if file:
            experiments_files = [file]
        else:
            repo = Repo(".")
            files = repo.git.execute(["git", "diff", "--name-only", "origin/main"]).split("\n")
            experiments_re = re.compile(r"^experiments\/.+")
            experiments_files = list(
                filter(lambda filename: bool(experiments_re.match(filename)), files)
            )
        for experiment in experiments_files:
            experiment_data = yamale.make_data(experiment)
            yamale.validate(experiment_schema, experiment_data)
            # validate keywords
            valid_keywords = yamale.make_data(keywords_file)[0][0]['keywords']
            keywords = experiment_data[0][0].get("keywords")
            all_kw_valid = all(map(lambda kw: kw.lower() in list(map(lambda valid_kw: valid_kw.lower(), valid_keywords)), keywords))
            if all_kw_valid == False:
                raise YAMLError("Experiment contains invalid keywords")
            # validate dataset and response
            n_runs = experiment_data[0][0].get("run_size")
            dataset = experiment_data[0][0].get("dataset")
            response = experiment_data[0][0].get("response", None)
            # Validate dataset size
            for data in dataset:
                coded_data = data.get("coded")
                uncoded_data = data.get("uncoded", None)
                if len(coded_data) != n_runs:
                    raise YAMLError("Mismatch in dataset coded data and number of runs")
                if uncoded_data and len(uncoded_data) != n_runs:
                    raise YAMLError("Mismatch in dataset uncoded data and number of runs")
            # Validate response size
            if response:
                for data in response:
                    value = data.get("value")
                    if len(value) != n_runs:
                        raise YAMLError("Mismatch in response values and number of runs")
        print("Validation success! 👍")
    except Exception as e:
        print("Validation failed!\n%s" % str(e))
        exit(1)


if __name__ == "__main__":
    validate()