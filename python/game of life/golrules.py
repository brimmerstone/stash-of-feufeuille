
rulestring = "B3/S23"
rules = {}
for i in range(2):
    rules[rulestring.split("/")[i][0]] = [int(n) for n in rulestring.split("/")[i] if n.isdigit()]
"""
rules["B"] — Bear:    0 to 1
rules["S"] — Survive: 1 to 1
else       — Die:     1 to 0
"""

Wd, Ln = 128,64
WdT,LnT = 80,48

gen = 0
gmap = [[0 for X in range(Wd)] for Y in range(Ln)]
nmap = [[0 for X in range(Wd)] for Y in range(Ln)]
mapT = [[0 for X in range(WdT)] for Y in range(LnT)]
nmapT = [[0 for X in range(WdT)] for Y in range(LnT)]

neighbors = [[-1,-1],[-1,0],[-1,1],
             [ 0,-1],       [ 0,1],
             [ 1,-1],[ 1,0],[ 1,1]]

prd1, prd2 = [], []

DISPLAY_DEBUG = 0
SECRET_PARTY  = 0
colors =   ["#C00000","#C03000","#C06000","#C09000",
            "#C0C000","#90C000","#60C000","#30C000",
            "#00C000","#00C030","#00C060","#00C090",
            "#00C0C0","#0090C0","#0060C0","#0030C0",
            "#0000C0","#3000C0","#6000C0","#9000C0",
            "#C000C0","#C00090","#C00060","#C00030"]