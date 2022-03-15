import yaml

with open('./complex.yaml', mode='r') as file:
    documents = yaml.load_all(file, Loader=yaml.FullLoader)

    for document in documents:
        programs = document["host"]["programs"]

        for program in programs:
            program["name"] = program["name"].upper()

        with open('./1.txt', mode='w') as output:
            yaml.dump(document, output)
