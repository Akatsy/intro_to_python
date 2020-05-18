import other_script
import useful_functions

print(5 * 5)
try:
    print(greeting)
except Exception as e:
    print(e)
finally:
    print("The above is to demonstrate you cannot access an object from another script directly using just it's identifier")

print(other_script.greeting)

scores = [90, 82, 74, 56, 50, 40, 22]

average = useful_functions.mean(scores)
standardized = useful_functions.add_five(scores)
mean_s = useful_functions.mean(standardized)

print("Scores:", scores)
print("Standardized scores:", standardized)
print("Original mean:", average, " standardized mean:", mean_s)