from csp import CSP, min_conflicts, backtracking_search
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class RoomFurnitureCSP(CSP):
    def __init__(self):
        # Room dimensions
        self.room_width = 300  # x
        self.room_length = 400  # z
        self.room_height = 230  # y
        
        # Furniture dimensions (width, length, height)
        self.bed = (100, 200, 80)
        self.desk = (160, 80, 90)
        self.chair = (41, 44, 57)
        self.sofa = (221, 103, 84)
        
        # Define variables: (x, z) coordinates for each piece of furniture
        variables = ['bed_x', 'bed_z', 'desk_x', 'desk_z', 'chair_x', 'chair_z', 'sofa_x', 'sofa_z']
        
        # Define domains: possible positions for each coordinate (using 20cm steps)
        STEP = 20  # 20cm steps to reduce search space
        domains = {}
        
        # Bed domains
        domains['bed_x'] = list(range(0, self.room_width - self.bed[0] + 1, STEP))
        domains['bed_z'] = list(range(0, self.room_length - self.bed[1] + 1, STEP))
        # Desk domains
        domains['desk_x'] = list(range(0, self.room_width - self.desk[0] + 1, STEP))
        domains['desk_z'] = list(range(0, self.room_length - self.desk[1] + 1, STEP))
        # Chair domains
        domains['chair_x'] = list(range(0, self.room_width - self.chair[0] + 1, STEP))
        domains['chair_z'] = list(range(0, self.room_length - self.chair[1] + 1, STEP))
        # Sofa domains
        domains['sofa_x'] = list(range(0, self.room_width - self.sofa[0] + 1, STEP))
        domains['sofa_z'] = list(range(0, self.room_length - self.sofa[1] + 1, STEP))
        
        # Add wall positions explicitly for bed and desk
        if self.room_width - self.bed[0] not in domains['bed_x']:
            domains['bed_x'].append(self.room_width - self.bed[0])
        if self.room_width - self.desk[0] not in domains['desk_x']:
            domains['desk_x'].append(self.room_width - self.desk[0])
        
        # Define neighbors
        neighbors = {}
        for var in variables:
            neighbors[var] = [other_var for other_var in variables if other_var != var]
        
        CSP.__init__(self, variables, domains, neighbors, self.constraints)
    
    def constraints(self, A, a, B, b):
        """Check if the assignment of value a to variable A and b to variable B satisfies the constraints"""
        # Get current assignments
        assignments = self.infer_assignment()
        if A not in assignments:
            assignments[A] = a
        if B not in assignments:
            assignments[B] = b
            
        # Extract furniture piece from variable name
        piece_A = A.split('_')[0]
        coord_A = A.split('_')[1]
        piece_B = B.split('_')[0]
        coord_B = B.split('_')[1]
        
        # If we're checking the same piece's coordinates
        if piece_A == piece_B:
            return True
        
        # Get dimensions for the pieces
        dims_A = getattr(self, piece_A)
        dims_B = getattr(self, piece_B)
        
        # Check if furniture fits in either orientation
        def fits(x, z, width, length):
            return (x + width <= self.room_width and z + length <= self.room_length) or \
                   (x + length <= self.room_width and z + width <= self.room_length)

        # Ensure furniture fits in the room
        if not fits(a, b, dims_A[0], dims_A[1]):
            return False

        # Check for furniture overlap in both orientations
        if piece_A != piece_B:
            x_A = assignments.get(f'{piece_A}_x', -1)
            z_A = assignments.get(f'{piece_A}_z', -1)
            x_B = assignments.get(f'{piece_B}_x', -1)
            z_B = assignments.get(f'{piece_B}_z', -1)
            
            if -1 not in [x_A, z_A, x_B, z_B]:
                no_overlap = (
                    (x_A + dims_A[0] <= x_B or x_B + dims_B[0] <= x_A or z_A + dims_A[1] <= z_B or z_B + dims_B[1] <= z_A) and
                    (x_A + dims_A[1] <= x_B or x_B + dims_B[1] <= x_A or z_A + dims_A[0] <= z_B or z_B + dims_B[0] <= z_A)
                )
                if not no_overlap:
                    return False

        # Ensure no furniture overlaps with room door area (0-100, 0-100)
        if (0 <= a <= 100 and 0 <= b <= 100):
            return False

        # Door constraints
        if coord_A == 'x' and coord_B == 'z':
            # Check balcony door area (200-300, 400)
            if (200 <= a <= 300 and b >= 300):
                return False

        # Wall constraint for bed
        if piece_A == 'bed' and coord_A == 'x':
            # Must be against a wall
            if a != 0 and a != (self.room_width - dims_A[0]):
                return False
        
        # Wall and light constraint for desk
        if piece_A == 'desk':
            desk_width, desk_length = dims_A[0], dims_A[1]
            long_side = max(desk_width, desk_length)
            if coord_A == 'x':
                # Must be against a wall and opposite to balcony door
                if (a != 0 and a != (self.room_width - desk_width)) or a >= 200:
                    return False
                # Check if long side touches a wall when desk is placed horizontally
                if long_side == desk_width and (b != 0 and b != (self.room_length - desk_length)):
                    return False
            elif coord_A == 'z':
                # Check if long side touches a wall when desk is placed vertically
                if long_side == desk_length and (a != 0 and a != (self.room_width - desk_width)):
                    return False
        # # Center chair along the longer side of the desk
        if piece_A == 'chair' and piece_B == 'desk' and coord_A == 'x':
            desk_x = assignments.get('desk_x', -1)
            if desk_x != -1:
                center_x = desk_x + (dims_B[0] // 2) - (dims_A[0] // 2)
                if abs(a - center_x) > 10:  # Allow a small margin of error
                    return False
        
        return True

def draw_room(solution):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Room dimensions
    room_width = 300
    room_length = 400
    
    # Draw room outline
    room = patches.Rectangle((0, 0), room_width, room_length, fill=False, color='black')
    ax.add_patch(room)
    
    # Draw balcony door (200-300, 400)
    balcony_door = patches.Rectangle((200, 395), 100, 5, color='lightblue', alpha=0.5)
    ax.add_patch(balcony_door)
    
    # Draw room door (0-100, 0)
    room_door = patches.Rectangle((0, 0), 100, 5, color='brown', alpha=0.5)
    ax.add_patch(room_door)
    
    if solution:
        # Draw bed
        bed = patches.Rectangle((solution['bed_x'], solution['bed_z']), 100, 200, 
                              color='red', alpha=0.5, label='Bed')
        ax.add_patch(bed)
        
        # Draw desk
        desk = patches.Rectangle((solution['desk_x'], solution['desk_z']), 160, 80, 
                               color='blue', alpha=0.5, label='Desk')
        ax.add_patch(desk)
        
        # Draw chair
        chair = patches.Rectangle((solution['chair_x'], solution['chair_z']), 41, 44, 
                                color='green', alpha=0.5, label='Chair')
        ax.add_patch(chair)
        
        # Draw sofa
        sofa = patches.Rectangle((solution['sofa_x'], solution['sofa_z']), 221, 103, 
                               color='purple', alpha=0.5, label='Sofa')
        ax.add_patch(sofa)
    
    # Add legend
    ax.legend()
    
    # Set equal aspect ratio and limits
    ax.set_aspect('equal')
    ax.set_xlim(-50, room_width + 50)
    ax.set_ylim(-50, room_length + 50)
    
    # Add labels
    ax.set_xlabel('Width (cm)')
    ax.set_ylabel('Length (cm)')
    ax.set_title('Room Layout')
    
    # Add grid
    ax.grid(True, linestyle='--', alpha=0.3)
    
    plt.show()

def solve_room_layout():
    problem = RoomFurnitureCSP()
    solution = backtracking_search(problem)
    
    if solution:
        print("Found a valid furniture arrangement!")
        print("\nFurniture positions (x, z):")
        print(f"Bed: ({solution['bed_x']}, {solution['bed_z']})")
        print(f"Desk: ({solution['desk_x']}, {solution['desk_z']})")
        print(f"Chair: ({solution['chair_x']}, {solution['chair_z']})")
        print(f"Sofa: ({solution['sofa_x']}, {solution['sofa_z']})")
        
        # Draw the room layout
        draw_room(solution)
        return True
    else:
        print("No valid furniture arrangement found!")
        return False

if __name__ == "__main__":
    solve_room_layout()
