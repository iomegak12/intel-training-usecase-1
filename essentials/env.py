import os

firstName = os.environ.get('FIRST_NAME', 'Rob')
lastName = os.environ.get('LAST_NAME', 'Dohanyos')

print('Your Name : %s %s' % (lastName, firstName))
