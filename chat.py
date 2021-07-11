def read_file(filename):
    lines = []
    with open(filename, 'r',encoding= 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())   #.strip()去掉換行符號
    return lines   

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == "劉倩怡Iris Liu":
            person = "劉倩怡Iris Liu" #把人名存進person
            continue
        elif line == "滋玲Giselle":
            person = "滋玲Giselle"
            continue
        if person :       
            new.append(person + ": " + line )   #append把東西裝進清單內，+是字串的合併
    return new

def write_file(filename, lines):
    with open(filename, 'w',encoding= 'utf-8') as f:
        for line in lines:
            f.write(line+ '\n')
    
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
    
main()    


    
