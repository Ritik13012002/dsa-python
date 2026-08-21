nums = [1, 2, 3, 4]
seen = set()
for num in nums:
    if num in seen:
        print("Duplicate found", True)
        break 

    seen.add(num)
else:
    print("No duplicates found", False)