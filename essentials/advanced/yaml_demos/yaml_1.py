import yaml

with open('./items.yaml', mode='r') as file:
    documents = yaml.load_all(file, Loader=yaml.FullLoader)

    for document in documents:
        for key, value in document.items():
            print(f'Key : {key}, Value: {value}')

