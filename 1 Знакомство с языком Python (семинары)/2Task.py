# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("X Y Z  Itog")
for x in range(2):
    for y in range(2):
        for z in range(2):
            itog = 0
            if not (x or y or z) == (not x and not y and not z):
                itog = 1
            print(f"{x} {y} {z}  {itog}")
