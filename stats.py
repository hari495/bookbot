def get_book_length(text):
    return len(text.split())

def count_chars(text):
    dict={}
    for letter in text:
        lower=letter.lower()
        if(lower) in dict:
            dict[lower]+=1
        else:
            dict[lower]=1
    return dict


def sort_dicts(dict):
    dict_list=[]
    
    for key in dict:
        new_dict={"char":key,"num":dict[key]}
        dict_list.append(new_dict)
    
    dict_list.sort(reverse=True,key=sort_on)
    return dict_list

def sort_on(items):
    return items["num"]