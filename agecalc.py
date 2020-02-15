print('Fill the details to know how long you have been alive for..')
name= input('Name: ')
print('What is your age',(name),'?')
age=int(input('age: '))

days=age*365
hour=age*8760
minutes=age*525600
seconds=age*31557600

print(name,'has been alive for',days,'days',hour,'hour',minutes,'minutes',seconds,'seconds')
print('Thank you for using my age calculating program')
