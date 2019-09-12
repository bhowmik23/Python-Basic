def function_Name_Print(a, b, c, d, e):
    print(a, b, c, d, e)
def funargs(mr, *args, **kwagrs):
    print(me)
    for item in args:
        print(item)
#      print(args[0])
    for key, value in kwagrs.items():
        print(f"{key} is a {value}")
function_Name_Print("Biddut", "Bappi", "Badhon", "Momi", "Toha")
list1 = ["Biddut", "Bappi", "Badhon", "Momi", "Toha"]
me = "my name is Biduut Bhowmik"
kw = {"Biddut":"Captain", "Bappi":"Programmer"}
funargs(me, *list1, **kw)