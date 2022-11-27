
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
#NEED 3 MORE FEATURE VECTORS!!!


with open ('NLU.train') as f:
    text = f.read()
    splitlines = text.split('>')
iter_dict = {}
for i in range (0, 50):

    #print(splitlines[i])
    split_str = splitlines[i].split('\n')
    for iter in range(len(split_str)):
        if split_str[iter] == '':
            continue
        else:
            #print({iter}, ' ', split_str[iter])
            if iter in iter_dict:
                iter_dict[iter] += 1
            else:
                iter_dict[iter] = 1
            str_line = split_str[iter]
            token_lst = str_line.split()
            #print(token_lst)
            for word in token_lst:
                all_cap_list.append(isAllCapital(word))
                first_cap_list.append(isFirstCapital(word))
                val_token_list.append(tokenVal(word))
                token_len_list.append(tokenLen(word))
                only_num_list.append(onlyNum(word))
            #val_token_list.append()
            break
ref_line_str = ''
id_word = ''
name_word = ''
for i in range (0, 15):
    split_str = splitlines[i].split('\n')
    for iter in range(len(split_str)):
        if split_str[iter] == '':
            continue
        elif '<'  not in split_str[iter] and '=' not in split_str[iter]:
            ref_line_str = split_str[iter]
            continue
            #print(ref_line_str)
        elif 'id=' in split_str[iter]:
            curr_line = split_str[iter]
            id_word = (curr_line.split('id=', 1)[1])

        elif 'name=' in split_str[iter]:
            curr_line = split_str[iter]
            name_word = (curr_line.split('name=', 1)[1])
        else:
            continue
main_line_lst = ref_line_str.split(' ')
for token_word in range(len(main_line_lst)):
    if id_word == main_line_lst[token_word]:
        main_line_lst[token_word] += '/B'
    else:
        for name_token in range(len(main_line_lst)):
            if main_line_lst[name_token] == main_line_lst[token_word] and name_token == 0:
                main_line_lst[token_word] += '/B'
            elif name_word[name_token] == main_line_lst[token_word] and name_token != 0:
                main_line_lst[token_word] += '/I'
            else:
                continue

print(ref_line_str)
print(id_word)
print(name_word)
print(main_line_lst)
            

feature_vect = [[] for x in range(len(all_cap_list))]
for x in range(len(all_cap_list)):
    f_in_vect = []
    f_in_vect.append(all_cap_list[x])
    f_in_vect.append(first_cap_list[x])
    f_in_vect.append(val_token_list[x])     
    f_in_vect.append(token_len_list[x])
    f_in_vect.append(only_num_list[x])
    feature_vect[x] = f_in_vect
#test_word = "h1234"
#print(all_cap_list)
#print(first_cap_list)
#print(val_token_list)
#print(token_len_list)
#print(only_num_list)

#print(len(all_cap_list))
#print(len(val_token_list))
#print(len(token_len_list))
#print(len(only_num_list))

#print(feature_vect)
#print(iter_dict)
