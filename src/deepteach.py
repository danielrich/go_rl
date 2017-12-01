from engine import trainingEngine
from gtp import Engine
import sys

deep_teach_engine  = Engine(trainingEngine())


while(1):
    data = sys.stdin.readline()
    response = deep_teach_engine.send(data)
    print (response)
