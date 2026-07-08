# 📝 DecodeLabs Week # 01 Project: To-Do List Application

A structured, console-based Task Management Utility built using Python. This project demonstrates in-memory data storage, auto-incrementing record identifiers, and structured data transformation resembling a relational database workflow.

---

## 🚀 Key Features

* **Dynamic In-Memory Storage:** Uses optimized arrays and dictionary schemas to manage task states dynamically during runtime.
* **Auto-Incrementing Identity Engine:** Mimics a primary key system (`IDENTITY(1,1)`) to ensure every inserted task receives a guaranteed unique ID automatically.
* **Structured Data Transformations:** Converts raw user string inputs into clean, structured object rows before saving them to the system.
* **Empty-State Validation:** Built-in checks to intercept data retrieval requests and display graceful alerts when no records exist.
* **De-coupled Control Menu:** A clean, infinite-loop execution block that keeps the system running smoothly until the user explicitly requests a shutdown.

---

## 🏗️ Technical Architecture & Data Mapping

The application processes data using a relational layout model:

### 📊 Task Row Schema
Every task is treated as a record with the following structure:
* `id` (Integer) -> Unique identifier (Auto-incremented)
* `task` (String) -> The actual string payload describing the objective

## [User Menu Selection]
│
├───> Option 1: [Input] ──> [Map to Dictionary Row] ──> [Append to Array]
├───> Option 2: [Validate State] ──> [Loop Through Rows] ──> [Formatted Output]
└───> Option 3: [Break Loop] ──> [Graceful Shutdown]

## 🛠️ Tech Stack & Prerequisites

* **Environment:** Python 3.8 or higher
* **Dependencies:** None (Uses pure Python native standard libraries)

---

## 🔮 Upcoming Updates & Roadmap
We are planning to transition this lightweight utility into a production-grade full-stack application. Future releases will include:

* Persistent Database Integration: Replacing in-memory arrays with an active relational database (like SQL Server via EF Core / Python equivalents) to save tasks permanently.
* Full CRUD Implementations: Adding specific backend modules to support updating existing tasks (UPDATE) and removing completed tasks (DELETE) by target ID.
* API Layer Evolution: Wrapping this core logical engine into a modern RESTful API backend structure to allow front-end communication.
