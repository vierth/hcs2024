import re
my_string = "This string 2024 has many numbers 18, 25, 2021"

# findall
results = re.findall(r'\d+', my_string)
print(results)

# finditer
results = re.finditer(r'\d+',my_string)
for res in results:
    print(res)