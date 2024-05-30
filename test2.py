import random

print("hallo welt")

test = 42

print(range(20))

x = random.randint(1, 10)
print(x)

if x < 5:
    print("python kaput")
else:
    print("ales gut")

liste = ["dies", "ist", 5, "eine", "liste"] + ["und", "noch", "eine"]
print(liste)

d = {"Mia": "Marvin", "Marvin": "Mia"}
print(d["Mia"])
print(d["Marvin"])
d["Mia"] = "toll"
d["Marvin"] = "noch toller"
print(d["Mia"])
print(d["Marvin"])

name = 5.5
Name2 = name * 2
print(Name2)

if 3 < 4:
    print("richtig")
