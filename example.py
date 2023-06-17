

import main


input_str='  {"name": "name1"  , "last_name" :  "last_name1" } '
input_str2='  {"name": "name1"  , "last_name" :  "last_name1","age":12,"m":12.3} '
input_str3='  {"name": "name1"  , "last_name" :  "last_name1","age":null,"person":{"name":"name2","last_name":"last_name4","True":true}} '
input_str4='  {"name": "name1"  , "last_name" :  "last_name1","age":"null2","second":"first","asds":"asdsdsa","number":12,"float_number":34.12} '

input_str5='{"name1":{"first":"first","second":"second"}}'
input_str7='["name1","name2","name3",true,false,null,{"first":"first","second":"second" }]'
#input_str7='["name1","name2","name3",{"first":"first","second":"second"}]'
input_str8='["name1",3.2,"name2","name3",9,["name4","name5",["name8",true]],"name6",["name7"]]'
input_str10='{"name1":3.2,"name2":"name3","n":9,"asd":["name4","name5",["name8",true]],"name6":["name7"]}'



"""
output=main._get_value(input_str)
output2=main._get_value(input_str2)
output3=main._get_value(input_str3)
output4=main._get_value(input_str4)
output5=main._get_value(input_str5)
output6=main._get_value(input_str5[10:len(input_str5)-1:])
#output7=main._get_value(input_str7)
"""
output7=main._get_list(input_str7)
output8=main._get_list(input_str8)
output9=main._get_value(input_str8)
output10=main._get_value(input_str10)


"""
print(output)
print(output2)

print(output2["age"])
print(' ')

print(output3)
print(' ')
print(output4)
print(' ')
print(output5)
print(' ')
#print(output6)
"""
print(' ')
print(output7)
print(' ')
print(output8)
print(' ')
print(output10)

"""
class Name:

    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
n = Name("name1","last_name1")
print(main.saves(n))
"""
