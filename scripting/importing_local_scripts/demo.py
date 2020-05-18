import other_script
import useful_functions as uf

print(5 * 5)
try:
    print(greeting)
except Exception as e:
    print(e)
finally:
    print("The above is to demonstrate you cannot access an object from another script directly using just it's identifier")

print(other_script.greeting)

scores = [90, 82, 74, 56, 50, 40, 22]

average = uf.mean(scores)
standardized = uf.add_five(scores)
mean_s = uf.mean(standardized)

print("Scores:", scores)
print("Standardized scores:", standardized)
print("Original mean:", average, " standardized mean:", mean_s)

print(__name__)
print(uf.__name__)