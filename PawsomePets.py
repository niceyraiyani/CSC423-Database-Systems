import sqlite3
import pandas as pd

db_connect = sqlite3.connect('CSC423Project.db')
cursor = db_connect.cursor()
cursor.execute("DROP TABLE IF EXISTS Owner")
cursor.execute("DROP TABLE IF EXISTS Clinic")
cursor.execute("DROP TABLE IF EXISTS Pet")
cursor.execute("DROP TABLE IF EXISTS Staff")
cursor.execute("DROP TABLE IF EXISTS Examination")
cursor.execute("DROP TABLE IF EXISTS Breed")



# ================================================================
#                    SQL Table Generation
# ================================================================

# Owner Table
query = """
    CREATE TABLE IF NOT EXISTS Owner(
        ownerNo INT,
        ownerName VARCHAR(15),
        ownerAddress VARCHAR(255),
        ownerTeleNo VARCHAR(10),
        PRIMARY KEY (ownerNo)
    );
    """
cursor.execute(query)

# Clinic Table
query = """
    CREATE TABLE IF NOT EXISTS Clinic(
        clinicNo INT,
        clinicName VARCHAR(25),
        clinicAddress VARCHAR(255),
        clinicTeleNo VARCHAR(10),
        managerStaffNo INT,
        PRIMARY KEY (clinicNo),
        FOREIGN KEY (managerStaffNo) REFERENCES Staff(staffNo)
    );
    """
cursor.execute(query)

# Pet Table
query = """
    CREATE TABLE IF NOT EXISTS Pet(
        petNo INT,
        petName VARCHAR(25),
        petDOB DATE,
        petBreed VARCHAR(25),
        petColor VARCHAR(15),
        ownerNo INT,
        clinicNo INT,
        PRIMARY KEY (petNo),
        FOREIGN KEY (petBreed) REFERENCES Breed(petBreed),
        FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    );
    """
cursor.execute(query)

# Staff Table
query = """
    CREATE TABLE IF NOT EXISTS Staff(
        staffNo INT,
        staffName VARCHAR(15),
        staffAddress VARCHAR(255),
        staffTeleNo VARCHAR(10),
        staffDOB DATE,
        position VARCHAR(20),
        salary INT,
        clinicNo INT,
        PRIMARY KEY (staffNo),
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    );
    """
cursor.execute(query)

# Examination Table
query = """
    CREATE TABLE IF NOT EXISTS Examination(
        examNo INT,
        chiefComplaint VARCHAR(255),
        description VARCHAR(255),
        dateSeen DATE,
        actionsTaken VARCHAR(255),
        petNo INT,
        staffNo INT,
        PRIMARY KEY (examNo),
        FOREIGN KEY (petNo) REFERENCES Pet(petNo),
        FOREIGN KEY (staffNo) REFERENCES Staff(staffNo)
    );
    """
cursor.execute(query)

# Breed Table
query = """
    CREATE TABLE IF NOT EXISTS Breed(
        petBreed VARCHAR(25),
        petSpecies VARCHAR(15),
        PRIMARY KEY (petBreed)
    );
    """
cursor.execute(query)


# ================================================================
#                     Test Data Population
# ================================================================
cursor.execute("PRAGMA foreign_keys = OFF;")
# Function to print a table or a view
def printTable(cursor, tableName):
    print('Table:', tableName)
    db_connect.commit()
    query = f"SELECT * FROM {tableName}"
    cursor.execute(query)
    table_data = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    df = pd.DataFrame(table_data, columns=column_names)
    # Print the DataFrame and its columns
    print(df)


def printAllTables(cursor):
    print('\n ### PAWSOME PETS DATABASE \n')
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        printTable(cursor, table_name)
        print('--------------------------------------------------------------------------------------------------------------------------------\n')
    
    print('--------------------------------------------------------------------------------------------------------------------------------\n')
printAllTables(cursor)
## Add 5 rows of data to each table
# Breed Table
query = """
    INSERT INTO Breed (petBreed, petSpecies) 
    VALUES 
        ('Golden Retriever', 'Dog'),
        ('Siamese Cat', 'Cat'),
        ('Bulldog', 'Dog'),
        ('Persian Cat', 'Cat'),
        ('Beagle', 'Dog');
    """
cursor.execute(query)

# Owner Table
query = """
    INSERT INTO Owner (ownerNo, ownerName, ownerAddress, ownerTeleNo) 
    VALUES 
        (1, 'John Doe', '123 Elm St, Miami, FL', '3051234567'),
        (2, 'Jane Smith', '456 Oak St, Miami, FL', '3059876543'),
        (3, 'Mike Johnson', '789 Pine St, Miami, FL', '3054567890'),
        (4, 'Emily Davis', '101 Maple St, Miami, FL', '3056781234'),
        (5, 'Anna Brown', '202 Birch St, Miami, FL', '3055436789');
    """
cursor.execute(query)

# Staff Table
query = """
    INSERT INTO Staff (staffNo, staffName, staffAddress, staffTeleNo, staffDOB, position, salary, clinicNo) 
    VALUES 
        (1, 'Alice Alon', '120 Elm St, Miami, FL', '3051112222', '1980-04-15', 'Manager', 120000, 1),
        (2, 'Bob Brown', '130 Oak St, Miami, FL', '3052223333', '1985-08-10', 'Manager', 115000, 2),
        (3, 'Carol Corne', '140 Pine St, Miami, FL', '3053334444', '1975-12-20', 'Manager', 130000, 3),
        (4, 'David Doogle', '150 Maple St, Miami, FL', '3054445555', '1990-06-25', 'Manager', 110000, 4),
        (5, 'Eve Evette', '160 Birch St, Miami, FL', '3055556666', '1982-11-30', 'Manager', 125000, 5),
        (6, 'Faruq Fonty', '170 Red Rd, Miami, FL', '305111333', '2002-17-08', 'Examiner', '6000', 6);
    """
cursor.execute(query)

# Clinic Table
query = """
    INSERT INTO Clinic (clinicNo, clinicName, clinicAddress, clinicTeleNo, managerStaffNo) 
    VALUES 
        (1, 'Pet Care Center', '500 Main St, Miami, FL', '3051234560', 1),
        (2, 'Animal Health Clinic', '600 Main St, Miami, FL', '3059876540', 2),
        (3, 'Happy Tails Clinic', '700 Main St, Miami, FL', '3054567899', 3),
        (4, 'Best Friend Vet', '800 Main St, Miami, FL', '3056781239', 4),
        (5, 'Pawfect Care', '900 Main St, Miami, FL', '3055436780', 5);
    """
cursor.execute(query)

# Pet Table
query = """
    INSERT INTO Pet (petNo, petName, petDOB, petBreed, petColor, ownerNo, clinicNo) 
    VALUES 
        (1, 'Buddy', '2021-01-15', 'Golden Retriever', 'Golden', 1, 1),
        (2, 'Mittens', '2020-05-20', 'Siamese Cat', 'White', 2, 2),
        (3, 'Max', '2019-07-10', 'Bulldog', 'Brown', 3, 3),
        (4, 'Bella', '2022-03-25', 'Persian Cat', 'Gray', 4, 4),
        (5, 'Charlie', '2021-09-05', 'Beagle', 'Tri-color', 5, 5);
    """
cursor.execute(query)

# Examination Table
query = """
    INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, petNo, staffNo) 
    VALUES 
        (1, 'Coughing', 'Persistent cough and lethargy', '2024-01-15', 'Prescribed medication', 1, 1),
        (2, 'Limping', 'Injury to front left leg', '2024-02-10', 'Applied bandage', 2, 2),
        (3, 'Vomiting', 'Repeated vomiting and loss of appetite', '2024-03-05', 'Administered IV fluids', 3, 3),
        (4, 'Skin Rash', 'Redness and irritation on skin', '2024-04-20', 'Prescribed ointment', 4, 4),
        (5, 'Ear Infection', 'Discharge and odor from ears', '2024-05-12', 'Cleaned ears and prescribed drops', 5, 5);
    """
cursor.execute(query)


printAllTables(cursor)


# ================================================================
#                     SQL Queries
# ================================================================


# To enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Transaction 1
print("# Transaction 1: Register a New Pet Owner and their Pet(s) at a clinic")

# Register a new owner
cursor.execute("""
    INSERT INTO Owner (ownerNo, ownerName, ownerAddress, ownerTeleNo)
    VALUES (6, 'Sarah Connor', '12 Skynet St, Miami, FL', '3055551234');
""")
print("Inserted new owner:")
cursor.execute("SELECT * FROM Owner WHERE ownerNo = 6;")
print(cursor.fetchall())

# Constraint check: Check if clinicNo = 1 exists
cursor.execute("SELECT * FROM Clinic WHERE clinicNo = 1;")
clinic = cursor.fetchone()
if not clinic:
    raise ValueError("Clinic with clinicNo = 1 does not exist.")
print("Constraint check 1: Clinic exists:", clinic)

# Constraint check: Check if ownerNo exists
cursor.execute("SELECT * FROM Owner WHERE ownerNo = 6;")
owner = cursor.fetchone()
if not owner:
    raise ValueError("Owner with ownerNo = 6 does not exist.")
print("Constraint check 2: Owner 6 exists" )

# Register pets for the owner
cursor.execute("""
    INSERT INTO Pet (petNo, petName, petDOB, petBreed, petColor, ownerNo, clinicNo)
    VALUES 
        (6, 'Rex', '2022-05-01', 'Golden Retriever', 'Brown', 6, 1),
        (7, 'Daisy', '2023-01-15', 'Persian Cat', 'Black', 6, 1);
""")

print("Inserted new pets:")
cursor.execute("SELECT * FROM Pet WHERE ownerNo = 6;")
print(cursor.fetchall())


# Transaction 2: Schedule an Examination for a Pet
print("\n# Transaction 2: Schedule an Examination for a Pet ")

# Constraint check: Check if staff exists
cursor.execute("SELECT * FROM Staff WHERE staffNo = 1;")
staff = cursor.fetchone()
if not staff:
    raise ValueError("Staff with staffNo = 1 does not exist.")
print("Constraint Check 1: Staff 1 exists" )
# Constraint check: Check if pet exists
cursor.execute("SELECT * FROM Pet WHERE petNo = 6;")
pet = cursor.fetchone()
if not pet:
    raise ValueError("Pet with petNo = 6 does not exist.")
print("Constraint Check 2: Pet 6 exists" )

# Schedule an examination
cursor.execute("""
    INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, petNo, staffNo)
    VALUES (6, 'Limping', 'Injury to front paw', '2024-12-05', 'Prescribed anti-biotics', 6, 1);
""")

cursor.execute("SELECT * FROM Examination WHERE examNo = 6;")
print(cursor.fetchall())

# Transaction 3: Update a Pet’s medical records after an examination
print("\n# Transaction 3: Update a Pet's medical records after an examination ")

# Constraint check: Check if examNo exists
cursor.execute("SELECT * FROM Examination WHERE examNo = 2;")
exam = cursor.fetchone()
if not exam:
    raise ValueError("Examination with examNo = 2 does not exist.")
print("Constraint Check 1: Exam 2 exists" )

# Update the examination record
cursor.execute("""
    UPDATE Examination
    SET chiefComplaint = 'Limping',
        description = 'Injury to front left leg, mild swelling',
        actionsTaken = 'Applied 2 bandages'
    WHERE examNo = 2;
""")

cursor.execute("SELECT * FROM Examination WHERE examNo = 2;")
print(cursor.fetchall())

# Transaction 4: Retrieve a list of all Pets owned by a specific owner
print("\n# Transaction 4: Retrieve a list of all Pets owned by a specific owner ")

# Constraint check: Check if ownerNo exists
cursor.execute("SELECT * FROM Owner WHERE ownerNo = 6;")
owner = cursor.fetchone()
if not owner:
    raise ValueError("Owner with ownerNo = 6 does not exist.")
print("Constraint check 1: Owner 6 exists" )

# Retrieve pets owned by a specific owner
cursor.execute("""
    SELECT petName, petDOB, petBreed, petColor, clinicNo
    FROM Pet
    WHERE ownerNo = 6;
""")
print(cursor.fetchall())

# Transaction 5: Assign a Manager to the Clinic
# Transaction 5: Assign a Manager to the Clinic
print("\n# Transaction 5: Assign a Manager to the Clinic")

# Define variables
clinic_no = 2  
staff_no = 6   

# Constraint check: Ensure the staff member is not already managing another clinic
cursor.execute("SELECT clinicNo FROM Clinic WHERE managerStaffNo = ?;", (staff_no,))
existing_clinic = cursor.fetchone()
if existing_clinic:
    raise ValueError(f"Constraint check failed: Staff member {staff_no} is already managing Clinic {existing_clinic[0]}.")
print(f"Constraint check 1: Staff member {staff_no} is not managing another clinic")

# Update the clinic table to assign the manager
cursor.execute("""
    UPDATE Clinic
    SET managerStaffNo = ?
    WHERE clinicNo = ?;
""", (staff_no, clinic_no))
# Constraint check 2
cursor.execute("SELECT * FROM Staff WHERE staffNo = ?;", (staff_no,))
staff = cursor.fetchone()
if not staff:
    raise ValueError(f"Constraint check failed: Staff member {staff_no} does not exist in the Staff table.")
print(f"Constraint check 2: Staff member {staff_no} exists in the Staff table")

# Update the staff's position to 'Manager'
cursor.execute("""
    UPDATE Staff
    SET position = 'Manager'
    WHERE staffNo = ?;
""", (staff_no,))


# Verify the updated clinic
cursor.execute("SELECT * FROM Clinic WHERE clinicNo = ?;", (clinic_no,))
print("Updated Clinic Details:", cursor.fetchone())


print("### All SQL Queries done")
printAllTables(cursor)