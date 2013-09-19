'''
Created on 17 Sept 2013

@author: don Najd
@description: Nao will act autonomously
'''
from __future__ import print_function
import naoutil.naoenv as naoenv
import naoutil.memory as memory
import fluentnao.nao as nao
from naoutil import broker


#########################
# SETUP
######################### 

# Broker (must come first)
broker.Broker('bootstrapBroker', naoIp="nao.local", naoPort=9559)

# FluentNao
env = naoenv.make_environment(None)
log = lambda msg: print(msg) # lambda for loggin to the console
nao = nao.Nao(env, log)

#########################
# GO
######################### 

# create greeter
greeter = Greet(nao)

# subscribe to face recog
faceRecog = FaceRecog(nao, memory)
faceRecog.add_subscriber(greeter)