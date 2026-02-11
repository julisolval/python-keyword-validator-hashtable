## Project Overview   
This mini project implements a custom hash table in Python to simulate how programming keywords could be stored, validated, and organized internally using hashing.

Instead of using Python dictionaries (which already handle hashing internally), this project builds a hash table from scratch to demonstrate:
* How hash functions work
* How collisions happen
* How collisions can be solved using **separate chaining**

The dataset is based on Python reserved keywords used as a beginner-friendly glossary.

![WhatsApp Image 2026-02-11 at 3 50 41 PM](https://github.com/user-attachments/assets/88eb05c2-c56b-4c55-9cf1-973c8bc085c9)
---

## How It Works

Each Python keyword is stored as a key-value pair:
* **Key:** Python keyword
* **Value:** Beginner-friendly description

A simple hash function is used:

```
hash_value = len(keyword) % table_size
```

The table size is fixed to **7 buckets**, intentionally small to provoke collisions and visualize how chaining works.

When multiple keywords map to the same index, they are stored inside the same bucket list.

---

## Collision Handling

This project uses **Separate Chaining**:

* Each index of the hash table contains a list.
* If two keywords generate the same hash index, they are appended to that list.
* This allows multiple values to coexist safely without overwriting data.

---

## Algorithm Complexity

Average time complexity of hash table operations:

```
O(1)
```

Worst case (many collisions in the same bucket):

```
O(n)
```

Because a simple hash function based on word length is used, collisions are expected and intentional for learning purposes.

---

## Educational Design Decision

Python dictionaries were intentionally **not used**.

Although Python `dict` already implements highly optimized hashing with open addressing and resizing, this project recreates a simplified version to:

* Visualize how hash maps work internally
* Understand collision behavior
* Practice implementing data structures manually

---

## Acknowledgment

Python keywords were referenced from:

*Python Crash Course, 2nd Edition.*

Keyword descriptions were written with AI assistance and adapted for educational purposes.
