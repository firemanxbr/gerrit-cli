#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands

projects = ['dmos-docs', 'dmos-buildroot', 'dmos-dmtdd', 'devops-testbed',
            'devops-tests', 'devops-docs', 'dmos-example']

gerrit_url = 'https://marcelo.barbosa@gerrit.ped.datacom.ind.br/'

def runCommand(command):
    """
    Run any command with its arguments
    """
    return commands.getstatusoutput(command)


if __name__ == "__main__":
    #runCommand("touch", "eu")

    for index in range(len(projects)):
        command = 'git clone %s%s' % (gerrit_url, projects[index])
        print command
        runCommand(command)





"""
 -  Adicionado o tipo de repositório pythonlib na documentação sobre criação de repositórios no Gerrit.
    Commit: f0fbe3f9c82cee77d2079c80d92f9538ef1800d4
    Author: Daiane.Fraga <daiane.fraga@datacom.ind.br>

 -  Remoção da documentação sobre inventory memory, uma vez que a mesma foi levada para o módulo dmos-hal-inventory.
    Commit: 6324734418992b115e8eb757aa586349c41ce168
    Author: Lucas.Gerhard <lucas.gerhard@datacom.ind.br>
"""



