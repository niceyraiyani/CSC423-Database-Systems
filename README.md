# CSC423-Database-Systems

The **Pawsome Pets Database** is a relational database designed to manage information for a pet clinic chain. The database tracks owners, pets, staff, clinics, and medical examinations, ensuring data integrity and enabling streamlined operations.

---

## Project Details

This project was developed as part of a course on **Database Systems** : CSC423. It involves the design, development, and implementation of a relational database using SQLite and Python. The project includes conceptual and logical modeling, SQL schema creation, data insertion, and the implementation of various user transactions.

---

## Features

1. **Owners and Pets Management:**
   - Register pet owners and their pets.
   - Store information such as owner's name, address, and contact number.
   - Track pets by their unique ID, name, DOB, breed, color, and associated clinic.

2. **Clinics and Staff Management:**
   - Store clinic details, including name, address, phone number, and manager.
   - Assign staff to clinics and manage their roles and salaries.

3. **Medical Examinations:**
   - Record detailed information about each pet examination.
   - Track complaints, treatments, dates, and actions taken by staff.

4. **Data Integrity:**
   - Enforce primary and foreign key constraints.
   - Ensure normalization up to 3NF.

---

## Project Structure

The project consists of the following components:

### 1. Conceptual Data Model 
- **Entity Types:**
  - Owner, Pet, Clinic, Staff, Examination, and Breed.
- **Relationships:**
  - Owners own Pets.
  - Clinics employ Staff.
  - Pets are examined by Staff at Clinics.
- **Diagrams:**
  - ER diagrams for the conceptual and logical models are included in the reports.

### 2. Logical Data Model
- Derived relations with normalization up to **3NF**.
- Integrity constraints:
  - Primary Key Constraints
  - Foreign Key Constraints
  - Attribute Domain Constraints
  - General Constraints

### 3. Implementation
- Database schema creation using SQL.
- Data population with 5 tuples for each relation.
- Implementation of user transactions using Python:
  - Registering a new pet and owner
  - Scheduling examinations
  - Updating examination descriptions
  - Retrieving list of pets for an owner
  - Assigning a manager to a clinic
