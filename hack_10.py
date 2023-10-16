"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    #...
    new=[('oo','00'),('i','1'),('a','@')]

    for i in range(len(new)):
        str_sear, str_rep= new[i]
        if result.find(str_sear):            
            result= result.replace(str_sear, str_rep) 


    return list(result.upper())   