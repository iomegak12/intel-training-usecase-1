employee_detail = {
    'employee_id': 1,
    'employee_name': 'Jon Flanders',
    'work_location': 'New York',
    'skills': ['C++', 'Python', 'Rust'],
    'projects': [
        {
            'project_id': 'PRJ10001',
            'project_title': 'Project X',
            'project_budget': 248983
        },
        {
            'project_id': 'PRJ10001',
            'project_title': 'Project Z',
            'project_budget': 500000
        }
    ]
}

print(employee_detail['work_location'])

skills = employee_detail['skills']

for skill in skills:
    if skill == 'Rust':
        print('Awesome Employee!')
        break

# comprehension syntax [statement loop condition]
filteredSkills = [x.upper() for x in skills if x in ['Rust', 'C']]

print(filteredSkills)

for project in employee_detail['projects']:
    if project['project_budget'] >= 500000:
        print(project['project_title'])

