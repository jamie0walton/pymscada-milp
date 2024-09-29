"""Example use."""
from pymscada_milp import LpModel

# max: 20 x1 + 6 x2 + 8 x3;
# 0.8 x1 + 0.2 x2 + 0.3 x3 <=20;
# 0.4 x1 + 0.3 x2 <= 10;
# 0.2 x1 + 0.1 x3 <= 5;
# int x1, x2, x3;
#
# and crucially, on a different page :(
# x3<=20;

m = LpModel()
m.add_row(-20, 'x1', -6, 'x2', -8, 'x3', 'N')  # Negate as default minimizes
m.add_row(0.8, 'x1', 0.2, 'x2', 0.3, 'x3', 'L', 20)
m.add_row(0.4, 'x1', 0.3, 'x2', 'L', 10)
m.add_row(0.2, 'x1', 0.1, 'x3', 'L', 5)
m.add_limit('x1', 'LI', 0)
m.add_limit('x2', 'LI', 0)
m.add_limit('x3', 'UI', 20)
m.write_mps()
m.solve_mps()
print([f'{x} {m.results[x]}' for x in ['x1', 'x2', 'x3']])
m.remove_result()
