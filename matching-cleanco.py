from cleanco import cleanco
temp_list = []
temp_list2 = []

with open(r"C:\Users\Kai\Desktop\CB_1719_v2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(len(lines))
for index, line in enumerate(lines):
    print(lines[index])
    temp_list.append(cleanco(lines[index]).clean_name())
    print(temp_list[index])
for index, line in enumerate(temp_list):
    temp_list2.append(''.join(e for e in line if e.isalnum()))
    print(temp_list2[index])
print(len(temp_list2))
with open(r"C:\Users\Kai\Desktop\CB1719_Comps_Cleaned.txt", "w") as f:
    f.write("\n".join(temp_list2))