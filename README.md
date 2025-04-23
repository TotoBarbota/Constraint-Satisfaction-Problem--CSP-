# AI Course - Problem Set 3

## Project Structure

This repository contains three Constraint Satisfaction Problem (CSP) implementations:

```
.
├── Problem_1/       # Exam Timetabling Problem
├── Problem_2/       # General CSP Problem
└── Problem_3/       # Activity Scheduling Problem
```

## Setup and Running

1. Clone the repository:

```bash
git clone
cd Problem_Set_3
```

2. Ensure you have Python 3.x installed

3. Each problem requires the following common files:

   - `csp.py` - Core CSP implementation
   - `search.py` - Search algorithms
   - `utils.py` - Utility functions

4. To run any problem:

```bash
cd Problem_X  # where X is 1, 2, or 3
python problemX.py
```

## Problem Descriptions

### Problem 1: Exam Timetabling

- Implements an exam scheduling system
- Constraints include:
  - 3 time slots per day (9:00-12:00, 12:00-15:00, 15:00-18:00)
  - Same semester exams on different days
  - Lab exams after theory exams
  - Two-day gap between difficult exams
  - Same professor exams on different days
- Features:
  - Multiple search algorithms (Min-Conflicts, MAC, FC)
  - Heuristics (MRV, dom/wdeg)
  - Performance comparison between algorithms

### Problem 2: General CSP

- Generic CSP implementation with various search strategies
- Features:
  - AC3 algorithm for constraint propagation
  - Backtracking search with heuristics
  - Performance comparison between different approaches
  - Flexible constraint definition
- Expected output:
  - Solution satisfying all constraints
  - Number of constraint checks
  - Execution time comparison

### Problem 3: Activity Scheduling

- Schedules 5 activities with temporal constraints
- Specific constraints:
  - A1 must start after A3
  - A3 must start before A4 and after A5
  - A2 cannot run at the same time as A1 or A4
  - A4 cannot start at 10:00
- Features:
  - AC3 domain reduction
  - Backtracking search
  - Constraint satisfaction checking
- Expected output:
  - Valid schedule for all activities
  - Number of constraint checks
  - Domain reduction results

## Testing

Each problem can be tested independently by running its respective python file. The programs will:

1. Display the initial problem setup
2. Show the results of AC3 domain reduction
3. Present the final solution
4. Display performance metrics (constraint checks, execution time)

## Dependencies

- Python 3.x
- All required Python files are included in the repository:
  - `csp.py`
  - `search.py`
  - `utils.py`

## Notes

- Each problem builds upon the core CSP implementation
- Results may vary depending on the specific problem instance
- The implementations include error handling for unsolvable instances
