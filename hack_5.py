"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"

    new=[('oo','00'),('i','1'),('a','@')]

    for i in range(len(new)):
        str_sear, str_rep= new[i]
        if result.find(str_sear):            
            result= result.replace(str_sear, str_rep) 

   
    return result 


