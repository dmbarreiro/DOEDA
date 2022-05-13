"""
Generate the skeleton of a JSON document, based on the contents of the csv file.

The csv file should:
- contain one row per experimental run
- contain one column per factor
- have its last column as the response
- have its first row contain the variable names
"""

import click
import pandas as pd
import numpy as np
import json
import os


@click.command()
@click.argument("filename")
@click.option(
    "--no-header",
    default=False,
    is_flag=True,
    show_default=True,
    help="Flag. Variable names are not in first row of csv file.",
)
@click.option(
    "--coded",
    default=False,
    is_flag=True,
    show_default=True,
    help="Flag. Factor levels are in coded form.",
)
@click.option(
    "-t",
    "--title",
    type=str,
    default=None,
    help="Title of the experiment. Filename is used if none is given.",
)
def main(filename, no_header, coded, title):
    """
    Read the contents of the csv file FILENAME to generate the skeleton experiment file.
    It is assumed that the full path of the csv file is "../csv/FILENAME", so that only the filename has to be provided.
    Save the output file to a YAML file in '../yml' folder.
    """
    # Options for loading the csv file
    if no_header:
        header = None
    else:
        header = 0
    # Full path of the csv file
    full_path = os.path.join("../csv", filename)
    # Loading file to a dataframe to keep column name
    df = pd.read_csv(full_path, header=header, index_col=None)
    # Only dict are written to yaml
    data_dict = dict()
    # Infer title from filename
    if title is None:
        exp_title = filename.replace(".csv", "").replace("_", " ").replace("-", " ")
    else:
        exp_title = title
    data_dict["title"] = exp_title
    # Run size and n_factors given by the matrix dimensions
    data_dict["runsize"] = df.shape[0]
    # For each variable in df, gather characteristics
    data_dict["design"] = []
    for factor_name in df.columns[:-1]:  # index by column names
        if coded:
            column = None
            coded_column = df[factor_name].to_list()
            levels = np.unique(column)
        else:
            column = df[factor_name].to_list()
            levels = np.unique(column)
            # Rule for recoding the factor levels
            rule = dict()
            for i, x in enumerate(levels):
                # Levels are -1, 0, 1 if it's a three-level factor
                idx = i - 1 if len(levels) == 3 else i
                rule[x] = idx
            # Recode the column
            coded_column = [rule[x] for x in column]
        factor = {
            "name": factor_name,
            "uncoded": column,
            "coded": coded_column,
            "levels": len(levels),
            "units": "NA",
        }
        data_dict["design"].append(factor)
    # Check if multilevel by comparing the number of factors
    n_levels = [i["levels"] for i in data_dict["design"]]
    data_dict["multilevel"] = len(np.unique(n_levels)) > 1
    # For now, description, keywords and DOI are not infered from the file
    data_dict["description"] = None
    data_dict["keywords"] = []
    data_dict["doi"] = None
    # Save experiment data to yaml file, use filename as path
    output_path = os.path.join("../yml", filename.replace(".csv", ".yml"))
    with open(output_path, "w") as file:
        json.dump(data_dict, file, indent=2)


if __name__ == "__main__":
    main()
