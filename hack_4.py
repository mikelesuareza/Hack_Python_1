"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    result = result.replace(result[-1], result[-1].capitalize())
    #...
    return result