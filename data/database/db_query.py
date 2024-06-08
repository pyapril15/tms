from data.database.db import Database

create_staff_table = ("CREATE TABLE IF NOT EXISTS staff (id INT PRIMARY KEY AUTO_INCREMENT,"
                      "username VARCHAR(30) UNIQUE NOT NULL,"
                      "fullname VARCHAR(30) NOT NULL,"
                      "mobile_no VARCHAR(15) NOT NULL);")

create_auth_table = ("CREATE TABLE IF NOT EXISTS auth (id INT PRIMARY KEY AUTO_INCREMENT,"
                     "username VARCHAR(30) NOT NULL,"
                     "salt VARCHAR(50) NOT NULL,"
                     "hashed_password VARCHAR(100) NOT NULL,"
                     "type BOOLEAN NOT NULL DEFAULT 0,"
                     "FOREIGN KEY (username) REFERENCES staff(username) ON DELETE CASCADE ON UPDATE CASCADE);")

create_university_table = ("CREATE TABLE IF NOT EXISTS university (university_id INT PRIMARY KEY AUTO_INCREMENT,"
                           "university_name VARCHAR(50) UNIQUE NOT NULL,"
                           "university_code INT UNIQUE NOT NULL,"
                           "university_short_name VARCHAR(15) UNIQUE NOT NULL);")

create_course_table = ("CREATE TABLE IF NOT EXISTS course (course_id INT PRIMARY KEY AUTO_INCREMENT,"
                       "course_name VARCHAR(50) UNIQUE NOT NULL,"
                       "course_code INT UNIQUE NOT NULL,"
                       "course_short_name VARCHAR(15) UNIQUE NOT NULL,"
                       "year INT NOT NULL);")

create_subject_table = ("CREATE TABLE IF NOT EXISTS subject (subject_id INT PRIMARY KEY AUTO_INCREMENT,"
                        "subject_name VARCHAR(50) UNIQUE NOT NULL,"
                        "subject_code INT(5) UNIQUE NOT NULL);")

create_transport_fee_table = (
    "CREATE TABLE IF NOT EXISTS transport_fee (transport_fee_id INT PRIMARY KEY AUTO_INCREMENT,"
    "center_code VARCHAR(15) UNIQUE NOT NULL,"
    "center_name VARCHAR(50) UNIQUE NOT NULL,"
    "fee INT NOT NULL);")

create_exam_detail_table = ("CREATE TABLE IF NOT EXISTS exam_detail (exam_detail_id INT PRIMARY KEY AUTO_INCREMENT,"
                            "university_short_name VARCHAR(15) NOT NULL,"
                            "course_short_name VARCHAR(15) NOT NULL,"
                            "semester INT NOT NULL, center_name VARCHAR(50) NOT NULL,"
                            "shift VARCHAR(20) NOT NULL,"
                            "is_active TINYINT(1) DEFAULT 0,"
                            "CONSTRAINT exam_detail_unique UNIQUE (university_short_name, course_short_name, semester),"
                            "FOREIGN KEY (university_short_name) REFERENCES university(university_short_name) ON DELETE CASCADE ON UPDATE CASCADE,"
                            "FOREIGN KEY (course_short_name) REFERENCES course(course_short_name) ON DELETE CASCADE ON UPDATE CASCADE);")

create_allotment_table = ("CREATE TABLE IF NOT EXISTS allotment (allotment_id INT PRIMARY KEY AUTO_INCREMENT,"
                          "university_short_name VARCHAR(15) NOT NULL, course_short_name VARCHAR(15) NOT NULL,"
                          "semester INT NOT NULL, subject_code INT(5) NOT NULL, subject_name VARCHAR(15) NOT NULL,"
                          "exam_date DATE DEFAULT NULL, journey_id INT DEFAULT NULL,"
                          "CONSTRAINT all_field UNIQUE (university_short_name, course_short_name, subject_name),"
                          "FOREIGN KEY (university_short_name) REFERENCES university(university_short_name) ON DELETE CASCADE ON UPDATE CASCADE,"
                          "FOREIGN KEY (course_short_name) REFERENCES course(course_short_name) ON DELETE CASCADE ON UPDATE CASCADE,"
                          "FOREIGN KEY (subject_code) REFERENCES subject(subject_code) ON DELETE CASCADE ON UPDATE CASCADE,"
                          "FOREIGN KEY (subject_name) REFERENCES subject(subject_name) ON DELETE CASCADE ON UPDATE CASCADE,"
                          "FOREIGN KEY (journey_id) REFERENCES journey_detail(journey_id) ON DELETE SET NULL);")

create_journey_detail_table = ("CREATE TABLE IF NOT EXISTS journey_detail (journey_id INT PRIMARY KEY AUTO_INCREMENT,"
                               "_to VARCHAR(50) NOT NULL, date DATE NOT NULL, time VARCHAR(15), no_of_passenger INT DEFAULT 0,"
                               "type VARCHAR(15) NOT NULL,"
                               "CONSTRAINT journey_unique UNIQUE (_to, date, time),"
                               "FOREIGN KEY (_to) REFERENCES transport_fee(center_name));")

create_student_table = (
    "CREATE TABLE IF NOT EXISTS student (roll_no VARCHAR(30) PRIMARY KEY, student_name VARCHAR(40) NOT NULL,"
    "guardian_name VARCHAR(40) NOT NULL, mobile_no VARCHAR(15) NOT NULL,"
    "university_short_name VARCHAR(30) NOT NULL, course_short_name VARCHAR(30) NOT NULL, semester INT NOT NULL,"
    "FOREIGN KEY (university_short_name) REFERENCES university(university_short_name) ON DELETE CASCADE ON UPDATE CASCADE,"
    "FOREIGN KEY (course_short_name) REFERENCES course(course_short_name) ON DELETE CASCADE ON UPDATE CASCADE);")

create_transport_fee_detail_table = (
    "CREATE TABLE IF NOT EXISTS transport_fee_detail (receipt_no INT PRIMARY KEY AUTO_INCREMENT,"
    "roll_no VARCHAR(30) NOT NULL, amount INT NOT NULL, date_and_time DATETIME DEFAULT CURRENT_TIMESTAMP,"
    "mode VARCHAR(15) NOT NULL,"
    "FOREIGN KEY (roll_no) REFERENCES student(roll_no) ON DELETE CASCADE ON UPDATE CASCADE);")

create_fee_journey = ("CREATE TABLE IF NOT EXISTS fee_journey (combine_id INT PRIMARY KEY AUTO_INCREMENT,"
                      "receipt_no INT, roll_no VARCHAR(30) NOT NULL, journey_id INT,"
                      "FOREIGN KEY (receipt_no) REFERENCES transport_fee_detail(receipt_no) ON DELETE CASCADE,"
                      "FOREIGN KEY (roll_no) REFERENCES student(roll_no) ON DELETE CASCADE ON UPDATE CASCADE,"
                      "FOREIGN KEY (journey_id) REFERENCES journey_detail(journey_id) ON DELETE CASCADE);")

# trigger
query_create_trigger_exam_detail_is_active = """
                CREATE TRIGGER IF NOT EXISTS update_is_active_on_exam_date_change
                AFTER UPDATE ON allotment
                FOR EACH ROW
                BEGIN
                    UPDATE exam_detail AS ed
                    SET ed.is_active = IF((SELECT COUNT(*) FROM allotment WHERE university_short_name = ed.university_short_name AND course_short_name = ed.course_short_name AND semester = ed.semester AND exam_date IS NOT NULL) > 0, 1, 0)
                    WHERE ed.university_short_name = NEW.university_short_name
                        AND ed.course_short_name = NEW.course_short_name
                        AND ed.semester = NEW.semester;
                END
            """

query_create_trigger_after_exam_date_null = """
CREATE TRIGGER IF NOT EXISTS after_exam_date_null
AFTER UPDATE ON allotment
FOR EACH ROW
BEGIN
    IF NEW.exam_date IS NULL AND OLD.exam_date IS NOT NULL THEN
        DELETE FROM journey_detail WHERE journey_id = OLD.journey_id;
    END IF;
END
"""

query_create_trigger_after_insertion_fee_journey = """
CREATE TRIGGER IF NOT EXISTS increment_passenger_count
AFTER INSERT ON fee_journey
FOR EACH ROW
BEGIN
    UPDATE journey_detail
    SET no_of_passenger = no_of_passenger + 1
    WHERE journey_id = NEW.journey_id;
END;
"""

query_create_trigger_after_deletion_fee_journey = """
CREATE TRIGGER IF NOT EXISTS decrement_passenger_count
AFTER DELETE ON fee_journey
FOR EACH ROW
BEGIN
    UPDATE journey_detail
    SET no_of_passenger = CASE
                                WHEN (no_of_passenger - 1) >= 0 THEN no_of_passenger - 1
                                ELSE 0
                           END
    WHERE journey_id = OLD.journey_id;
END;
"""

query_create_trigger_after_deletion_transport_fee_detail = """
CREATE TRIGGER decrement_passenger_count_on_transport_fee_detail_delete
AFTER DELETE ON transport_fee_detail
FOR EACH ROW
BEGIN
    UPDATE journey_detail 
    SET no_of_passenger = GREATEST(0, no_of_passenger - 1) 
    WHERE journey_id = (SELECT journey_id FROM fee_journey WHERE receipt_no = OLD.receipt_no);
END;
"""

# sql query only
query_get_auth_type = "SELECT type FROM auth WHERE type='1';"
query_insert_staff = "INSERT INTO staff (username, fullname, mobile_no) VALUES (%s, %s, %s)"
query_insert_auth = "INSERT INTO auth (username, salt, hashed_password, type) VALUES (%s, %s, %s, %s)"
query_get_auth_detail = "SELECT salt, hashed_password, type FROM auth WHERE username='{}'"
query_alter_fee_detail_auto_increment = "ALTER TABLE fee_detail AUTO_INCREMENT=1000"

query_get_university_detail = "SELECT university_code, university_short_name, university_name FROM university;"
query_get_university_short_name = "SELECT university_short_name FROM university;"
query_insert_university_detail = "INSERT INTO university (university_name, university_code, university_short_name) VALUES (%s,%s,%s)"
query_update_university_detail = "UPDATE university SET university_name=%s, university_code=%s, university_short_name=%s WHERE university_code=%s"
query_delete_university_detail = "DELETE FROM university WHERE university_code='{}'"

query_get_course_detail = "SELECT course_code, course_short_name, course_name, year FROM course"
query_get_course_short_name = "SELECT course_short_name FROM course;"
query_get_course_year = "SELECT year FROM course WHERE course_short_name='{}';"
query_insert_course_detail = "INSERT INTO course (course_name, course_code, course_short_name, year) VALUES (%s, %s, %s, %s)"
query_update_course_detail = "UPDATE course SET course_name=%s, course_code=%s, course_short_name=%s, year=%s WHERE course_code = %s"
query_delete_course_detail = "DELETE FROM course WHERE course_code='{}'"

query_get_subject_detail = "SELECT subject_code, subject_name FROM subject"
query_get_subject_name_from_subject = "SELECT subject_name FROM subject;"
query_get_subject_code_of_subject_name_from_subject = "SELECT subject_code FROM subject WHERE subject_name='{}'"
query_insert_subject_detail = "INSERT INTO subject (subject_name, subject_code) VALUES (%s, %s)"
query_update_subject_detail = "UPDATE subject SET subject_name = %s, subject_code = %s WHERE subject_code = %s"
query_delete_subject_detail = "DELETE FROM subject WHERE subject_code='{}'"

query_get_transport_fee_detail = "SELECT center_code, center_name, fee FROM transport_fee;"
query_get_transport_fee = "SELECT fee FROM transport_fee WHERE center_name='{}'"
query_get_center_name_from_transport_fee = "SELECT center_name FROM transport_fee;"
query_insert_transport_fee = "INSERT INTO transport_fee (center_code, center_name, fee) VALUES (%s, %s, %s)"
query_update_transport_fee = "UPDATE transport_fee SET center_code=%s, center_name=%s, fee=%s WHERE center_code=%s"
query_delete_transport_fee = "DELETE FROM transport_fee WHERE center_code='{}'"

query_get_j_id_subject_code_subject_name_exam_date = "SELECT journey_id, subject_code, subject_name, exam_date FROM allotment WHERE university_short_name=%s AND course_short_name=%s AND semester=%s"
query_get_subject_name_exam_date = "SELECT subject_name, exam_date FROM allotment WHERE university_short_name=%s AND course_short_name=%s AND semester=%s"
query_get_subject_exam_date = "SELECT exam_date FROM allotment WHERE university_short_name=%s AND course_short_name=%s AND semester=%s AND exam_date is not NULL"
query_insert_detail_into_allotment_table = "INSERT INTO allotment (university_short_name, course_short_name, semester, subject_code, subject_name) VALUES (%s, %s, %s, %s, %s)"
query_update_detail_of_allotment_tabel = "UPDATE allotment SET subject_code=%s, subject_name = %s WHERE university_short_name = %s AND course_short_name = %s AND subject_name = %s"
query_update_exam_date = "UPDATE allotment SET exam_date = %s WHERE university_short_name = %s AND course_short_name = %s AND semester = %s AND subject_name = %s"
query_update_journey_id = "UPDATE allotment SET journey_id = %s WHERE university_short_name = %s AND course_short_name = %s AND semester = %s AND subject_name = %s"
query_update_journey_id_where_date = "UPDATE allotment SET journey_id = NULL WHERE university_short_name = %s AND course_short_name = %s AND semester = %s AND subject_name = %s"
query_delete_detail_of_allotment_table = "DELETE FROM allotment WHERE university_short_name=%s AND course_short_name=%s AND semester=%s AND subject_code=%s"
query_delete_exam_date = "UPDATE allotment SET exam_date=NULL WHERE university_short_name = %s AND course_short_name = %s AND semester = %s"

query_get_exam_detail = "SELECT university_short_name, course_short_name, semester, center_name, shift, is_active FROM exam_detail WHERE university_short_name=%s AND course_short_name=%s AND semester=%s;"
query_center_name_shift_is_active_from_exam_detail = "SELECT center_name, shift, is_active FROM exam_detail WHERE university_short_name=%s AND course_short_name=%s AND semester=%s"
query_center_name_shift_from_exam_detail = "SELECT center_name, shift FROM exam_detail WHERE university_short_name=%s AND course_short_name=%s AND semester=%s"
query_exam_center_from_exam_detail = "SELECT center_name FROM exam_detail WHERE university_short_name=%s AND course_short_name=%s AND semester=%s"
query_is_active_from_exam_detail = "SELECT is_active FROM exam_detail WHERE university_short_name=%s AND course_short_name=%s AND semester=%s"
query_insert_detail_into_exam_detail = "INSERT INTO exam_detail (university_short_name, course_short_name, semester, center_name, shift) VALUES (%s, %s, %s, %s, %s)"
query_update_detail_of_exam_detail = "UPDATE exam_detail SET center_name = %s, shift = %s WHERE university_short_name = %s AND course_short_name = %s AND semester = %s"
query_update_exam_is_active_detail = "UPDATE exam_detail SET is_active = %s WHERE university_short_name = %s AND course_short_name = %s AND semester = %s"

query_get_journey_detail = "SELECT * FROM journey_detail"
query_get_journey_id_detail = "SELECT journey_id FROM journey_detail WHERE _to=%s AND date=%s AND time=%s"
query_get_journey_type_detail = "SELECT type FROM journey_detail WHERE journey_id='{}'"
query_get_journey_detail_j_id = "SELECT _to, date, time FROM journey_detail WHERE journey_id='{}'"
query_insert_journey_detail = "INSERT INTO journey_detail (_to, date, time, type) VALUES (%s, %s, %s, %s)"
query_update_exam_journey_detail = "UPDATE journey_detail SET _to=%s, time=%s WHERE _to=%s AND date=%s AND time=%s AND type='exam'"
query_update_exam_date_journey_detail = "UPDATE journey_detail SET date=%s WHERE _to=%s AND date=%s AND time=%s AND type='exam'"
query_update_journey_detail = "UPDATE journey_detail SET _to=%s, date=%s, time=%s WHERE journey_id=%s"
query_delete_journey_detail = "DELETE FROM journey_detail WHERE _to=%s AND date=%s AND time=%s"
query_delete_journey_detail_j_id = "DELETE FROM journey_detail WHERE journey_id='{}'"

query_get_student_detail = "SELECT * FROM student"
query_get_similar_roll_no = "SELECT roll_no FROM student WHERE roll_no LIKE %s LIMIT 5"
query_get_student_detail_of_roll_no = "SELECT * FROM student WHERE roll_no LIKE {}"
query_get_student_ucs_of_roll_no = "SELECT university_short_name, course_short_name, semester FROM student WHERE roll_no = '{}'"
query_insert_student_detail = "INSERT INTO student (roll_no, student_name, guardian_name, mobile_no, university_short_name, course_short_name, semester) VALUES (%s, %s, %s, %s, %s, %s, %s)"
query_update_student_detail = "UPDATE student SET roll_no=%s, student_name=%s, guardian_name=%s, mobile_no=%s, university_short_name=%s, course_short_name=%s, semester=%s WHERE roll_no=%s"
query_delete_student_detail = "DELETE FROM student WHERE roll_no='{}'"

query_insert_transport_fee_detail = "INSERT INTO transport_fee_detail (roll_no, amount, mode) VALUES (%s, %s, %s)"
query_get_receipt_detail = "SELECT * FROM transport_fee_detail"
query_get_last_insert_receipt_no = "SELECT receipt_no, roll_no FROM transport_fee_detail ORDER BY receipt_no DESC LIMIT 1"
query_get_receipt_no = "SELECT receipt_no FROM transport_fee_detail"
query_get_receipt_roll_no = "SELECT roll_no FROM transport_fee_detail"
query_delete_fee_detail = "DELETE FROM transport_fee_detail WHERE receipt_no='{}'"

query_insert_fee_journey = "INSERT INTO fee_journey (receipt_no, roll_no, journey_id) VALUES (%s, %s, %s)"
query_get_fee_journey_id = "SELECT journey_id FROM fee_journey WHERE receipt_no=%s AND roll_no=%s"
query_get_fee_journey_id_roll_no = "SELECT journey_id FROM fee_journey WHERE roll_no='{}'"
query_get_fee_receipt_roll_no = "SELECT DISTINCT receipt_no FROM fee_journey WHERE roll_no='{}'"
query_delete_fee_receipt_receipt_no = "DELETE FROM fee_journey WHERE receipt_no='{}'"

query_get_amount_mode = """
SELECT DISTINCT t.amount, t.mode
FROM transport_fee_detail AS t
JOIN fee_journey AS fj ON t.receipt_no = fj.receipt_no
WHERE fj.roll_no = '{}'
"""


class Query:
    def __init__(self, table_name=None):
        self._table_name = table_name
        self.db = Database("localhost", "root", "pyapril15", "college")

    def check_is_connected(self):
        """
        Checks if the database connection is established and active.
        """
        with self.db as db_connection:
            return db_connection.is_connected()

    def create_all_table(self):
        try:
            with self.db as db_connection:
                db_connection.execute_query(create_staff_table)
                db_connection.execute_query(create_auth_table)
                db_connection.execute_query(create_university_table)
                db_connection.execute_query(create_course_table)
                db_connection.execute_query(create_subject_table)
                db_connection.execute_query(create_transport_fee_table)
                db_connection.execute_query(create_exam_detail_table)
                db_connection.execute_query(create_journey_detail_table)
                db_connection.execute_query(create_allotment_table)
                db_connection.execute_query(create_student_table)
                db_connection.execute_query(create_transport_fee_detail_table)
                db_connection.execute_query(create_fee_journey)
                db_connection.execute_query(query_create_trigger_exam_detail_is_active)
                db_connection.execute_query(query_create_trigger_after_exam_date_null)
                db_connection.execute_query(query_create_trigger_after_insertion_fee_journey)
                db_connection.execute_query(query_create_trigger_after_deletion_fee_journey)
                db_connection.execute_query(query_create_trigger_after_deletion_transport_fee_detail)
                return True
        except Exception as e:
            return False

    def show_table_status(self):
        with self.db as db_connection:
            query = f"SHOW TABLE STATUS LIKE '{self._table_name}'"
            success = db_connection.fetchone_query(query)
        if success:
            return success
        else:
            return False

    def alter_table_auto_increment(self):
        status = self.show_table_status()
        with self.db as db_connection:
            if status[10] == 1:
                success = db_connection.execute_query(query_alter_fee_detail_auto_increment)
                if success:
                    return True
                else:
                    return False
            else:
                return True

    def get_auth_type(self):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_auth_type)
        if success:
            return success
        return

    def get_auth(self, username: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_auth_detail.format(username))
        if success:
            return success
        return

    def insert_staff_and_auth(self, staff: tuple, auth: tuple):
        """Inserts staff and authentication data into the database."""
        with self.db as db_connection:
            success = db_connection.transaction_execute_query_with_value(query_insert_staff, staff, query_insert_auth,
                                                                         auth)
        if success:
            return True
        return False

    def update_exam_date_create_exam_journey(self, exam_date: list, journey: list):
        with self.db as db_connection:
            success = db_connection.transaction_execute_many_query(query_update_exam_date, exam_date,
                                                                   query_insert_journey_detail, journey)
        if success:
            return True
        return False

    def update_exam_date_update_exam_journey(self, exam_date: list, journey: list):
        with self.db as db_connection:
            success = db_connection.transaction_execute_many_query(query_update_exam_date, exam_date,
                                                                   query_update_exam_date_journey_detail, journey)
        if success:
            return True
        return False

    def delete_fee_journey_and_fee_detail(self, receipt_no: str):
        with self.db as db_connection:
            success = db_connection.transaction_execute_query(query_delete_fee_receipt_receipt_no.format(receipt_no),
                                                              query_delete_fee_detail.format(receipt_no))
        if success:
            return True
        return False

    # ---------------------------University database function-----------------------------------------------------------
    def get_university_detail(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_university_detail)
        if success:
            return success
        return

    def get_university_short_name(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_university_short_name)
        if success:
            return success
        return

    def insert_university_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_university_detail, value)
        if success:
            return True
        else:
            return False

    def update_university_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_university_detail, value)
        if success:
            return True
        else:
            return False

    def delete_university_detail(self, university_code: str):
        with self.db as db_connection:
            success = db_connection.execute_query(query_delete_university_detail.format(university_code))
        if success:
            return True
        else:
            return False

    # -------------------------End University database function---------------------------------------------------------

    # ---------------------------Course database function---------------------------------------------------
    def get_course_detail(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_course_detail)
        if success:
            return success
        return

    def get_course_short_name(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_course_short_name)
        if success:
            return success
        return

    def get_course_year(self, course_short_name: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_course_year.format(course_short_name))
        if success:
            return success
        return

    def insert_course_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_course_detail, value)
        if success:
            return True
        else:
            return False

    def update_course_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_course_detail, value)
        if success:
            return True
        else:
            return False

    def delete_course_detail(self, course_code: str):
        with self.db as db_connection:
            success = db_connection.execute_query(query_delete_course_detail.format(course_code))
        if success:
            return True
        return False

    # -------------------------End Course database function-----------------------------------------------

    # ---------------------------Subject database function-----------------------------------------------------------
    def get_subject_detail(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_subject_detail)
        if success:
            return success
        else:
            return

    def get_subject_name_from_subject(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_subject_name_from_subject)
        if success:
            return success
        return

    def get_subject_code_of_subject_name_from_subject(self, subject_name: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(
                query_get_subject_code_of_subject_name_from_subject.format(subject_name))
        if success:
            return success
        return

    def insert_subject_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_subject_detail, value)
        if success:
            return True
        else:
            return False

    def update_subject_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_subject_detail, value)
        if success:
            return True
        else:
            return False

    def delete_subject_detail(self, subject_code: str):
        with self.db as db_connection:
            success = db_connection.execute_query(query_delete_subject_detail.format(subject_code))
        if success:
            return True
        else:
            return False

    # -------------------------End subject database function---------------------------------------------------------

    # --------------------------Transport Fee/Place database function------------------------------------------------
    def get_transport_place_fee_detail(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_transport_fee_detail)
        if success:
            return success
        return

    def get_transport_fee(self, center_name: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_transport_fee.format(center_name))
        if success:
            return success
        return

    def get_center_name_from_transport_fee(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_center_name_from_transport_fee)
        if success:
            return success
        return

    def insert_transport_place_fee_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_transport_fee, value)
        if success:
            return True
        return False

    def update_transport_place_fee_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_transport_fee, value)
        if success:
            return True
        return False

    def delete_transport_place_fee_detail(self, center_code: str):
        with self.db as db_connection:
            success = db_connection.execute_query(query_delete_transport_fee.format(center_code))
        if success:
            return True
        return False

    # --------------------------End Transport Fee/Place database function-----------------------------------------------

    # ---------------------------Allotment database function------------------------------------------------------------
    # 1. Subject
    def get_usn_csn_sem_sc_sn(self, query: str):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query)
        if success:
            return success
        return

    def get_j_id_subject_code_subject_name_exam_date(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchall_query_with_value(query_get_j_id_subject_code_subject_name_exam_date, value)
        if success:
            return success
        return

    def get_subject_name_exam_date(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchall_query_with_value(query_get_subject_name_exam_date, value)
        if success:
            return success
        return

    def get_subject_exam_date(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchall_query_with_value(query_get_subject_exam_date, value)
        if success:
            return success
        return

    def insert_allotment_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_detail_into_allotment_table, value)
        if success:
            return True
        else:
            return False

    def update_allotment_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_detail_of_allotment_tabel, value)
        if success:
            return True
        return False

    def update_journey_id_allotment(self, value: list):
        with self.db as db_connection:
            success = db_connection.execute_manyquery_with_value(query_update_journey_id, value)
        if success:
            return True
        return False

    def update_journey_id_allotment_where_date(self, value: list):
        with self.db as db_connection:
            success = db_connection.execute_manyquery_with_value(query_update_journey_id_where_date, value)
        if success:
            return True
        return False

    def delete_allotment_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_delete_detail_of_allotment_table, value)
        if success:
            return True
        return False

    def delete_exam_date_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_delete_exam_date, value)
        if success:
            return True
        return False

    # 2. Exam detail
    def get_usn_csn_sem_cn_shift_is_active(self, query: str):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query)
        if success:
            return success
        else:
            return

    # -----------------------End Allotment database function----------------------------------------------------------

    # ------------------------Exam Detail database function----------------------------------------------------------

    def get_exam_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchone_query_with_value(query_get_exam_detail, value)
        if success:
            return success
        return

    def get_center_name_shift_is_active_from_exam_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchone_query_with_value(query_center_name_shift_is_active_from_exam_detail, value)
        if success:
            return success
        return

    def get_center_name_shift_from_exam_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchone_query_with_value(query_center_name_shift_from_exam_detail, value)
        if success:
            return success
        return

    def get_exam_center_from_exam_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchone_query_with_value(query_exam_center_from_exam_detail, value)
        if success:
            return success
        return

    def get_is_active_from_exam_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchone_query_with_value(query_is_active_from_exam_detail, value)
        if success:
            return success
        return

    def insert_exam_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_detail_into_exam_detail, value)
        if success:
            return True
        return False

    def update_exam_detail(self, exam_detail: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_detail_of_exam_detail, exam_detail)
        if success:
            return True
        return False

    def update_exam_is_active_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_exam_is_active_detail, value)
        if success:
            return True
        else:
            return False

    def update_exam_detail_and_exam_journey(self, exam_detail: tuple, exam_journey: list):
        with self.db as db_connection:
            success = db_connection.transaction_execute_with_execute_many_query(query_update_detail_of_exam_detail,
                                                                                exam_detail,
                                                                                query_update_exam_journey_detail,
                                                                                exam_journey)
        if success:
            return True
        return False

    # -----------------------End Exam Detail database function----------------------------------------------------------

    # -----------------------Journey database function----------------------------------------------------------
    def get_journey_detail(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_journey_detail)
        if success:
            return success
        return

    def get_journey_id(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.fetchone_query_with_value(query_get_journey_id_detail, value)
        if success:
            return success
        return

    def get_journey_type(self, value: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_journey_type_detail.format(value))
        if success:
            return success
        return

    def get_journey_detail_j_id(self, journey_id: int):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_journey_detail_j_id.format(journey_id))
        if success:
            return success
        return

    def insert_exam_journey_detail(self, value: list):
        with self.db as db_connection:
            success = db_connection.execute_manyquery_with_value(query_insert_journey_detail, value)
        if success:
            return True
        return False

    def insert_other_journey_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_journey_detail, value)
        if success:
            return True
        return False

    def update_journey_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_journey_detail, value)
        if success:
            return True
        return False

    def delete_journey_detail(self, value: list):
        with self.db as db_connection:
            success = db_connection.execute_manyquery_with_value(query_delete_journey_detail, value)
        if success:
            return True
        return False

    def delete_journey_detail_j_id(self, journey_id: str):
        with self.db as db_connection:
            success = db_connection.execute_query(query_delete_journey_detail_j_id.format(journey_id))
        if success:
            return True
        return False

    # -----------------------End Journey database function----------------------------------------------------------

    # -----------------------Student database function----------------------------------------------------------
    def get_student_detail(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_student_detail)
        if success:
            return success
        return

    def get_similar_roll_no(self, roll_no: tuple):
        with self.db as db_connection:
            success = db_connection.fetchall_query_with_value(query_get_similar_roll_no, roll_no)
        if success:
            return success
        return

    def get_student_detail_of_roll_no(self, roll_no: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_student_detail_of_roll_no.format(roll_no))
        if success:
            return success
        return

    def get_student_ucs_of_roll_no(self, roll_no: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_student_ucs_of_roll_no.format(roll_no))
        if success:
            return success
        return

    def insert_student_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_insert_student_detail, value)
        if success:
            return True
        else:
            return False

    def update_student_detail(self, value: tuple):
        with self.db as db_connection:
            success = db_connection.execute_query_with_value(query_update_student_detail, value)
        if success:
            return True
        else:
            return False

    def delete_student_detail(self, roll_no):
        with self.db as db_connection:
            success = db_connection.execute_query(query_delete_student_detail.format(roll_no))
        if success:
            return True
        else:
            return False

    # -----------------------End Student database function----------------------------------------------------------
    def insert_fee_detail_and_fee_journey(self, fee_detail: tuple, journey_id: list):
        with self.db as db_connection:
            success = db_connection.transaction_execute_query_with_and_without(query_insert_transport_fee_detail,
                                                                               fee_detail, query_insert_fee_journey,
                                                                               journey_id)
        if success:
            return True
        return False

    def get_receipt_detail(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_receipt_detail)
        if success:
            return success
        return

    def get_last_insert_receipt_no(self):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_last_insert_receipt_no)
        if success:
            return success
        return

    def get_receipt_no(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_receipt_no)
        if success:
            return success
        return

    def get_receipt_roll_no(self):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_receipt_roll_no)
        if success:
            return success
        return

    def get_fee_journey_id(self, fee_journey: tuple):
        with self.db as db_connection:
            success = db_connection.fetchall_query_with_value(query_get_fee_journey_id, fee_journey)
        if success:
            return success
        return

    def get_fee_journey_id_roll_no(self, roll_no: str):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_fee_journey_id_roll_no.format(roll_no))
        if success:
            return success
        return

    def get_fee_receipt_no_roll_no(self, roll_no: str):
        with self.db as db_connection:
            success = db_connection.fetchone_query(query_get_fee_receipt_roll_no.format(roll_no))
        if success:
            return success
        return

    def get_amount_mode_roll_no(self, roll_no: str):
        with self.db as db_connection:
            success = db_connection.fetchall_query(query_get_amount_mode.format(roll_no))
        if success:
            return success
        return

# ------------------------------End Database Query Function------------------------------------------------------------
