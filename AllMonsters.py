from BasicImports import *
def troll_encounter():
    name="troll"
    magic=2
    health=5
    attack=[-1, -2]
    speed=3
    if health<=3:
        critical=True
    else:
        critical=False
    criticalattack=choice(attack)-2
    saying=None
    criticalsaying=["STOP MON YOU HURTIN ME.", "WHY WON'T YOU JUST LET ME KILL YOU.", "RRRRRR"]
    
    
