import other_script
print(5*5)
try:
    print(greeting)
except Exception as e:
    print(e)
finally:
    print("The above is to demonstrate you cannot access an object from another script directly using just it's identifier")

print(other_script.greeting)