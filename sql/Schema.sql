create database hospital;

use hospital;

CREATE TABLE Doctor (
    doctor_Id INT IDENTITY(1,1) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    specialization VARCHAR(50) NOT NULL,
    contactNumber VARCHAR(15) NOT NULL
);

CREATE TABLE Patient (
    patient_Id INT IDENTITY(1,1) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contactNumber VARCHAR(15) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Appointments (
    appointmentId INT IDENTITY(1,1) PRIMARY KEY,
    patient_Id INT NOT NULL,
    doctor_Id INT NOT NULL,
    appointment_date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (patient_Id) REFERENCES Patient(patient_Id),
    FOREIGN KEY (doctor_Id) REFERENCES Doctor(doctor_Id)
);




