from jinja2 import Template

fileName = './template.txt'

with open(fileName, mode='r', encoding='utf-8') as file:
    fileContents = file.readlines()
    templateContents = "".join(fileContents)
    template = Template(templateContents)
    
    data = {
        "hostname": "RAMTHINKPAD",
        "name_server_primary": "1.1.1.1",
        "name_server_secondary": "10.82.83.23",
        "ntp_server_primary": "0.pool.server1",
        "ntp_server_secondary": "0.pool.server2"
    }

    output = template.render(data)

    print(output)
