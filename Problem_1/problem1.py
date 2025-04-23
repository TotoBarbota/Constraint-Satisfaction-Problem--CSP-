from csp import CSP, forward_checking
import csv
from datetime import datetime, timedelta
from collections import defaultdict

class ExamTimetabling(CSP):
    def __init__(self, subjects_file, num_days):
        self.DAYS = num_days
        self.SLOTS_PER_DAY = 3
        self.TIME_SLOTS = [(i, j) for i in range(self.DAYS) for j in range(self.SLOTS_PER_DAY)]
        
        self.subjects = self.read_subjects(subjects_file)
        
        variables = []
        for subject in self.subjects:
            variables.append(f"{subject['name']}_theory")
        
        domains = {}
        for var in variables:
            subject = self.get_subject_info(var)
            if subject['has_lab']:
                domains[var] = [(i, j) for i in range(self.DAYS) for j in range(self.SLOTS_PER_DAY - 1)]
            else:
                domains[var] = self.TIME_SLOTS
        
        neighbors = {}
        for var in variables:
            neighbors[var] = [other for other in variables if other != var]
        
        super().__init__(variables, domains, neighbors, self.constraints)
        
    def read_subjects(self, filename):
        subjects = []
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                subject = {
                    'semester': int(row[0]),  # Εξάμηνο
                    'name': row[1].strip(),  # Μάθημα
                    'professor': row[2].strip(),  # Καθηγητής
                    'is_difficult': row[3].strip().upper() == 'TRUE',  # Δύσκολο (TRUE/FALSE)
                    'has_lab': row[4].strip().upper() == 'TRUE'  # Εργαστήριο (TRUE/FALSE)
                }
                subjects.append(subject)
        # for subject in subjects:
        #     print(f"Semester: {subject['semester']}, Name: {subject['name']}, Professor: {subject['professor']}, Difficult: {subject['is_difficult']}, Has Lab: {subject['has_lab']}")
        
        return subjects
    
    def get_subject_info(self, exam_code):
        """Get subject information from exam code (removing _theory or _lab suffix)"""
        name = exam_code.rsplit('_', 1)[0]  # Split from right side once
        return next(s for s in self.subjects if s['name'] == name)
    
    def constraints(self, A, a, B, b):
        """Check if assignments of A->a and B->b satisfy all constraints"""
        if A == B:
            return True
        
        # Get subject information
        subject_A = self.get_subject_info(A)
        subject_B = self.get_subject_info(B)
        
        # Get day and slot for both exams
        day_A, slot_A = a
        day_B, slot_B = b

        # Same day and time constraint
        if day_A == day_B:
            # Check for overlapping time slots
            if slot_A == slot_B:
                return False
            # Calculate the slots each exam takes depending on if it has a lab or not
            slots_A = 2 if subject_A['has_lab'] else 1
            slots_B = 2 if subject_B['has_lab'] else 1
            
            # Calculate the range of slots each exam occupies
            range_A = range(slot_A, slot_A + slots_A)
            range_B = range(slot_B, slot_B + slots_B)
            
            # Check if the ranges overlap
            for slot in range_A:
                if slot in range_B:
                    return False
            
            # Check for same professor constraint
            if subject_A['professor'] == subject_B['professor']:
                return False
            # Check for same semester constraint
            if subject_A['semester'] == subject_B['semester']:
                return False
        
        # Difficult exam constraint
        if subject_A['is_difficult'] and subject_B['is_difficult']:
            if abs(day_A - day_B) < 2:
                return False

        
                
        return True

def solve_timetable(csv_file, num_days, all_exams=False):
    problem = ExamTimetabling(csv_file, num_days)
    
    from csp import (backtracking_search, mrv, mac, forward_checking, 
                    min_conflicts, first_unassigned_variable, dom_wdeg)
    import time

    results = {}
    
    combinations = [
        ("MAC with MRV", mrv, mac),
        ("MAC with dom/wdeg", dom_wdeg, mac),
        ("FC with MRV", mrv, forward_checking),
        ("FC with dom/wdeg", dom_wdeg, forward_checking),

    ]
    
    # Test min-conflicts algorithm
    print("\nTesting: Min-Conflicts")
    start_time = time.time()
    min_conflicts_solution = min_conflicts(problem)
    end_time = time.time()
    duration = end_time - start_time
    
    results["Min-Conflicts"] = {
        'time': duration,
        'assignments': problem.nassigns,
        'solution': min_conflicts_solution
    }
    
    print(f"Time taken: {duration:.2f} seconds")
    print(f"Solution found: {'Yes' if min_conflicts_solution else 'No'}")
    if(all_exams):
        for name, var_selector, inference in combinations:
            print(f"\nTesting: {name}")
            start_time = time.time()
            problem.nassigns = 0
            
            solution = backtracking_search(problem, 
                                        select_unassigned_variable=var_selector,
                                        inference=inference)
            
            end_time = time.time()
            duration = end_time - start_time
            
            results[name] = {
                'time': duration,
                'assignments': problem.nassigns,
                'solution': solution
            }
            
            print(f"Time taken: {duration:.2f} seconds")
            print(f"Number of assignments: {problem.nassigns}")
            print(f"Solution found: {'Yes' if solution else 'No'}")
    
    
    # Print comparison table
    print("\nComparison Table:")
    print("-" * 80)
    print(f"{'Method':<25} {'Time (s)':<15} {'Assignments':<15} {'Solution Found':<15}")
    print("-" * 80)
    for method, data in results.items():
        print(f"{method:<25} {data['time']:<15.2f} {data['assignments']:<15} {'Yes' if data['solution'] else 'No':<15}")
    print("-" * 80)
    
    # Return the solution from the best performing method (by time)
    best_method = min(results.items(), key=lambda x: x[1]['time'] if x[1]['solution'] else float('inf'))
    best_solution = best_method[1]['solution']
    
    if best_solution:
        timetable = {}
        for exam, (day, slot) in best_solution.items():
            subject = problem.get_subject_info(exam)
            slot_times = ['9:00-12:00', '12:00-15:00', '15:00-18:00']
            duration = 2 if subject['has_lab'] else 1
            
            end_slot = (slot + duration - 1) % problem.SLOTS_PER_DAY
            end_time = slot_times[end_slot].split('-')[1]
            
            timetable[exam] = {
                'day': day + 1,
                'start_slot': slot,
                'duration': duration,
                'time': f"{slot_times[slot].split('-')[0]}-{end_time}",
                'subject': subject
            }
        
        # Print timetable sorted by day and time
        print("\nΠρόγραμμα Εξεταστικής:")
        print("-" * 60)
        for day in range(1, problem.DAYS + 1):
            day_exams = [(exam, info) for exam, info in timetable.items() if info['day'] == day]
            if day_exams:
                print(f"\nΗμέρα {day}:")
                # Sort by start slot
                day_exams.sort(key=lambda x: x[1]['start_slot'])
                for exam, info in day_exams:
                    subject = info['subject']
                    duration = "6 ώρες" if subject['has_lab'] else "3 ώρες"
                    print(f"{info['time']}: {subject['name']} ({duration}) - {subject['professor']}")
        return timetable
    else:
        print("Δεν βρέθηκε εφικτή λύση!")
        return None

if __name__ == "__main__":
    num_days = int(input("Enter the number of days for the exam period: "))
    all_exams = input("Include all exams? (y/n): ").lower().strip()
    all_exams = all_exams in ['y', 'yes', '', 'Y', 'YES']

    timetable = solve_timetable('h3-data.csv', num_days, all_exams)