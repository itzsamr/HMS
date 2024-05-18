INSERT INTO Doctor (firstName, lastName, specialization, contactNumber) VALUES
('John', 'Doe', 'Cardiology', '123-456-7890'),
('Jane', 'Smith', 'Neurology', '234-567-8901'),
('Emily', 'Johnson', 'Pediatrics', '345-678-9012'),
('Michael', 'Williams', 'Dermatology', '456-789-0123'),
('Sarah', 'Brown', 'Orthopedics', '567-890-1234');

INSERT INTO Patient (firstName, lastName, dateOfBirth, gender, contactNumber, address) VALUES
('Alice', 'Davis', '1985-06-15', 'Female', '678-901-2345', '123 Main St, Springfield'),
('Bob', 'Miller', '1990-07-20', 'Male', '789-012-3456', '456 Elm St, Springfield'),
('Charlie', 'Wilson', '2000-08-25', 'Male', '890-123-4567', '789 Pine St, Springfield'),
('Diana', 'Moore', '1975-09-30', 'Female', '901-234-5678', '101 Maple St, Springfield'),
('Ethan', 'Taylor', '1982-10-10', 'Male', '012-345-6789', '202 Oak St, Springfield');

INSERT INTO Appointments (patient_Id, doctor_Id, appointment_date, description) VALUES
(1, 1, '2024-06-01', 'Routine check-up'),
(2, 2, '2024-06-02', 'Neurological examination'),
(3, 3, '2024-06-03', 'Pediatric consultation'),
(4, 4, '2024-06-04', 'Skin rash treatment'),
(5, 5, '2024-06-05', 'Knee pain consultation');
