"""Check if the list of keywords in validation/ matches the one from the glossary."""
if __name__ == "__main__":
    import re

    # Reference keywords in the yaml file
    with open('utils/validation/keywords.yaml', 'r') as f:
        f.readline()  # --- line
        f.readline()  # header lines
        content = f.readlines()

    ref_keywords = [re.sub(r"\s+-\s+", "", s).strip() for s in content]

    # Keywords detailled in the docs
    with open('docs/source/glossary.rst', 'r') as f:
        l = f.readline()  # Pass header
        while re.search("glossary::", l) is None:
            l = f.readline()
        f.readline()  # Pass blank lines
        content = f.readlines()

    detected_kw = [re.sub(':', '', i).strip()
                   for i in content if re.match("\s{2}[^\s]", i)]
    processed_kw = [re.sub('\s', '-', i.lower()) for i in detected_kw]

    # Check for non-matches
    non_exp_kw = [i for i in ref_keywords if i not in processed_kw]
    if len(non_exp_kw) > 0:
        print('⚠️ Unexplained keywords missing from glossary ⚠️ \n%s' % non_exp_kw)
        raise('⚠️ Unexplained keywords missing from glossary ⚠️ \n%s' % non_exp_kw)
    else:
        print('All keywords are explained in the glossary 👍')
