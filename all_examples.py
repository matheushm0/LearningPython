conds = [True, True, True]
print(f"{all(conds)}")  # True

conds = [True, True, True, False]
print(f"{all(conds)}")  # False

conds = []
print(f"{all(conds)}")  # True!!
