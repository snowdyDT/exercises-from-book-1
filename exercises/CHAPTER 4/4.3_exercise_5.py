string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "bEautiful"

result1 = string1.lower().startswith("be")
result2 = string2.lower().startswith("be")
result3 = string3.lower().startswith("be")
result4 = string4.lower().startswith("be")

print(result1, result2, result3, result4)