# TCS CodeVita Season 12
This repository contains my solutions for the **TCS CodeVita Season 12 programming competition**, which includes various **MockVita** problems. Below are the descriptions of the problems solved and the technologies used in the solutions.

---

## MockVita Problems

### 1. Best Bubble

**Problem Description:**
This problem revolves around the classic **Bubble Sort** algorithm, where adjacent elements are repeatedly swapped if they are in the wrong order. Sorting an array in ascending order can take longer when the smallest element is positioned at the end, but sorting in descending order can be quicker.

An array is considered "beautiful" if its elements are sorted in either ascending or descending order. The challenge is to determine the **minimum number of swaps** required to make an array beautiful.

- **Input:**
  - First line: Integer `N` (the number of elements in the array).
  - Second line: `N` space-separated integers representing the array.

- **Output:** Print the minimum number of swap operations required to make the array beautiful.

---

### 2. Good String

**Problem Description:**
A school trip to a museum led to students quarreling in line. To settle the dispute, a teacher introduced the concept of a "Good String". 

A **Good String** is a string in which all characters are "good". Each student’s name is to be converted into a "good name" by replacing each character with the nearest good character from the good string, based on ASCII values. If multiple characters are equidistant, choose the one closest to the previously selected character.

Your task is to help calculate the total distance for the student's name after converting it to a "good name".

- **Input:**
  - First line: The "Good String".
  - Second line: The student's name.

- **Output:** Print the total distance for the given name.

---

### 3. Orchard

**Problem Description:**
Two friends, Ashok and Anand, visit an orchard where **lemon (L)** and **mango (M)** trees are planted in rows. They each select a row and argue about which row contains more fruit. Akhil steps in to settle the debate and asks each friend to choose three non-adjacent trees from their respective rows. The goal is to determine who has the most possible valid selections.

- **Input:**
  - First line: A string representing Ashok’s row (consisting of 'M' and 'L').
  - Second line: A string representing Anand’s row (also consisting of 'M' and 'L').

- **Output:** Print the winner's name or "Draw" if neither wins. If the input is invalid, print "Invalid input".

---

### 4. VIP Cafe

**Problem Description:**
Raj runs a popular cafe that caters to VIP customers who order high-priced beverages. To ensure VIPs receive quicker service while still attending to other customers, Raj implements a dynamic priority system for handling orders. Every order is assigned a priority, and orders with higher priorities are served first. Additionally, after an order is served, the priority of the remaining orders is adjusted.

Given the current state of the queue, your task is to determine how many orders will be served before Raj’s friend’s order is processed.

- **Input:**
  - First line: An integer `N` representing the total number of orders.
  - Second line: `N` space-separated integers representing the priority of each order.
  - Third line: An integer `K`, representing the position of Raj’s friend in the queue.

- **Output:** Print the number of orders that will be served before Raj’s friend’s order.

---

### 5. Weapon Boxes

**Problem Description:**
In a military camp, boxes filled with weapons have different weights, indicating the quantity of weapons inside. The commander prioritizes heavier boxes for inspection. During each cycle, he selects the first `N` boxes, compares the first two, and shifts the lighter one to the end of the line. The process continues until one box remains unchanged for `K` consecutive cycles. Additionally, boxes with triangular number weights are excluded from the total labor cost.

Your task is to calculate the cost of labor based on the sum of the weights of the valid boxes after the sorting process.

- **Input:**
  - First line: Array representing the weight of all the boxes.
  - Second line: Two integers, `N` and `K`, indicating the number of boxes selected in each cycle and the stopping condition.

- **Output:** Print the total cost of labor.

---

### 6. Zero Count

**Problem Description:**
You are given a binary string `B` of length `L` containing `K` ones. Your task is to rearrange the ones in such a way that the **longest consecutive zeros** in the string is minimized. Once the optimal arrangement is achieved, print the length of the longest block of consecutive zeros.

- **Input:**
  - A single line containing two integers, `L` and `K`.

- **Output:** Print the length of the longest consecutive zeros after rearrangement.

---

## Technologies Used
- **Python**
- **C++**

These solutions tackle various algorithmic and data structure challenges using Python and C++, ensuring both efficiency and clarity in solving problems under competitive programming conditions.
