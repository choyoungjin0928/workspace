case_1 = ["A", "B", "C", "D"]
case_2 = ["D", "E", "F", "G"]

result = [[a+b for a in case_1] for b in case_2]
print(result)
