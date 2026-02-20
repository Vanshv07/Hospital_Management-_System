patients = {}
doctors = {}
appointments = {}

def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    gender = input("Enter Patient Gender: ")
    disease = input("Enter Disease: ")

    patients[pid] = {
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease
    }
    print("Patient added successfully!\n")

def add_doctor():
    did = input("Enter Doctor ID: ")
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")

    doctors[did] = {
        "name": name,
        "specialization": specialization
    }
    print("Doctor added successfully!\n")

def schedule_appointment():
    aid = input("Enter Appointment ID: ")
    pid = input("Enter Patient ID: ")
    did = input("Enter Doctor ID: ")
    date = input("Enter Appointment Date (dd-mm-yyyy): ")

    if pid not in patients:
        print("Patient not found!\n")
        return
    if did not in doctors:
        print("Doctor not found!\n")
        return

    appointments[aid] = {
        "patient": patients[pid]["name"],
        "doctor": doctors[did]["name"],
        "date": date
    }
    print("Appointment scheduled successfully!\n")

def show_patients():
    if not patients:
        print("No patients found.\n")
        return
    print("\n--- Patient List ---")
    for pid, info in patients.items():
        print(f"ID: {pid}, Name: {info['name']}, Age: {info['age']}, Gender: {info['gender']}, Disease: {info['disease']}")
    print()

def show_doctors():
    if not doctors:
        print("No doctors found.\n")
        return
    print("\n--- Doctor List ---")
    for did, info in doctors.items():
        print(f"ID: {did}, Name: {info['name']}, Specialization: {info['specialization']}")
    print()


def main_menu():
    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. Show All Patients")
        print("5. Show All Doctors")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            add_doctor()
        elif choice == "3":
            schedule_appointment()
        elif choice == "4":
            show_patients()
        elif choice == "5":
            show_doctors()
        elif choice == "6":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

main_menu()

