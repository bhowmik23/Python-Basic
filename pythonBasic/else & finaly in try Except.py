f1 = open("harry-ex.txt")

try:
    # f = open("dose.txt")
    f = open("harry-ex.txt")

except Exception as e:
    print(e)

except IOError as e:
    print(e)

except EOFError as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anywhy")
    f1.close()

print("important staff")