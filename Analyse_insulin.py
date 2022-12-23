import re 

txt_file = 'preproinsulin-seq.txt'
with open(txt_file) as f:
    lines = f.read()
    pattern = r'\s+|[0-9]|ORIGIN|//' 
    
    cleaned_data = re.sub(pattern,'',lines)
    cleaned_data_24 = cleaned_data[0:24] 
    cleaned_data_54 = cleaned_data[24:54]
    cleaned_data_89 = cleaned_data[54:89]
    cleaned_data_110 = cleaned_data[89:110]
       
    with open('lsinsulin-seq-clean.txt','w') as f:
        f.write(cleaned_data_24)
    
    with open('binsulin-seq-clean.txt','w') as f:
        f.write(cleaned_data_54)
        
    with open('cinsulin-seq-clean.txt','w') as f:
        f.write(cleaned_data_89)    

    with open('ainsulin-seq-clean.txt','w') as f:
        f.write(cleaned_data_110)


print(f'After Cleaning the Amino Acid count is {len(cleaned_data)}')
print(f'Amino acid count from 1 to 24: {len(cleaned_data_24)}')
print(f'Amino acid count from 24 to 54: {len(cleaned_data_54)}')
print(f'Amino acid count from 54 to 89: {len(cleaned_data_89)}')
print(f'Amino acid count from 89 to 110: {len(cleaned_data_110)}')