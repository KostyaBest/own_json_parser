






"""
    Read the JSON document and return object or exception
"""
def load(path:str)->object:
    try:
        with open(path,"r") as f:
            file_data=f.readlines()
        string=""
        for line in file_data:
            string+=line
        return _get_value(string)
    except Exception as e:
       raise e.message() 


"""
    Read the JSON string and return object or exception
"""
def loads(string:str)->object:
    try:
        return _get_value(string)
    except Exception as e:
        raise e.message


def _get_value(string:str)->object:
    output={}
    QUOTATION_MARK_COUNT=0
    BRACKETS_COUNT=0
    BRACES_COUNT=0
    COLON_COUNT=0
    #BRACES_INDEXES=[]
    LIST_BUFFER=''
    PREV_BRACKETS_INDEX=0
    PREV_BRACES_INDEX=0
    HAS_BEEN_STARTED=False
    

    VALUE_TYPE="str"
    KEY=""
    IS_KEY=True
    VALUE=""

    for i in range(len(string)):
        if QUOTATION_MARK_COUNT %2 ==0:
            if VALUE_TYPE == "list":
                if string[i] == "]":
                    list_value = _get_list(string[PREV_BRACKETS_INDEX:i+1:])
                    VALUE_TYPE="str"
                    output[KEY]=list_value
                    KEY=""
                    VALUE=""
                    continue
                #if PREV_BRACKETS_INDEX !=0:
                    #if string[i] == "]" and BRACKETS_COUNT == 2:
                        #output[KEY]=_get_value(string[PREV_BRACKETS_INDEX:i+1:])
                        #VALUE_TYPE="str"
                        #continue
                continue

            if PREV_BRACES_INDEX !=0:
                if string[i] == "}" and BRACES_COUNT == 2:
                    output[KEY]=_get_value(string[PREV_BRACES_INDEX:i+1:])
                    continue
                continue
            if string[i] == " ":
                continue
            if string[i] == "[":
                PREV_BRACKETS_INDEX=0
                VALUE_TYPE = "list"
                BRACKETS_COUNT +=1
                continue
            if string[i] == ":":
                COLON_COUNT+=1
                IS_KEY=False
                continue
            if string[i] == '"':
                QUOTATION_MARK_COUNT+=1
                continue
            if string[i] == "{" and BRACES_COUNT==1:
                PREV_BRACES_INDEX=i
                BRACES_COUNT+=1
                continue
            if string[i] == "{":
                BRACES_COUNT+=1
                continue
            if string[i]=='}':
                    if PREV_BRACES_INDEX != 0:
                        VALUE=_get_value(string[PREV_BRACES_INDEX:i:])
                        output[KEY]=VALUE
                        VALUE=""
                        KEY=""
                        IS_KEY=True
                        PREV_BRACES_INDEX=0
                        continue
            if string[i] == ',' or string[i] == '}':
                COLON_COUNT-=1
                if KEY == "" and VALUE == "":
                    continue
                if VALUE=="null":
                    output[KEY]=None
                    KEY=""
                    VALUE=""
                    IS_KEY=True
                    continue
                if VALUE=="true":
                    output[KEY]=True
                    KEY=""
                    VALUE=""
                    IS_KEY=True
                    continue
                if VALUE=="false":
                    output[KEY]=None
                    KEY=""
                    VALUE=""
                    IS_KEY=True
                    continue
                if VALUE.isdigit() or VALUE.replace(".","").isdigit():
                    is_float=False
                    for i in range(len(VALUE)):
                        if VALUE[i]==".":
                            if is_float:
                                raise Exception("Error there must be only 1 . in number")
                            is_float=True
                    if is_float:
                        value=float(VALUE)
                        output[KEY]=value
                        KEY=""
                        VALUE=""
                        IS_KEY=True
                        QUOTATION_MARK_COUNT=0
                        COLON_COUNT=0
                        continue
                    value=int(VALUE)
                    output[KEY]=value
                    KEY=""
                    VALUE=""
                    IS_KEY=True
                    QUOTATION_MARK_COUNT=0      
                    continue
            if string[i] == '{':
                BRACES_COUNT+=1
                #if BRACES_COUNT==2 or BRACES_COUNT>2:
                if BRACES_COUNT>2 and COLON_COUNT>0:
                    PREV_BRACES_INDEXES=i
                continue
        #if QUOTATION_MARK % 2 == 1:
        if IS_KEY:
            if string[i] == '"':
                QUOTATION_MARK_COUNT -= 1
                IS_KEY = False
                continue
            KEY+=string[i]
            continue

        if not IS_KEY:
            if string[i] == '"':
                output[KEY]=VALUE
                KEY=""
                VALUE=""
                QUOTATION_MARK_COUNT-=1
                IS_KEY=True
                continue
            VALUE+=string[i]
            continue

    return output

def _get_list(string:str)->list:
    output=[]
    QUOTATION_MARK_COUNT=0
    BRACES_COUNT=0
    BRACKETS_COUNT=0
    #BRACES_INDEXES=[]
    PREV_BRACKETS_INDEX=0
    PREV_BRACES_INDEX=0
    VALUE=""
    for i in range(len(string)):
        #if QUOTATION_MARK_COUNT % 2 == 0 and BRACES_COUNT == 0:
        if QUOTATION_MARK_COUNT % 2 == 0:
            if string[i] == ' ':
                continue
            if string[i] == "[":
                BRACKETS_COUNT+=1
                if BRACKETS_COUNT == 2:
                    PREV_BRACKETS_INDEX=i
                    continue
                continue
            if string[i] == "]":
                if BRACKETS_COUNT == 2:
                    BRACKETS_COUNT-=1
                    VALUE=_get_list(string[PREV_BRACKETS_INDEX:i:])
                    value_length=len(VALUE)
                    output=output[0:len(output)-value_length:]
                    output.append(VALUE)
                    VALUE=""
                    continue
                BRACKETS_COUNT-=1
                continue
            if string[i] == '"':
                QUOTATION_MARK_COUNT+=1
                continue

            if string[i] == "{":
                BRACES_COUNT+=1
                if PREV_BRACES_INDEX == 0:
                    PREV_BRACES_INDEX=i
                    print(PREV_BRACES_INDEX)
                    continue
                continue
            if string[i] == '}' and BRACES_COUNT-1==0:
                BRACES_COUNT-=1
                VALUE=_get_value(string[PREV_BRACES_INDEX:i:])
                output.append(VALUE)
                VALUE=""
                continue
            if string[i] == "}":
                BRACES_COUNT-=1
                if PREV_BRACES_INDEX != 0:
                    VALUE=_get_value(string[PREV_BRACES_INDEX:i:])
                    output.append(VALUE)
                    VALUE=""
                    continue
                continue

            if string[i] == ',':
                if VALUE=="":
                    continue
                if VALUE=="true":
                    output.append(True)
                    VALUE=""
                    continue
                if VALUE=="false":
                    output.append(False)
                    VALUE=""
                    continue
                if VALUE=="null":
                    output.append(None)
                    VALUE=""
                    continue
                if VALUE.isdigit() or VALUE.replace(".","").isdigit():
                    is_float=False
                    for i in range(len(VALUE)):
                        if VALUE[i]==".":
                            if is_float:
                                raise Exception("Error there must be only 1 . in number")
                            is_float=True
                    if is_float:
                        value=float(VALUE)
                        output.append(value)
                        VALUE=""
                        continue
                    value=int(VALUE)
                    output.append(value)
                    VALUE=""
                    continue
                continue
        #if QUOTATION_MARK_COUNT % 2 == 1
        if BRACES_COUNT == 0:
            if string[i] == '"':
                QUOTATION_MARK_COUNT-=1
                output.append(VALUE)
                VALUE=""
                continue
            VALUE+=string[i]
            continue
    return output

"""
    Save object in JSON file or return exception
"""
def save(obj:object,path:str)->None:
    with open(path,'a') as f:
        f.writelines(saves(obj))


"""
    Read the object and return JSON string or exception
"""
def saves(obj:object)->str:
    obj=o.__dict__
    out=""
    IS_FIRST=True
    for (key,value) in obj.items():
        if IS_FIRST:
            out+="{"
            IS_FIRST=False
        if type(value) is list:
            for line in len(value):
                out.append(line)
        out+=f"{key}:{value}"
    return obj


if __name__ == "__main__":
    pass


