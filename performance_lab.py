# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

# Optimization:
# The original solution used one loop to count the numbers and a second loop
# to find the most frequent value. This version tracks the most frequent value
# while building the dictionary, so it only needs one pass through the input.
# Both versions are O(n), but this version performs less work in practice.

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = None
    highest_count = 0

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

        if counts[number] > highest_count:
            highest_count = counts[number]
            most_common = number

    return most_common


# Test cases for Problem 1
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Expected: 3
print(most_frequent([5, 5, 2, 2, 5]))        # Expected: 5
print(most_frequent([7]))                     # Expected: 7
print(most_frequent([]))                      # Expected: None

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
  The function must examine every number in the list to know which value
  appears most frequently.

- Worst-case: O(n)
  The function processes each of the n elements once. Dictionary lookups
  and updates are O(1) on average, so the total work grows linearly.

- Average-case: O(n)
  Dictionary lookups and updates are O(1) on average, so processing all n
  numbers takes linear time.

- Space complexity: O(n)
  The counts dictionary may need to store every number if all values in the
  input are unique.

- Why this approach?
  A dictionary lets me count how many times each number appears using fast
  lookups. This avoids repeatedly scanning the list to count each number.

- Could it be optimized?
  Yes. The original version used a second loop to find the most frequent
  value after counting all numbers. I optimized it by tracking the most
  frequent value during the counting loop. Both versions are O(n), but the
  optimized version performs fewer passes through the data.

- Trade-offs:
  The optimized version still uses O(n) extra space for the dictionary.
  It improves practical runtime by removing the second loop without
  increasing the space complexity.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


# Test cases for Problem 2
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Expected: [4, 5, 6, 7]
print(remove_duplicates([1, 1, 1, 1]))        # Expected: [1]
print(remove_duplicates([1, 2, 3]))           # Expected: [1, 2, 3]
print(remove_duplicates([]))                  # Expected: []

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
  The function still checks every element in the input list, even if there
  are no duplicates or the list is already unique.

- Worst-case: O(n)
  The loop processes all n elements. Set membership checks and additions are
  amortized O(1), so the total work grows linearly with the input size.

- Average-case: O(n)
  Each number is visited once, and checking whether a value is in the set is
  O(1) on average.

- Space complexity: O(n)
  In the worst case, all values are unique, so the seen set and result list
  can both grow with the size of the input.

- Why this approach?
  I used a set to quickly check whether a value has already been seen and a
  list to preserve the original order of the values.

- Could it be optimized?
  The time complexity is already O(n), which is efficient because every input
  value must be examined at least once.

- Trade-offs:
  This approach uses O(n) extra memory for the set and result list, but that
  extra memory allows duplicate checks to be fast. Using only a list could
  reduce the number of data structures but may increase runtime to O(n^2).
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        needed = target - num

        if needed in seen:
            pairs.append((needed, num))

        seen.add(num)

    return pairs


# Test cases for Problem 3
print(find_pairs([1, 2, 3, 4], 5))      # Expected: [(2, 3), (1, 4)]
print(find_pairs([2, 4, 6, 8], 10))     # Expected: [(4, 6), (2, 8)]
print(find_pairs([1, 2, 3], 10))        # Expected: []
print(find_pairs([], 5))                # Expected: []

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
  The function still checks every number in the list because it needs to find
  all pairs that add up to the target.

- Worst-case: O(n)
  Each number is processed once. Set membership checks and additions are
  amortized O(1), so the total runtime grows linearly with the input size.

- Average-case: O(n)
  The loop visits each element once, and checking for the needed value in the
  set is O(1) on average.

- Space complexity: O(n)
  The seen set can store up to n values, and the pairs list can also grow
  depending on how many matching pairs are found.

- Why this approach?
  I used a set so I can quickly check whether the number needed to reach the
  target has already been seen. This avoids using nested loops.

- Could it be optimized?
  This is already efficient for an unsorted list because it avoids the O(n^2)
  runtime of checking every possible pair.

- Trade-offs:
  This approach uses O(n) extra memory for the set in order to reduce runtime
  from O(n^2) to O(n). It trades extra space for faster performance.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    items = [None] * capacity

    for i in range(n):
        if size == capacity:
            old_capacity = capacity
            capacity *= 2

            print(f"Resizing from capacity {old_capacity} to {capacity}")

            new_items = [None] * capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items

        items[size] = i
        size += 1

    return items[:size]


# Test cases for Problem 4
print(add_n_items(6))   # Expected values: [0, 1, 2, 3, 4, 5]
print(add_n_items(1))   # Expected values: [0]
print(add_n_items(0))   # Expected values: []

"""
Time and Space Analysis for problem 4:
- Best-case: O(n)
  Adding n items requires processing all n items, even when few resizes occur.

- Worst-case: O(n)
  Across all n additions, resizing requires copying elements occasionally,
  but the total work across the complete sequence still grows linearly.

- Average-case: O(n)
  Performing n appends takes O(n) total time because each append has
  amortized O(1) cost.

- When do resizes happen?
  Resizing happens whenever the current number of stored items reaches the
  current capacity. The capacity doubles each time, such as 1, 2, 4, 8, 16.

- What is the worst-case for a single append?
  O(n). When the list is full, a new larger list must be created and all
  existing values must be copied into it before the new value can be added.

- What is the amortized time per append overall?
  O(1). Most appends do not require resizing, so although an occasional
  append costs O(n), the average cost per append over many operations is
  constant time.

- Space complexity:
  O(n). The list capacity grows with the number of elements being stored.
  During a resize, both the old and new lists temporarily exist in memory,
  but the total space still grows linearly with n.

- Why does doubling reduce the cost overall?
  Doubling creates enough extra capacity that another resize is not needed
  after every append. As the list grows, resizes become less frequent, which
  spreads the expensive copying operations across many inexpensive appends.

- Trade-offs:
  Doubling uses some extra unused memory between resizes, but it makes repeated
  appends much faster overall by reducing how often values must be copied.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result


# Test cases for Problem 5
print(running_total([1, 2, 3, 4]))   # Expected: [1, 3, 6, 10]
print(running_total([5, 5, 5]))      # Expected: [5, 10, 15]
print(running_total([10]))           # Expected: [10]
print(running_total([]))             # Expected: []

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
  The function must process every number in the input list to calculate all
  of the running totals.

- Worst-case: O(n)
  The loop visits each of the n elements exactly once, so the amount of work
  grows linearly with the size of the input.

- Average-case: O(n)
  Regardless of the values in the list, each element is processed once.

- Space complexity: O(n)
  The function creates a new result list containing one running total for
  every element in the input list.

- Why this approach?
  I keep a running sum instead of recalculating the sum from the beginning
  for every position. This allows the function to complete in one pass.

- Could it be optimized?
  The time complexity is already O(n), which is optimal because every value
  must be processed. Space could only be reduced by modifying the original
  list in place, but the problem specifically asks for a new list.

- Trade-offs:
  Creating a new list requires O(n) extra memory, but it preserves the
  original input list and keeps the solution simple and efficient.
"""
