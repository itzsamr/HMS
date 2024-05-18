from dao.HospitalService import HospitalService
from util.DBConnUtil import DBConnUtil


class HospitalServiceImpl(HospitalService):

    def get_appointment_by_id(self, appointment_id):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM Appointments WHERE appointmentId = ?"
                cursor.execute(query, (appointment_id,))
                result = cursor.fetchone()
                return result if result else None
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error fetching appointment:", e)
        finally:
            if connection:
                connection.close()

    def get_appointments_for_patient(self, patient_id):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM Appointments WHERE patient_Id = ?"
                cursor.execute(query, (patient_id,))
                result = cursor.fetchall()
                return result
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error fetching appointments for patient:", e)
        finally:
            if connection:
                connection.close()

    def get_appointments_for_doctor(self, doctor_id):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM Appointments WHERE doctor_Id = ?"
                cursor.execute(query, (doctor_id,))
                result = cursor.fetchall()
                return result
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error fetching appointments for doctor:", e)
        finally:
            if connection:
                connection.close()

    def schedule_appointment(self, appointment):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM Patient WHERE patient_Id = ?",
                    appointment.patient_id,
                )
                patient_count = cursor.fetchone()[0]
                if patient_count == 0:
                    print(
                        "Failed to schedule appointment. The provided Patient ID does not exist."
                    )
                    return
                cursor.execute(
                    "SELECT COUNT(*) FROM Doctor WHERE doctor_Id = ?",
                    appointment.doctor_id,
                )
                doctor_count = cursor.fetchone()[0]
                if doctor_count == 0:
                    print(
                        "Failed to schedule appointment. The provided Doctor ID does not exist."
                    )
                    return
                query = "INSERT INTO Appointments (patient_Id, doctor_Id, appointment_date, description) VALUES (?, ?, ?, ?)"
                values = (
                    appointment.patient_id,
                    appointment.doctor_id,
                    appointment.appointment_date,
                    appointment.description,
                )
                cursor.execute(query, values)
                connection.commit()
                print("Appointment scheduled successfully.")
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error scheduling appointment:", e)
        finally:
            if connection:
                connection.close()

    def update_appointment(self, date, new_description, appointment_id):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                query = "UPDATE Appointments SET appointment_date = ?, description = ? WHERE appointmentId = ?"
                values = (date, new_description, appointment_id)
                cursor.execute(query, values)
                connection.commit()
                print("Appointment updated successfully.")
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error updating appointment:", e)
        finally:
            if connection:
                connection.close()

    def cancel_appointment(self, appointment_id):
        try:
            connection = DBConnUtil.get_connection()
            if connection:
                cursor = connection.cursor()
                query = "DELETE FROM Appointments WHERE appointmentId = ?"
                cursor.execute(query, (appointment_id,))
                connection.commit()
                print("Appointment canceled successfully.")
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error canceling appointment:", e)
        finally:
            if connection:
                connection.close()
