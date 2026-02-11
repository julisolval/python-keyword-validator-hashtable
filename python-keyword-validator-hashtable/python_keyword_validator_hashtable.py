python_keywords = (
    ('False', 'Boolean value that represents false'),
    ('None', 'Represents the absence of a value'),
    ('True', 'Boolean value that represents true'),
    ('and', 'Logical operator used to combine conditions'),
    ('as', 'Used to give an alias to a module or import'),
    ('assert', 'Used for debugging to test if a condition is true'),
    ('async', 'Used to define asynchronous functions'),
    ('await', 'Used to wait for an asynchronous operation'),
    ('break', 'Stops a loop immediately'),
    ('class', 'Used to define a class'),
    ('continue', 'Skips the current loop iteration'),
    ('def', 'Used to define a function'),
    ('del', 'Deletes a variable or object'),

    ('elif', "Used in conditional statements, means 'else if'"),
    ('finally', 'Runs code no matter what after try-except'),
)

hash_table = [[],[],[],[],[],[],[]]

for keyword, description in python_keywords:
    hash_value = len(keyword) % len(hash_table)
    hash_table[hash_value].append((keyword, description))

print("Hash Table:")
for index, bucket in enumerate(hash_table):
    print(f"Bucket {index}:")
    for keyword, description in bucket:
        print(f"  {keyword}: {description}")

