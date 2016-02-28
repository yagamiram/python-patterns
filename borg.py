#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This is an example of singletone class. Only one instance for the class.
But the singleton is achieved in different way

You are allowed to created as many instance for a class but the instances wont be unique. 
The instances are shared to each other so if you make any changes it will affect all other instances.

How this is achieved?
By declaring a variable outside the class and refering it to the memeber variable declared inside the init function.

Here, the __shared_state dict is declared outside the init fn and it is pointed by the variabel __dict__ which is declared
inside the init function. 

How come this helps to achieve singleton ?
https://stackoverflow.com/questions/1537202/variables-inside-and-outside-of-a-class-init-function/1537226#1537226

Variable set outside __init__ belong to the class. They're shared by all instances.

Variables created inside __init__ (and all other method functions) and prefaced with self. belong to the object instance.

And pointing the shared variable by a variable declared inside the init fn made all instance of the class as one single instance.
'''

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

### OUTPUT ###
# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 140732837899224
# rm2 id: 140732837899296
# rm1: Init
# rm2: Init
# rm3: Init
