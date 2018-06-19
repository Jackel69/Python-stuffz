myinfo = ["Angela","Fred","Trudy",3,4,5]
for name in myinfo:
     print(name)
     
myshopping_list = ["olive oil", "walnuts", "wine"]
print(myshopping_list[2])
     
myshopping_list.append("eggs")
print(myshopping_list)  
 
myshopping_list.remove("eggs")
print(myshopping_list)
print(len(myshopping_list))

colors = ["blue", "red" , "green", "purple","indiago"]

print(colors.index("green"))
colors.insert(2,"yellow")

print(colors)

weather = []
w =raw_input("What is the weather today?")
weather.append(w)
print(weather)