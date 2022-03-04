def greet(employeeId, name, *skills):
    print('Hello, ' + name)
    print('Employee Id : ' + employeeId)

    print('Analyzing your skills ...')

    for skill in skills:
        print('Skill : ' + skill)


greet('E10001', 'John Flanders', "C++", 'Python', 'Rust')
