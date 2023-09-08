file_path = ""
symbol_path = "
text = ""
with open(symbol_path,"r") as f:
    text = f.read()
lines = text.split("\n")
symbol_dict = {}
for line in lines:
    try:
        if line != lines[0]:
            line = line.split("\t")
            symbol_dict[line[0]] = line[1]
    except Exception:
        pass
    
with open(file_path,"r") as f:
    text = f.read()
lines = text.split("\n")
result = ""
genes = list()
for line in lines:
    try:
        if line[0] == "!" or line=="":
            continue
        else:
            if line[0:8] == '"ID_REF"':
                for gene in line.split("\t"):
                    if gene != '"ID_REF"':
                        genes.append(gene)
                line = line.replace(line[0:8],"")
                result += line + "\n"
                continue
            else:
                t = line.split("\t")
                symbol = symbol_dict[t[0].replace('"','')]
                new_line = symbol + "\t"
                new_line += line.replace(t[0]+"\t","")
                result += new_line + "\n"
    except Exception:
        pass
with open(file_path+".result","w") as f:
    f.write(result)
