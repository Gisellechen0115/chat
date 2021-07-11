def read_file(filename):
    lines = []
    with open(filename, 'r',encoding= 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())   #.strip()去掉換行符號
    return lines   

def convert(lines):
    person = None
    name1_world_count = 0
    name2_world_count = 0
    name1_sticker_count = 0
    name2_sticker_count = 0
    name1_image_count = 0
    name2_image_count = 0
    for line in lines:
         s = line.split(" ")
         time = s[0]
         name = s[1]
         if name == "許自佑":
             if s[2:] == "貼圖":
                name1_sticker_count += 1
             elif s[2:] == "貼圖": 
                  name1_image_count += 1
             else:
                 for m in s[2:]:
                     name1_world_count += len(m)
         elif name =="滋玲Giselle":
              if s[2] == "貼圖":
                name2_sticker_count += 1
              elif s[2:] == "貼圖": 
                 name2_image_count += 1  
              else:   
                 for m in s[2:]:
                     name2_world_count += len(m) 
    print('yo siad:',name1_world_count,'傳了 ',name1_sticker_count,'個貼圖, 傳了幾張圖片', name1_image_count )
    print('Giselle siad:', name1_world_count,'傳了 ', name2_sticker_count,'個貼圖，傳了幾張', name2_image_count)


def write_file(filename, lines):
    with open(filename, 'w',encoding= 'utf-8') as f:
        for line in lines:
            f.write(line+ '\n')
    
    
def main():
    lines = read_file('line.txt')
    lines = convert(lines)
    #write_file('output_line.txt', lines)
    
main()    


    
