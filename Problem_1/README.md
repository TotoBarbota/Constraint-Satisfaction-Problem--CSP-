# Program 1: Exam Timetable

## Execution

In order to run the program run ```python ./problem1```

Once run, the program will ask you to input the number of days the exam will last.

After that the program will ask you if you want to rn only the Min Conflict algorithm or all the possible compbination.

The possible combinations are:

Min-Conflicts,
MAC with MRV,
MAC with dom/wdeg,
FC with MRV,
FC with dom/wdeg

After that the program will show you the result of the algorithm(s), the time it took and the number of assignments, along with the exam slots.

Changes have also been made on the ```csp.py``` program in order to implement the dom/wdeg heuristic. 

The heuristic MRV along with the fucntion MAC and FC where not changed and are used as given. 

# Constains

The constains that we were asked to implement were:

- 3 time slots per day (9:00-12:00, 12:00-15:00, 15:00-18:00)
- each subject has a unique name, professor, semester, and whether it is difficult or not.
- for each subject the exam duration must be 3 hours.
- subject with the same semester must be examed different days
- If a subject has a lab, the lab must be exammed after the theory
- a difficult subject must have a two day gap between them
- subjects from the same professor must be exammed different days 

## SubClass ExamTimetabling
A subclass ExamTimetabling of CSP was created for ease of fucntion. This subclass holds the number of days, slots per day and the subjects. When the initialiase this class, the subjects are read from the file and stored, adn then starts the creation of the Domains and the Neighbors. 

## Constains implementaion

Using the information mentioned above the constraints are created to make sure that the exams are valid. First, we check for the similarity to avoid checking the same subject.
Then we continue by checking the day:
    If we are on the same day:
        - we Check for overlapping time slots
        - Calculate the slots each exam takes depending on if it has a lab or not, if it has it takes 2 slots
        - We re-check for the overlapping time slots
        - Check for the same proffessor
        - Cgheck for the same semester
If none of these constaints are triggered, then we check if the two subjects are difficult. If they are we make sure that the days between them are 2 apart.

# Results

As we can see the MAC algorithm using the MRV heuristic takes a long time to compute ( 6.44 seconds ), opposite to using the dom/wdeg heuristic which is completed in 0.03 seconds, similar with the other test cases. 

### Days -> 21

Comparison Table:
--------------------------------------------------------------------------------
Method                    Time (s)        Assignments     Solution Found
--------------------------------------------------------------------------------
Min-Conflicts             0.29            38              Yes     
MAC with MRV              6.44            38              Yes     
MAC with dom/wdeg         0.03            38              Yes     
FC with MRV               0.01            38              Yes     
FC with dom/wdeg          0.02            38              Yes     
--------------------------------------------------------------------------------

Πρόγραμμα Εξεταστικής:
------------------------------------------------------------

Ημέρα 1:
9:00-15:00: Τεχνητή Νοηµοσύνη (ΤΟ ΚΑΛΥΤΕΡΟ!!!!) (6 ώρες) - ΚΟΥΜΠΑΡΑΚΗΣ
15:00-18:00: Υπολογιστική Πολυπλοκότητα (3 ώρες) - ΓΙΑΝΝΟΠΟΥΛΟΥ

Ημέρα 2:
9:00-15:00: Τεχνητή Νοημοσύνη ΙΙ (ΤΟ ΔΕΥΤΕΡΟ ΚΑΛΥΤΕΡΟ!!!) (6 ώρες) - ΚΟΥΜΠΑΡΑΚΗΣ
15:00-18:00: Εφαρμοσμένα Μαθηματικά (3 ώρες) - ΓΑΤΖΟΥΡΑ

Ημέρα 3:
9:00-15:00: Αντικειµενοστραφής Προγραµµατισµός (6 ώρες) - ΚΑΡΑΛΗ
15:00-18:00: Σχεδίαση Ψηφιακών Συστηµάτων -VHDL (3 ώρες) - ΠΑΣΧΑΛΗΣ

Ημέρα 4:
9:00-15:00: Υλοποίηση Συστημάτων Βάσεων Δεδομένων (6 ώρες) - ΙΩΑΝΝΙΔΗΣ
15:00-18:00: Πιθανότητες και στοιχεία Στατιστικής (3 ώρες) - ΚΑΡΑΛΙΟΠΟΥΛΟΥ

Ημέρα 5:
9:00-15:00: Εισαγωγή στον Προγραµµατισµό (6 ώρες) - ΣΤΑΜΑΤΟΠΟΥΛΟΣ
15:00-18:00: Δίκτυα Επικοινωνιών ΙΙ (3 ώρες) - ΜΠΑΛΑΟΥΡΑΣ

Ημέρα 6:
9:00-12:00: Αριθµητική Ανάλυση (3 ώρες) - ΤΖΑΦΕΡΗΣ
12:00-15:00: Εισαγωγή στην Πληροφορική και στις Τηλεπικοινωνίες (3 ώρες) - ΤΣΑΛΓΑΤΙΔΟΥ
15:00-18:00: Εργαστήριο Κυκλωμάτων και Συστημάτων (3 ώρες) - ΠΙΝΟ

Ημέρα 7:
9:00-12:00: Λειτουργικά Συστήµατα (3 ώρες) - ΧΑΤΖΗΕΥΘΥΜΙΑΔΗΣ
12:00-15:00: Διακριτά Μαθηµατικά (3 ώρες) - ΑΧΛΙΟΠΤΑΣ
15:00-18:00: Ειδικά Θέματα Επικοινωνιών και Επεξεργασίας Σήματος: Ενισχυτική μηχανική μάθηση και στοχαστικά παίγνια (3 ώρες) - ΚΑΛΟΥΠΤΣΙΔΗΣ

Ημέρα 8:
9:00-12:00: Αρχιτεκτονική Υπολογιστών ΙΙ (3 ώρες) - ΓΚΙΖΟΠΟΥΛΟΣ
12:00-15:00: Λογική Σχεδίαση (3 ώρες) - ΠΑΣΧΑΛΗΣ
15:00-18:00: Ειδικά Θέματα Θεωρητικής Πληροφορικής: Αλγόριθμοι Δομικής Βιοπληροφορικής (3 ώρες) - ΑΧΛΙΟΠΤΑΣ

Ημέρα 9:
9:00-12:00: Ψηφιακή Επεξεργασία Σήµατος (3 ώρες) - ΑΛΕΞΑΝΔΡΟΠΟΥΛΟΣ
12:00-15:00: Ανάπτυξη Λογισµικού για Πληροφοριακά Συστήματα (3 ώρες) - ΙΩΑΝΝΙΔΗΣ

Ημέρα 10:
9:00-12:00: Σήµατα και Συστήµατα (3 ώρες) - ΠΑΝΑΓΑΚΗΣ
12:00-15:00: Τηλεπικοινωνιακά Δίκτυα (3 ώρες) - ΒΑΡΟΥΤΑΣ
15:00-18:00: Ανάπτυξη Λογισµικού για Αλγοριθμικά Προβλήματα (3 ώρες) - ΕΜΙΡΗΣ

Ημέρα 11:
9:00-12:00: Γραφικά Ι (3 ώρες) - ΘΕΟΧΑΡΗΣ
12:00-15:00: Συστήματα Πληροφορικής και e-Προσβασιμότητα για μαθητές με αναπηρία (3 ώρες) - ΠΙΝΟ

Ημέρα 12:
9:00-12:00: Ανάλυση ΙΙ (3 ώρες) - ΓΑΤΖΟΥΡΑ
12:00-15:00: Αρχές Γλωσσών Προγραµµατισµού (3 ώρες) - ΡΟΝΤΟΓΙΑΝΝΗΣ
15:00-18:00: Προηγμένοι Επιστημονικοί Υπολογισμοί (3 ώρες) - ΤΖΑΦΕΡΗΣ

Ημέρα 13:
9:00-12:00: Επικοινωνία Ανθρώπου Μηχανής (3 ώρες) - ΡΟΥΣΣΟΥ

Ημέρα 14:
9:00-12:00: Γραµµική Άλγεβρα (3 ώρες) - ΓΙΑΝΝΟΠΟΥΛΟΥ
12:00-15:00: Δοµή και Θεσµοί της Ευρωπαϊκής Ένωσης (3 ώρες) - ΤΟΛΙΔΗΣ

Ημέρα 15:
9:00-12:00: Αλγόριθμοι Βιοπληροφορικής (3 ώρες) - ΕΜΙΡΗΣ

Ημέρα 16:
9:00-12:00: Αλγοριθµική Επιχειρησιακή Έρευνα (3 ώρες) - ΖΗΣΙΜΟΠΟΥΛΟΣ

Ημέρα 17:
9:00-12:00: Ανάπτυξη Λογισμικού για Συστήματα Δικτύων και Τηλεπικοινωνιών (3 ώρες) - ΜΠΑΛΑΟΥΡΑΣ

Ημέρα 18:
9:00-12:00: Σχεδίαση VLSI Κυκλωµάτων (3 ώρες) - ΝΙΚΑΣ

Ημέρα 19:
9:00-12:00: ΤΠΕ στη Μάθηση (Πληροφορική κ Εκπαίδευση) (3 ώρες) - ΓΟΓΟΥΛΟΥ

Ημέρα 20:
9:00-12:00: Προηγµένα Θέµατα Αλγορίθµων (3 ώρες) - ΦΟΥΡΤΟΥΝΕΛΗ


## Problems

For days lower tha 20, the backtracking algorithms are too slow to recomment. In my testing, 7 minutes were not enought to get results using the MAC and FC algorithms. 
The Min-Conflicts algorithm on the other hand, is the only one that can complete the task fast and reliably. We managed to get results using it for days as low as 16 taking 1.56 seconds to complete.

### Following you can see the results for 16 days:

Testing: Min-Conflicts
Time taken: 1.56 seconds
Solution found: Yes

Comparison Table:
--------------------------------------------------------------------------------
Method                    Time (s)        Assignments     Solution Found
--------------------------------------------------------------------------------
Min-Conflicts             1.56            122             Yes     
--------------------------------------------------------------------------------

Πρόγραμμα Εξεταστικής:
------------------------------------------------------------

Ημέρα 1:
9:00-12:00: Ανάπτυξη Λογισµικού για Πληροφοριακά Συστήματα (3 ώρες) - ΙΩΑΝΝΙΔΗΣ
12:00-18:00: Τεχνητή Νοηµοσύνη (ΤΟ ΚΑΛΥΤΕΡΟ!!!!) (6 ώρες) - ΚΟΥΜΠΑΡΑΚΗΣ

Ημέρα 2:
9:00-12:00: Αριθµητική Ανάλυση (3 ώρες) - ΤΖΑΦΕΡΗΣ
15:00-18:00: Δοµή και Θεσµοί της Ευρωπαϊκής Ένωσης (3 ώρες) - ΤΟΛΙΔΗΣ

Ημέρα 3:
9:00-15:00: Αντικειµενοστραφής Προγραµµατισµός (6 ώρες) - ΚΑΡΑΛΗ
15:00-18:00: Συστήματα Πληροφορικής και e-Προσβασιμότητα για μαθητές με αναπηρία (3 ώρες) - ΠΙΝΟ

Ημέρα 4:
9:00-12:00: Γραφικά Ι (3 ώρες) - ΘΕΟΧΑΡΗΣ
15:00-18:00: Αλγοριθµική Επιχειρησιακή Έρευνα (3 ώρες) - ΖΗΣΙΜΟΠΟΥΛΟΣ

Ημέρα 5:
9:00-15:00: Υλοποίηση Συστημάτων Βάσεων Δεδομένων (6 ώρες) - ΙΩΑΝΝΙΔΗΣ
15:00-18:00: Σχεδίαση VLSI Κυκλωµάτων (3 ώρες) - ΝΙΚΑΣ

Ημέρα 6:
9:00-12:00: Ειδικά Θέματα Θεωρητικής Πληροφορικής: Αλγόριθμοι Δομικής Βιοπληροφορικής (3 ώρες) - ΑΧΛΙΟΠΤΑΣ
12:00-18:00: Εισαγωγή στον Προγραµµατισµό (6 ώρες) - ΣΤΑΜΑΤΟΠΟΥΛΟΣ

Ημέρα 7:
9:00-12:00: Δίκτυα Επικοινωνιών ΙΙ (3 ώρες) - ΜΠΑΛΑΟΥΡΑΣ
12:00-15:00: Ειδικά Θέματα Επικοινωνιών και Επεξεργασίας Σήματος: Ενισχυτική μηχανική μάθηση και στοχαστικά παίγνια (3 ώρες) - ΚΑΛΟΥΠΤΣΙΔΗΣ
15:00-18:00: Ανάλυση ΙΙ (3 ώρες) - ΓΑΤΖΟΥΡΑ

Ημέρα 8:
9:00-12:00: Λογική Σχεδίαση (3 ώρες) - ΠΑΣΧΑΛΗΣ
12:00-15:00: ΤΠΕ στη Μάθηση (Πληροφορική κ Εκπαίδευση) (3 ώρες) - ΓΟΓΟΥΛΟΥ
15:00-18:00: Αρχές Γλωσσών Προγραµµατισµού (3 ώρες) - ΡΟΝΤΟΓΙΑΝΝΗΣ

Ημέρα 9:
9:00-12:00: Λειτουργικά Συστήµατα (3 ώρες) - ΧΑΤΖΗΕΥΘΥΜΙΑΔΗΣ
12:00-18:00: Τεχνητή Νοημοσύνη ΙΙ (ΤΟ ΔΕΥΤΕΡΟ ΚΑΛΥΤΕΡΟ!!!) (6 ώρες) - ΚΟΥΜΠΑΡΑΚΗΣ

Ημέρα 10:
9:00-12:00: Ανάπτυξη Λογισµικού για Αλγοριθμικά Προβλήματα (3 ώρες) - ΕΜΙΡΗΣ
15:00-18:00: Ψηφιακή Επεξεργασία Σήµατος (3 ώρες) - ΑΛΕΞΑΝΔΡΟΠΟΥΛΟΣ

Ημέρα 11:
9:00-12:00: Αλγόριθμοι Βιοπληροφορικής (3 ώρες) - ΕΜΙΡΗΣ
12:00-15:00: Σχεδίαση Ψηφιακών Συστηµάτων -VHDL (3 ώρες) - ΠΑΣΧΑΛΗΣ
15:00-18:00: Εργαστήριο Κυκλωμάτων και Συστημάτων (3 ώρες) - ΠΙΝΟ

Ημέρα 12:
9:00-12:00: Γραµµική Άλγεβρα (3 ώρες) - ΓΙΑΝΝΟΠΟΥΛΟΥ
12:00-15:00: Εφαρμοσμένα Μαθηματικά (3 ώρες) - ΓΑΤΖΟΥΡΑ
15:00-18:00: Προηγµένα Θέµατα Αλγορίθµων (3 ώρες) - ΦΟΥΡΤΟΥΝΕΛΗ

Ημέρα 13:
9:00-12:00: Ανάπτυξη Λογισμικού για Συστήματα Δικτύων και Τηλεπικοινωνιών (3 ώρες) - ΜΠΑΛΑΟΥΡΑΣ
12:00-15:00: Εισαγωγή στην Πληροφορική και στις Τηλεπικοινωνίες (3 ώρες) - ΤΣΑΛΓΑΤΙΔΟΥ

Ημέρα 14:
9:00-12:00: Αρχιτεκτονική Υπολογιστών ΙΙ (3 ώρες) - ΓΚΙΖΟΠΟΥΛΟΣ
15:00-18:00: Υπολογιστική Πολυπλοκότητα (3 ώρες) - ΓΙΑΝΝΟΠΟΥΛΟΥ

Ημέρα 15:
9:00-12:00: Διακριτά Μαθηµατικά (3 ώρες) - ΑΧΛΙΟΠΤΑΣ
12:00-15:00: Πιθανότητες και στοιχεία Στατιστικής (3 ώρες) - ΚΑΡΑΛΙΟΠΟΥΛΟΥ
15:00-18:00: Επικοινωνία Ανθρώπου Μηχανής (3 ώρες) - ΡΟΥΣΣΟΥ

Ημέρα 16:
9:00-12:00: Προηγμένοι Επιστημονικοί Υπολογισμοί (3 ώρες) - ΤΖΑΦΕΡΗΣ
12:00-15:00: Τηλεπικοινωνιακά Δίκτυα (3 ώρες) - ΒΑΡΟΥΤΑΣ
15:00-18:00: Σήµατα και Συστήµατα (3 ώρες) - ΠΑΝΑΓΑΚΗΣ


