from Lab1.method_add import add_algorithm
from Lab1.method_drop import drop_algorithm

c = [2, 7, 3, 9]

T = [
    [5, 2, 4],
    [1, 3, 2],
    [4, 1, 4],
    [2, 5, 1]
]

z_drop, f_drop = drop_algorithm(c, T)
z_add, f_add = add_algorithm(c, T)

print(f"DROP: z = {z_drop}, F = {f_drop}")
print(f"ADD:  z = {z_add}, F = {f_add}")