from time import sleep

def name(name='asd'):
    try:
        for i in range(500):
            print(f'My name is {name}')
            sleep(2)
    except:
        print('asdasdasda')


def age(age=0):
    for i in range(500):
        print(f"I'm {age} years old")
        sleep(2)

