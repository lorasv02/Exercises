words = ["abc", "def", "ghi", "cba", "bac", "fed"]

seen = set()
result = []

for word in words:
    key = "".join(sorted(word))
    if key not in seen:
        seen.add(key)
        result.append(word)

print(result)

