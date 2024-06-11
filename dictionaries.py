# lokesh={1:"name",2:"age"}
# print(type(lokesh))
# print(lokesh[1])
# lokesh[1]="reddy"
# print(lokesh)

reddy={"sno":1,"name":"loki","age":21}
#print(reddy.clear())
ram=reddy.copy()
print(ram)
print(ram.get("name"))
print(ram.items())
print(ram.keys())
print(ram.values())
ram.update({"name":"sai"})
print(ram)
ram.update({"gender":"male"})
print(ram)
ram.pop("sno")
print(ram)

ps={1:"reddy","age":23,"gender":"male"}
for i in ps:
    print(i)

sp={1:"reddy","age":23,"gender":"male"}
for i,j in sp.items():
    print(i,j)

lok={
    1:"a",
    2:"b",
    3:{1:"aa"}
}
print(lok)
print(lok[3][1])
