teams = {"Toronto":"Raptors" , "LA":"Lakers", "Chicago":"Bulls"} 
t =dict()
t1={}
t["bread"]=1
t["fruits"]= 5
t["milk"] = 2

print(t["fruits"])
print(t.get("fruits"))

for itm ,qty in t.items() :
    print (qty , itm)

for k  in teams.keys():
    print(k)

for v  in teams.values():
    print(v)
MLB_team = dict([
     ('Colorado', 'Rockies'),
     ('Boston', 'Red Sox'),
     ('Minnesota', 'Twins'),
     ('Milwaukee', 'Brewers'),
     ('Seattle', 'Mariners')
 ])
x = {1, 2, 3, 4, 5}
x.issubset(x)
#  tuple =() , list =[] , dictionary = {} , set ={<iter>} , x = frozenset(['foo', 'bar', 'baz'])