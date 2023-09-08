file_path = ""
text = ""
result = "ID\tSymbol\n"

with open(file_path, "r") as f:
    text = f.read()
lines = text.split("\n")
for line in lines:
    if line == lines[0]:
        continue
    try:
        if str(line)[0] == "#":
            continue
        t = line.split("\t")

        id = t[0]
        symbol = t[10]
        if symbol == "Gene Symbol":
            continue
        else:
            if t[10].find("///"):
                symbol = t[10].split("///")[0]
            result += id + "\t" + symbol + "\n"
    except Exception:
        print(line)
with open(file_path + ".result", "w") as f:
    f.write(result)
