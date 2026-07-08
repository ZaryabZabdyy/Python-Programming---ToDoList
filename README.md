# 📝 CoreEngine-ToDo: In-Memory Data Management Logic

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Software Engineering Practice](https://img.shields.io/badge/Workflow-Requirements--Driven-orange.svg)]()

An industrial-grade console-based data management engine built using pure programmatic logic in Python. This project serves as a clean engineering foundation for handling in-memory data structures, simulating real-world database behaviors before moving to persistent storage layers.

---

## 🎯 Project Overview & Objective

This project focuses strictly on core **Data Management** and backend logic. The objective is to move past primitive scalar variables and establish structural logic capable of storing, processing, and rendering multiple data entities within volatile system memory. 

It implements the classic **IPO (Input-Process-Output) Architectural Model**:
1. **Input (Storage):** Holding data structurally in dynamic arrays.
2. **Process (Logic):** Mutating and modifying the state of the data securely.
3. **Output (Display):** Providing structural views of the system state.

---

## 🛠️ Tech Stack & Systems Architecture

* **Language:** Python 3.x
* **Paradigm:** Core Programmatic Logic (No heavy third-party frameworks)
* **Memory Management:** Dynamic Array Allocations (Python List & Heap Management)

### 🧠 Under The Hood: Memory Lifecycle
* **The Reference Pointer (Stack):** The variable acts as a reference address pointer.
* **The Dynamic Object (Heap):** Tasks are appended to runtime dynamic memory structures. 
* **Algorithmic Efficiency:** Utilizes Amortized $O(1)$ time complexity for appends due to Python's pre-allocated memory optimization on the system Heap.

---

## 🚀 Key Features

* **In-Memory Volatile Storage:** Uses a dynamic array block to safely track active task strings during execution.
* **The Append Pipeline:** Secure user entry validation that cleanly passes raw input directly into the main state variable.
* **System View Generator:** Implements an Iterator Protocol loop that parses the active list to generate a structured console output.
* **Clean Terminal Menu Interface:** An interactive loop structure providing absolute clarity during add and view operations.

---

## 📋 Requirements Mapping

This system strictly fulfills the following functional benchmarks:
* **Requirement 1:** Provide an explicit option for users to cleanly inject new tasks (e.g., `"Finish Python assignment"`) into the tracking array.
* **Requirement 2:** Render a structured, real-time read-out of all tracked array values upon execution commands.
* **Requirement 3:** Maintain a persistent runtime loop allowing multiple operations until explicitly terminated.

---

## ⚙️ Installation & Local Setup

Follow these commands to spin up this engine on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
