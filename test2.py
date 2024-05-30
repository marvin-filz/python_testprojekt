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

d = {"Ich": "Marvin", "Marvin": "Ich"}
print(d["Ich"])
print(d["Marvin"])
d["Ich"] = "das bin ich"
d["Marvin"] = "noch mehr ich"
print(d["Ich"])
print(d["Marvin"])

name = 5.5
Name2 = name * 2
print(Name2)

if 3 < 4:
    print("richtig")
if 3 == 4 or 3 != 4 or 3 < 4 or 3 > 4 or 3 <= 4 or 3 >= 4:
    print("irgendwas ist richtig")

if not 4 < 3:
    if "true":
        print("stimmt nicht")

print(max([1, 4, 5, 8, 5, 20, 6]))
print(min([1, 4, 5, 8, 5, 20, 6]))
