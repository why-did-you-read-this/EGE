# На числовой прямой даны два отрезка:
# В = [18; 52] и С = [16; 41].
# Укажите наименьшую возможную длину такого отрезка А,
# что логическое выражение
# ((x ∈ B) → (x ∈ A)) ∧ (¬(x ∈ C) ∨ (x ∈ A))
# истинно (т.е. принимает значение 1) при любом значении переменной х.

u = 4
m = 9999999


def f(x, a1, a2):
    B = 18 * u <= x <= 52 * u
    C = 16 * u <= x <= 41 * u
    A = a1 <= x <= a2
    return (B <= A) and ((not C) or A)


for a1 in range(14 * u, 55 * u + 1):
    for a2 in range(a1, 55 * u + 1):
        if all(f(x, a1, a2) for x in range(14 * u, 55 * u + 1)):
            m = min(m, a2 - a1)

print(m / 4)
