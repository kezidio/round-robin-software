# 🔁 Round Robin Schedule Generator

This project generates a round-robin schedule from a list of participants. Each participant is paired with every other participant exactly once.

If the number of participants is odd, the program automatically adds a `"bye"` so the schedule can be completed.

---

## 🚀 How It Works

1. The user provides a list of participants
2. If the list length is odd, `"bye"` is added
3. The program generates all possible pairings using a round-robin algorithm

---

## ✨ Features

* Supports any number of participants
* Automatically handles odd-length lists
* Ensures every participant plays every other participant once
* Simple and easy to use

---

## 📥 Input Example

```id="input1"
["Jorge", "Ana", "Ed", "Sam", "Alfie"]
```

---

## 📤 Sample Output

```python id="output1"
[
 ('Jorge', 'bye'),
 ('Ana', 'Ed'),
 ('Sam', 'Alfie'),
 ('Jorge', 'Ed'),
 ('bye', 'Alfie'),
 ('Ana', 'Sam'),
 ('Jorge', 'Alfie'),
 ('Ed', 'Sam'),
 ('bye', 'Ana'),
 ('Jorge', 'Sam'),
 ('Alfie', 'Ana'),
 ('Ed', 'bye'),
 ('Jorge', 'Ana'),
 ('Sam', 'bye'),
 ('Alfie', 'Ed')
]
```


---

## 🛠️ Technologies

* Python

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👤 Author

Kaweny Ezidio

---
