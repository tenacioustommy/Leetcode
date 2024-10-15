input=[{"asd":"12","sd":{"asd":"42"}},["1",5]]
def str_int(input):
    if isinstance(input,list):
        for i in range(len(input)):
            if isinstance(input[i],str):
                input[i]=int(input[i])
            else:
                str_int(input[i])
    elif isinstance(input,dict):
        for i in input.keys():
            if isinstance(input[i],str):
                input[i]=int(input[i])
            else:
                str_int(input[i])
print(input)    
str_int(input)
print(input)