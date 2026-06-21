words= ["apple","bat","cherry","dog","elderberry"]
filter_words = [w.upper() for w in words if len(w)>=4]
print(f"original: {words}")
print(f"Result: {filter_words}")