
def isAllCapital(token):
    return token.isupper()

def isFirstCapital(token):
    return token[0].isupper()

def tokenVal(token):
    return hash(token)

def tokenLen(token):
    return(len(token))

def onlyNum(token):
    return token.isdigit()

#FEATURE VECTORS
val_token_list = []       #what is the value of the token
all_cap_list = []         #is the token made up of all capital letters
first_cap_list = []       #does the token start with a capital
token_len_list = []       #what is the length of token
only_num_list = []        #does the token only have numbers
cl_label = []             #tagging as /B, /I, or /O
#NEED 3 MORE FEATURE VECTORS!!!


with open ('NLU.train') as f:
    text = f.read()
    splitlines = text.split('>')
iter_dict = {}
#LOOP FOR FEATURE VECTORS PER TOKEN
for i in range (len(splitlines)):
    split_str = splitlines[i].split('\n')
    for iter in range(len(split_str)):
        if split_str[iter] == '':
            continue
        else:

            if iter in iter_dict:
                iter_dict[iter] += 1
            else:
                iter_dict[iter] = 1
            str_line = split_str[iter]
            token_lst = str_line.split()

#            for word in token_lst:
#                all_cap_list.append(isAllCapital(word))
 #               first_cap_list.append(isFirstCapital(word))
  #              val_token_list.append(tokenVal(word))
   #             token_len_list.append(tokenLen(word))
    #            only_num_list.append(onlyNum(word))
            #val_token_list.append()
            break
#LOOP TO ASSIGN THE FEATURE VECTORS TO THE CORRESPONDING TOKENS

lst_all_tokens = []

for iter in range (len(splitlines)):
    name_str = ''
    id_num = ''
    main_token = ''
    print(splitlines[iter])
    sentence = splitlines[iter].split('\n')
    for sen_iter in range(len(sentence)):
        if '<' in sentence[sen_iter]:
            main_token = (sentence[sen_iter -1])
        elif 'id=' in sentence[sen_iter]:
            id_num = (sentence[sen_iter].split('id=', 1)[1])
        elif 'name=' in sentence[sen_iter]: 
            
            name_str = (sentence[sen_iter].split('name=', 1)[1])
        else:
            continue
    print(id_num)
    print(name_str)
    print(main_token)
    tok_split = main_token.split()
    for c in range(len(tok_split)):
        if len(tok_split[c]) > 1:
            if tok_split[c] in id_num:
                tok_split[c] += '/B'
                lst_all_tokens.append(tok_split[c])
            elif tok_split[c] in name_str and c < len(tok_split) and tok_split[c+1] in name_str:
                tok_split[c] += '/B'
                tok_split[c+1] += '/I'
                lst_all_tokens.append(tok_split[c])
            elif tok_split[c] in name_str and c > 0 and 'I' in tok_split[c -1]:
                tok_split[c] += '/I'
                lst_all_tokens.append(tok_split[c])
            elif tok_split[c] in name_str:
                tok_split[c] += '/B'
                lst_all_tokens.append(tok_split[c])
            elif '/I' in tok_split[c] or '/B' in tok_split[c]:
                continue
            else:
                tok_split[c] += '/O'
                lst_all_tokens.append(tok_split[c])
        else:
            tok_split[c] += '/O'
            lst_all_tokens.append(tok_split[c])
            
    print(tok_split)
for tok in lst_all_tokens:
    spl_tok = tok.split('/')
    all_cap_list.append(isAllCapital(spl_tok[0]))
    first_cap_list.append(isFirstCapital(spl_tok[0]))
    val_token_list.append(tokenVal(spl_tok[0]))
    token_len_list.append(tokenLen(spl_tok[0]))
    only_num_list.append(onlyNum(spl_tok[0]))
    cl_label.append(spl_tok[1])

feature_vect = [[] for x in range(len(all_cap_list))]
for x in range(len(all_cap_list)):
    f_in_vect = []
    f_in_vect.append(all_cap_list[x])
    f_in_vect.append(first_cap_list[x])
    f_in_vect.append(val_token_list[x])     
    f_in_vect.append(token_len_list[x])
    f_in_vect.append(only_num_list[x])
    feature_vect[x] = f_in_vect
print(feature_vect)
print(cl_label)
    


            


