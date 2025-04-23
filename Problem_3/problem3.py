from csp import CSP, AC3

def schedule_constraint(A, a, B, b):
    """
    Constraint function that checks if two activities satisfy the scheduling constraints.
    A, B are activities (A1-A5), and a, b are their respective start times (9, 10, or 11).
    """
    # If it's the same activity, no constraint needed
    if A == B:
        return True
    
    # A1 must start after A3
    if (A == 'A1' and B == 'A3'):
        return a > b
    if (A == 'A3' and B == 'A1'):
        return b > a
    
    # A3 must start before A4 and after A5
    if (A == 'A3' and B == 'A4'):
        return a < b
    if (A == 'A4' and B == 'A3'):
        return b < a
    
    if (A == 'A3' and B == 'A5'):
        return a > b
    if (A == 'A5' and B == 'A3'):
        return b > a
    
    # A2 cannot run at the same time as A1 or A4
    if (A == 'A2' and (B == 'A1' or B == 'A4')) or ((A == 'A1' or A == 'A4') and B == 'A2'):
        return a != b
    
    # All other pairs of activities can run at any time
    return True

def create_schedule_csp():
    """Create and return a CSP for the scheduling problem."""
    # Variables: A1, A2, A3, A4, A5
    variables = ['A1', 'A2', 'A3', 'A4', 'A5']
    
    # Domains: Each activity can start at 9:00, 10:00, or 11:00
    # For A4, we exclude 10:00 as per the constraint
    domains = {
        'A1': [9, 10, 11],
        'A2': [9, 10, 11],
        'A3': [9, 10, 11],
        'A4': [9, 11],  # A4 cannot start at 10:00
        'A5': [9, 10, 11]
    }
    
    # Each activity potentially affects every other activity
    neighbors = {var: [other for other in variables if other != var] for var in variables}
    
    return CSP(variables, domains, neighbors, schedule_constraint)

def solve_schedule():
    """Create and solve the scheduling CSP."""
    csp = create_schedule_csp()
    # Apply AC-3 algorithm
    is_consistent, checks = AC3(csp)
    
    if not is_consistent:
        return None, "Problem is inconsistent after AC-3"
    
    if csp.curr_domains is None:
        return None, "Current domains are not set."

    # Get the reduced domains after AC-3
    domains_after_ac3 = {var: list(csp.curr_domains[var]) for var in csp.variables}
    
    return domains_after_ac3, checks


if __name__ == "__main__":
    # Solve the CSP
    domains, checks = solve_schedule()
    if domains:
        print("\nDomains after AC-3:")
        for var in sorted(domains.keys()):
            print(f"{var}: {domains[var]}")
        print(f"\nNumber of constraint checks: {checks}")
    else:
        print("No solution exists.")
