conds = [False, False, False]
print(f"{any(conds)}")  # False

conds = [False, False, False, True]
print(f"{any(conds)}")  # True

conds = []
print(f"{any(conds)}")  # False!!
