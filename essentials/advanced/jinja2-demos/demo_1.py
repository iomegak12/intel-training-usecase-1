from jinja2 import Template

template = "Hello {{ greeting }}"

data = {
    "greeting": "Ramkumar J Damodaran"
}

j2_template = Template(template)

print(j2_template.render(data))
