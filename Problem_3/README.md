# Problem 3: Activity Scheduling Problem

## Execution

To run the program:

```python
python ./problem3.py
```

The program implements a Constraint Satisfaction Problem (CSP) solver for a specific activity scheduling problem.

## Problem Description

This problem involves scheduling 5 activities (A1 through A5) with specific temporal constraints:

- Each activity must be assigned a start time (9:00, 10:00, or 11:00)
- Specific temporal relationships:
  - A1 must start after A3
  - A3 must start before A4
  - A3 must start after A5
  - A2 cannot run at the same time as A1 or A4
  - A4 cannot start at 10:00

## Implementation Details

The solution implements:

- CSP class from the csp.py module
- AC3 algorithm for constraint propagation
- Custom constraint function for activity scheduling
- Domain reduction based on constraints

### Constraint Implementation

The following constraints are implemented:

- Temporal ordering constraints between activities
- Mutual exclusion constraints for conflicting activities
- Specific time slot restrictions for certain activities
- Domain reduction based on constraints

### Search Heuristics

The program uses:

- AC3 algorithm for domain reduction
- Backtracking search with appropriate heuristics
- Constraint satisfaction checking during assignment

## Results

The program demonstrates that:

- AC3 effectively reduces the domains of variables
- The combination of AC3 with backtracking search finds valid solutions
- The constraints are properly enforced during the search process

## Example Output

The program will output:

```
Domains after AC-3:
A1: [11]
A2: [9, 10]
A3: [10]
A4: [11]
A5: [9]

Number of constraint checks: 90
```

This output shows:

- The final domains for each activity after AC3
- The number of constraint checks performed
- A valid schedule that satisfies all constraints

## Notes

- The program uses the AC3 algorithm to reduce domains before search
- The solution is found using backtracking with appropriate heuristics
- The implementation includes error handling for unsolvable instances
- The output shows both the reduced domains and the number of constraint checks

## Solution Analysis

The solution shows that:

- A1 must start at 11:00 (after A3)
- A2 can start at either 9:00 or 10:00 (not conflicting with A1 or A4)
- A3 is fixed at 10:00 (between A5 and A4)
- A4 is fixed at 11:00 (after A3, not at 10:00)
- A5 is fixed at 9:00 (before A3)

This solution satisfies all the given constraints while minimizing the number of constraint checks.

"problem3.py" makes use of the "csp.py".

Make sure to have cps.py search.py and utils.py in the same folder.
