import os.path
import os.path
import socket
import sys
import threading

import bcrypt
from PySide6.QtCore import Qt, QEvent, QTimer, QObject, Signal, Slot, QDate
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QTableWidget, QTableWidgetItem, QMessageBox, QGraphicsDropShadowEffect

from data.database.db_query import Query
from data.print_pdf import PrintPreviewDialog
from data.ui.ui_custom_title_bar import Ui_Form as CustomWindowTitleBar
from data.ui.ui_splash_screen import Ui_splashScreen as splashScreen
from data.ui.ui_three_btn_combo import Ui_Form as ThreeBtnCombo
from data.ui.ui_transport_management import Ui_MainWindow
from data.working.allotment import AllotmentDialog
from data.working.book_transport import BookTransportUI
from data.working.common import Common
from data.working.course import CourseDialog
from data.working.dateSheet import DateSheetDialog
from data.working.exam_detail import ExamDetailDialog
from data.working.journey import NewJourney
from data.working.student import StudentDialog
from data.working.subject import SubjectDialog
from data.working.transport_fee import TransportPlaceFeeDialog
from data.working.university import UniversityDialog
from data.working.user_registration import UserRegistration
from data.working.weather import Weather

read_auth_type_table = "SELECT type FROM auth WHERE type='1';"


def hash_password(password, salt):
    """Hashes a password with the provided salt using bcrypt."""
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def resource_path(relative_path: str) -> str:
    """
    Get the absolute path to a resource file located relative to the application's base path.

    Parameters:
    relative_path (str): The path to the resource file relative to the base path.

    Returns:
    str: The absolute path of the resource file.
    """
    try:
        # Attempt to get the base path using sys._MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # If sys._MEIPASS is not available (not running from a PyInstaller bundle), use the current working directory
        base_path = os.path.abspath(".")

    # Join the base path and the relative path to get the absolute path of the resource file
    absolute_path = os.path.join(base_path, relative_path)

    return absolute_path


class ThreeBtnWidget(QWidget, ThreeBtnCombo):
    currently_edited_row = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class CustomTitleBar(QWidget, CustomWindowTitleBar):
    """Custom title bar widget for PyQt application windows."""

    def __init__(self, parent=None):
        """
        Constructor for CustomTitleBar.

        Args:
            parent: Parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setupUi(self)

        self.drag_start_pos = None
        self.resize_direction = None
        self.old_pos = None
        self.old_size = None

        # Connect button signals
        self.minimizeBtn.clicked.connect(self.parent().showMinimized)
        self.minimizeBtn.installEventFilter(self)
        self.maximizeBtn.clicked.connect(self.toggle_maximized)
        self.maximizeBtn.installEventFilter(self)
        self.closeBtn.clicked.connect(self.parent().close)
        self.closeBtn.installEventFilter(self)

    def eventFilter(self, obj, event):
        """
        Filters events for buttons.

        Args:
            obj: The object that the event occurred on.
            event: The event object.

        Returns:
            bool: True if the event is filtered, otherwise False.
        """
        if event.type() == QEvent.Enter:
            if obj == self.maximizeBtn:
                if self.parent().isMaximized():
                    obj.setCursor(Qt.SplitHCursor)
                    obj.setToolTip("Restore")
                else:
                    obj.setCursor(Qt.SizeVerCursor)
                    obj.setToolTip("Maximize")
            else:
                obj.setCursor(Qt.PointingHandCursor)
                return True
        elif event.type() == QEvent.Leave:
            if obj == self.maximizeBtn:
                obj.setCursor(Qt.ArrowCursor)
                obj.setToolTip("Maximize" if not self.parent().isMaximized() else "Restore")
            else:
                obj.setCursor(Qt.ArrowCursor)
                return True
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        """
        Handles mouse press event for dragging and resizing.

        Args:
            event: The mouse press event.
        """
        if event.button() == Qt.LeftButton:
            self.drag_start_pos = event.globalPosition()
            self.old_pos = event.globalPosition()
            self.old_size = self.parent().size()
            frame_rect = self.parent().frameGeometry()

            if event.position().x() <= 5:
                self.resize_direction = Qt.LeftEdge
            elif event.position().x() >= frame_rect.width() - 5:
                self.resize_direction = Qt.RightEdge
            elif event.position().y() <= 5:
                self.resize_direction = Qt.TopEdge
            elif event.position().y() >= frame_rect.height() - 5:
                self.resize_direction = Qt.BottomEdge

    def mouseMoveEvent(self, event):
        """
        Handles mouse move event for dragging and resizing.

        Args:
            event: The mouse move event.
        """
        if event.buttons() == Qt.LeftButton:
            if self.drag_start_pos is not None:  # Check if drag_start_pos is initialized
                if self.resize_direction is not None:
                    diff = event.globalPosition() - self.old_pos
                    if self.resize_direction == Qt.LeftEdge:
                        new_width = max(self.old_size.width() - diff.x(), self.parent().minimumWidth())
                        self.parent().setGeometry(self.old_pos.x(), self.parent().y(), new_width,
                                                  self.parent().height())
                    elif self.resize_direction == Qt.RightEdge:
                        new_width = max(self.old_size.width() + diff.x(), self.parent().minimumWidth())
                        self.parent().setGeometry(self.parent().x(), self.parent().y(), new_width,
                                                  self.parent().height())
                    elif self.resize_direction == Qt.TopEdge:
                        new_height = max(self.old_size.height() - diff.y(), self.parent().minimumHeight())
                        self.parent().setGeometry(self.parent().x(), self.old_pos.y(), self.parent().width(),
                                                  new_height)
                    elif self.resize_direction == Qt.BottomEdge:
                        new_height = max(self.old_size.height() + diff.y(), self.parent().minimumHeight())
                        self.parent().setGeometry(self.parent().x(), self.parent().y(), self.parent().width(),
                                                  new_height)
                else:
                    new_pos = self.parent().pos() + (event.globalPosition() - self.drag_start_pos).toPoint()
                    self.parent().move(new_pos)
                    self.drag_start_pos = event.globalPosition()

    def mouseReleaseEvent(self, event):
        """
        Handles mouse release event for dragging and resizing.

        Args:
            event: The mouse release event.
        """
        if event.button() == Qt.LeftButton:
            self.drag_start_pos = None
            self.resize_direction = None

    def mouseDoubleClickEvent(self, event):
        """
        Handles mouse double click event.

        Args:
            event: The mouse double click event.
        """
        if event.button() == Qt.LeftButton:
            if self.parent().isMaximized():
                self.parent().showNormal()
            else:
                self.parent().showMaximized()

    def toggle_maximized(self):
        """Toggles the maximized state of the parent window."""
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()


class NetworkMonitor(QObject):
    internetConnectionChecked = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stop_event = threading.Event()

    def start_monitoring(self):
        threading.Thread(target=self.monitor_loop, daemon=True).start()

    def stop_monitoring(self):
        self.stop_event.set()

    def monitor_loop(self):
        try:
            while not self.stop_event.is_set():
                connected = self.check_connection()
                self.internetConnectionChecked.emit(connected)
                self.stop_event.wait(1)  # Adjust the wait time as needed
        except RuntimeError:  # Catch RuntimeError due to possible deletion of the object
            pass

    def check_connection(self):
        return self.is_connected_to_internet()

    @staticmethod
    def is_connected_to_internet():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("www.google.com", 80))
            return True
        except Exception as e:
            return False


class MainApp(QMainWindow, Ui_MainWindow, Weather):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowIcon(QIcon("./assets/icons/bus.png"))

        self.title_bar = CustomTitleBar(self)
        self.title_bar.window_title.setText("Transport Fee Management System")
        self.setMenuWidget(self.title_bar)

        self.internet_connected = False
        self.userType = bool
        self.networkMonitor = NetworkMonitor(parent=self)
        self.networkMonitor.internetConnectionChecked.connect(self.check_is_internet_connected)
        self.networkMonitor.start_monitoring()

        self.query = Query()
        self._welcome()
        self.last_selected_row = None
        self.login_stack_page()
        self.university_manager = self.UniversityManagement(self)
        self.course_manager = self.CourseManagement(self)
        self.subject_manager = self.SubjectManagement(self)
        self.transport_place_fee_manager = self.TransportPlaceFeeManagement(self)
        self.subject_allotment_manager = self.SubjectAllotmentManager(self)
        self.exam_allotment_manager = self.ExamManagement(self)
        self.exam_date_sheet_manager = self.DateSheetManagement(self)
        self.journey_manager = self.JourneyManagement(self)
        self.student_manager = self.StudentManagement(self)
        self.student_fee_receipt_manager = self.StudentFeeReceiptManagement(self)
        self.student_journey_manager = self.StudentJourneyManagement(self)

        # --------admin button functionality-------------------
        self.title_bar.name_icon_btn.clicked.connect(self.handle_frm)
        self.loginBtn.clicked.connect(self.login)
        self.aOSPAddUserBtn1.clicked.connect(self.add_user)
        self.aOSPAddUserBtn2.clicked.connect(self.add_user)
        self.aOSPLogoutBtn1.clicked.connect(self.logout)
        self.aOSPLogoutBtn2.clicked.connect(self.logout)
        self.aOSPSwitchToUserDashboardBtn1.clicked.connect(self.user_dashboard_page)
        self.aOSPSwitchToUserDashboardBtn2.clicked.connect(self.user_dashboard_page)
        self.uOSPLogoutBtn1.clicked.connect(self.logout)
        self.uOSPLogoutBtn2.clicked.connect(self.logout)
        self.uOSPSwitchToAdminDashboardBtn1.clicked.connect(self.admin_dashboard_page)
        self.uOSPSwitchToAdminDashboardBtn2.clicked.connect(self.admin_dashboard_page)

        self.aOSPDashboardBtn1.clicked.connect(self.admin_dashboard_page)
        self.aOSPDashboardBtn2.clicked.connect(self.admin_dashboard_page)
        self.aOSPAddUniversityDetailBtn1.clicked.connect(self.admin_university_detail_page)
        self.aOSPAddUniversityDetailBtn2.clicked.connect(self.admin_university_detail_page)
        self.aOSPAllotmentDetailBtn1.clicked.connect(self.admin_allotment_detail_page)
        self.aOSPAllotmentDetailBtn2.clicked.connect(self.admin_allotment_detail_page)
        self.aOSPViewJourneyBtn1.clicked.connect(self.admin_journey_detail_page)
        self.aOSPViewJourneyBtn2.clicked.connect(self.admin_journey_detail_page)

        self.uOSPUserDashboardBtn1.clicked.connect(self.user_dashboard_page)
        self.uOSPUserDashboardBtn2.clicked.connect(self.user_dashboard_page)
        self.uOSPMSViewStudentBtn.clicked.connect(self.user_dashboard_page)
        self.uOSPViewStudentBtn1.clicked.connect(self.user_view_student)
        self.uOSPViewStudentBtn2.clicked.connect(self.user_view_student)
        self.uOSPMSViewJourneyBtn.clicked.connect(self.user_view_journey)
        self.uOSPViewJourneyBtn1.clicked.connect(self.user_view_journey)
        self.uOSPViewJourneyBtn2.clicked.connect(self.user_view_journey)
        self.uOSPViewFeeBtn1.clicked.connect(self.user_view_fee)
        self.uOSPViewFeeBtn2.clicked.connect(self.user_view_fee)

        # ---------admin_add_university_detail functionality-----------------------
        self.aOSPISUniversityTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISUniversityTable.doubleClicked.connect(self.table_double_click)
        self.aOSPISAVUUniversityAddBtn.clicked.connect(self.university_manager.add_university)

        self.aOSPISCourseTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISCourseTable.doubleClicked.connect(self.table_double_click)
        self.aOSPISAVUCourseAddBtn.clicked.connect(self.course_manager.add_course)

        self.aOSPISSubjectTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISSubjectTable.doubleClicked.connect(self.table_double_click)
        self.aOSPISAVUSubjectAddBtn.clicked.connect(self.subject_manager.add_subject)

        self.aOSPISExamTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISExamTable.doubleClicked.connect(self.table_double_click)
        self.aOSPISAVUExamAddBtn.clicked.connect(self.transport_place_fee_manager.add_transport_place_fee)

        self.aOSPISALTUniversity.currentIndexChanged.connect(
            self.subject_allotment_manager.refresh_subject_allotment_view)
        self.aOSPISALTCourse.currentIndexChanged.connect(self.subject_allotment_manager.refresh_subject_allotment_view)
        self.aOSPISALTSemester.currentIndexChanged.connect(
            self.subject_allotment_manager.refresh_subject_allotment_view)

        self.aOSPISAllotmentLBTable.itemSelectionChanged.connect(self.exam_allotment_manager.refresh_exam_detail_view)
        self.aOSPISAllotmentLBTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISAllotmentLBTable.doubleClicked.connect(self.table_double_click)
        self.aOSPISALBFAddBtn.clicked.connect(self.subject_allotment_manager.allot_subject)

        self.aOSPISAllotmentRTTable.itemSelectionChanged.connect(self.exam_date_sheet_manager.refresh_date_sheet_view)
        self.aOSPISAllotmentRTTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISAllotmentRTTable.doubleClicked.connect(self.table_double_click)
        self.aOSPISARTFAddBtn.clicked.connect(self.exam_allotment_manager.allot_exam_detail)

        self.aOSPISAllotmentRBTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISAllotmentRBTable.doubleClicked.connect(self.table_double_click)
        self.aOSPISARBFAddBtn.clicked.connect(self.exam_date_sheet_manager.allot_exam_date)
        self.aOSPISARBFDeleteBtn.clicked.connect(self.exam_date_sheet_manager.delete_exam_date)

        self.aOSPISJViewTable.itemClicked.connect(self.table_row_single_click)
        self.aOSPISJFNewBtn.clicked.connect(self.journey_manager.create_other_journey)

        # -----------------end admin function -----------------------

        # ---------------------user/staff-----------------------------
        self.uOSPMIStudentViewTable.itemClicked.connect(self.table_row_single_click)
        self.uOSPMSAddStudentBtn.clicked.connect(self.student_manager.add_student)
        self.uOSPMISSFUniversity.currentIndexChanged.connect(self.student_manager.filter_table)
        self.uOSPMISSFCourse.currentIndexChanged.connect(self.student_manager.filter_table)
        self.uOSPMISSFSemester.currentIndexChanged.connect(self.student_manager.filter_table)
        self.uOSPMISSFClearBtn.clicked.connect(self.student_manager.clear_filter)
        self.uOSPMISSFPrintBtn.clicked.connect(self.student_manager.print_table)

        self.uOSPMSBookTransportBtn.clicked.connect(self.book_transport)

        self.uOSPMISJFUniversity.currentIndexChanged.connect(self.student_journey_manager.filter_table)
        self.uOSPMISJFCourse.currentIndexChanged.connect(self.student_journey_manager.filter_table)
        self.uOSPMISJFSemester.currentIndexChanged.connect(self.student_journey_manager.filter_table)

        self.uOSPMISJFDate.setDate(QDate.currentDate())
        self.uOSPMISJFDate.dateChanged.connect(self.student_journey_manager.filter_table)
        self.uOSPMISJFClear.clicked.connect(self.student_journey_manager.clear_filter)
        self.uOSPMISJFPrintBtn.clicked.connect(self.student_journey_manager.print_table)

    def show_message_in_statusbar(self, message: str, error: str):
        self.statusbar.showMessage("Message:- " + str(message) + "Error:- " + str(error), 5000)

    @Slot(bool)
    def check_is_internet_connected(self, is_connected: bool):
        if is_connected:
            self.statusbar.showMessage("Internet connected", 5000)
        else:
            self.statusbar.showMessage("No internet connection", 5000)
        self.internet_connected = is_connected

    def closeEvent(self, event):
        self.networkMonitor.stop_monitoring()
        event.accept()

    def _welcome(self):
        auth_type = self.query.get_auth_type()

        # self.query.trigger_exam_detail_is_active()

        if auth_type is None:
            dialog = UserRegistration(self, user_type="admin")
            dialog.ui()
            dialog.exec()

        self.set_weather_report()

    def auth_login(self, username: str, password: str):
        try:
            auth = self.query.get_auth(username)
            if auth:
                hashed_password = hash_password(password, auth[0].encode())
                if hashed_password.decode() == auth[1]:
                    if int(auth[2]):
                        self.userType = True
                    else:
                        self.userType = False
                    # self.userType = auth[2]
                    return True
                else:
                    Common.show_message("Incorrect Authentication.", "C")
            else:
                Common.show_message("Register yourself!.", "C")
        except Exception as e:
            self.show_message_in_statusbar("Login unsuccessful", str(e))

    def login(self):
        username = self.loginUsername.text()
        password = self.loginPassword.text()

        try:
            if username != '':
                if password != '':
                    output = self.auth_login(username, password)
                    if output:
                        Common.show_message("Login Successful!.", "I")
                        # if self.userType is not None:
                        if self.userType is True:
                            self.admin_dashboard_page()
                        if self.userType is False:
                            self.user_dashboard_page()
                else:
                    Common.show_message("Password is empty!.")
            else:
                Common.show_message("Username is empty!.")
        except Exception as e:
            self.show_message_in_statusbar("Login unsuccessful", str(e))

    def logout(self):
        self.loginPassword.clear()
        self.login_stack_page()

    def add_user(self):
        dialog = UserRegistration(self)
        dialog.ui()
        dialog.exec()

    def set_weather_report(self):
        try:
            weather_data = self.get_weather_information()
            if weather_data is None:
                return

            weather_description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]

            data = f"Current weather in <strong>Varanasi</strong>:-\nWeather:- {weather_description}\nTemperature:- {temperature:.2f}°C (Feels like:- {feels_like:.2f}°C)\nHumidity:- {humidity}%"

            self.aOSPISWeatherInfo.setText(data)
            self.weatherInfo.setText(data)
        except Exception as e:
            self.show_message_in_statusbar("Weather", str(e))

    # -------------------stackedWidget----------------------------
    def handle_frm(self, checked):
        if checked:
            self.aOSPNameOnlyFrm.setVisible(True)
            self.aOSPIconsOnlyFrm.setVisible(False)
            self.uOSPNameOnlyFrm.setVisible(True)
            self.uOSPIconsOnlyFrm.setVisible(False)
        else:
            self.aOSPNameOnlyFrm.setVisible(False)
            self.aOSPIconsOnlyFrm.setVisible(True)
            self.uOSPNameOnlyFrm.setVisible(False)
            self.uOSPIconsOnlyFrm.setVisible(True)

    def login_stack_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.uOSPLogoutBtn1.setChecked(False)
        self.uOSPLogoutBtn2.setChecked(False)

    def admin_outer_stack_page(self):
        self.stackedWidget.setCurrentIndex(1)
        if not self.title_bar.name_icon_btn.isChecked():
            self.title_bar.name_icon_btn.click()

    def user_outer_stack_page(self):
        self.stackedWidget.setCurrentIndex(2)
        if not self.title_bar.name_icon_btn.isChecked():
            self.title_bar.name_icon_btn.click()

    # -------------------end stackedWidget----------------------------

    # ------------------admin Inner stacked Widget-----------------------
    def admin_dashboard_page(self):
        if self.userType is True:
            self.admin_outer_stack_page()
            self.aOSPInnerStackedWidget.setCurrentIndex(0)
            self.aOSPDashboardBtn2.setChecked(True)

    def admin_university_detail_page(self):
        if self.userType is True:
            self.admin_outer_stack_page()
            self.aOSPInnerStackedWidget.setCurrentIndex(1)
            self.university_manager.refresh_university_view()
            self.course_manager.refresh_course_view()
            self.subject_manager.refresh_subject_view()
            self.transport_place_fee_manager.refresh_transport_place_fee_view()

    def admin_allotment_detail_page(self):
        if self.userType is True:
            self.aOSPISALTUniversity.clear()
            self.aOSPISALTUniversity.addItem("Select University")
            self.aOSPISALTCourse.clear()
            self.aOSPISALTCourse.addItem("Select Course")
            self.aOSPISALTSemester.clear()
            self.aOSPISALTSemester.addItem("Select Semester")

            for i in range(1, 11):
                self.aOSPISALTSemester.addItem(f"{i}")

            self.admin_outer_stack_page()
            self.aOSPInnerStackedWidget.setCurrentIndex(2)
            self.subject_allotment_manager.populate_combo_boxes()

            if not self.aOSPISAllotmentLeftFrm.isVisible():
                self.aOSPISAllotmentLeftFrm.show()

            if not self.aOSPISAllotmentRightFrm.isVisible():
                self.aOSPISAllotmentRightFrm.show()

            if not self.aOSPISAllotmentLTopFrm.isVisible():
                self.aOSPISAllotmentLTopFrm.show()

            if not self.aOSPISAllotmentRTopFrm.isVisible():
                self.aOSPISAllotmentRTopFrm.show()

            if not self.aOSPISAllotmentRBottomFrm.isVisible():
                self.aOSPISAllotmentRBottomFrm.show()

    def admin_journey_detail_page(self):
        if self.userType is True:
            self.admin_outer_stack_page()
            self.aOSPInnerStackedWidget.setCurrentIndex(3)
            self.journey_manager.refresh_journey_view()

    # ------------------admin Inner stacked Widget-----------------------

    def user_dashboard_page(self):
        self.user_outer_stack_page()
        self.user_view_student()

        if not self.uOSPUserDashboardBtn2.isChecked():
            self.uOSPUserDashboardBtn2.click()

        if self.userType is True:
            if not self.uOSPSwitchToAdminDashboardBtn1.isVisible():
                self.uOSPSwitchToAdminDashboardBtn1.show()

            if not self.uOSPSwitchToAdminDashboardBtn2.isVisible():
                self.uOSPSwitchToAdminDashboardBtn2.show()

            if not self.uOSPSwitchToAdminDashboardBtn1.isEnabled():
                self.uOSPSwitchToAdminDashboardBtn1.setEnabled(True)

            if not self.uOSPSwitchToAdminDashboardBtn2.isEnabled():
                self.uOSPSwitchToAdminDashboardBtn2.setEnabled(True)

        if self.userType is False:
            if self.uOSPSwitchToAdminDashboardBtn1.isEnabled():
                self.uOSPSwitchToAdminDashboardBtn1.setDisabled(True)

            if self.uOSPSwitchToAdminDashboardBtn2.isEnabled():
                self.uOSPSwitchToAdminDashboardBtn2.setDisabled(True)

            if self.uOSPSwitchToAdminDashboardBtn2.isVisible():
                self.uOSPSwitchToAdminDashboardBtn1.hide()
                self.uOSPSwitchToAdminDashboardBtn2.hide()

        self.student_manager.add_in_combobox()
        self.student_journey_manager.add_in_combobox()

    def user_view_student(self):
        self.uOSPMInnerStackWidget.setCurrentIndex(0)
        self.student_manager.refresh_student_view()

    def user_view_journey(self):
        self.user_outer_stack_page()
        self.uOSPMInnerStackWidget.setCurrentIndex(1)
        self.student_journey_manager.refresh_student_journey_view()
        # self.student_manager.refresh_student_view()

    def user_view_fee(self):
        self.uOSPMInnerStackWidget.setCurrentIndex(2)
        self.student_fee_receipt_manager.refresh_student_fee_receipt()

    def table_row_single_click(self, item):
        sender_widget = self.sender()
        current_row = item.row()
        if self.last_selected_row == current_row:
            if sender_widget == self.aOSPISUniversityTable:
                self.aOSPISUniversityTable.clearSelection()
                self.aOSPISUniversityTable.selectionModel().clearCurrentIndex()

            if sender_widget == self.aOSPISCourseTable:
                self.aOSPISCourseTable.clearSelection()
                self.aOSPISCourseTable.selectionModel().clearCurrentIndex()

            if sender_widget == self.aOSPISSubjectTable:
                self.aOSPISSubjectTable.clearSelection()
                self.aOSPISSubjectTable.selectionModel().clearCurrentIndex()

            if sender_widget == self.aOSPISExamTable:
                self.aOSPISExamTable.clearSelection()
                self.aOSPISExamTable.selectionModel().clearCurrentIndex()

            if sender_widget == self.aOSPISAllotmentLBTable:
                self.aOSPISAllotmentLBTable.clearSelection()
                self.aOSPISAllotmentLBTable.selectionModel().clearCurrentIndex()
                self.aOSPISAllotmentRTTable.setRowCount(0)
                self.aOSPISAllotmentRBTable.setRowCount(0)

            if sender_widget == self.aOSPISAllotmentRTTable:
                self.aOSPISAllotmentRTTable.clearSelection()
                self.aOSPISAllotmentRTTable.selectionModel().clearCurrentIndex()
                self.aOSPISAllotmentRBTable.setRowCount(0)

            if sender_widget == self.aOSPISAllotmentRBTable:
                self.aOSPISAllotmentRBTable.clearSelection()
                self.aOSPISAllotmentRBTable.selectionModel().clearCurrentIndex()

            if sender_widget == self.aOSPISJViewTable:
                self.aOSPISJViewTable.clearSelection()
                self.aOSPISJViewTable.selectionModel().clearCurrentIndex()

            if sender_widget == self.uOSPMIStudentViewTable:
                self.uOSPMIStudentViewTable.clearSelection()
                self.uOSPMIStudentViewTable.selectionModel().clearCurrentIndex()

            self.last_selected_row = None
        else:
            self.last_selected_row = current_row

    def table_double_click(self, index):
        sender_widget = self.sender()

        if isinstance(sender_widget, QTableWidget):
            if sender_widget == self.aOSPISUniversityTable:
                if self.aOSPISAVUCourseFrm.isVisible():
                    self.aOSPISAVUCourseFrm.hide()
                else:
                    self.aOSPISAVUCourseFrm.show()

                if self.aOSPISAVUSubjectFrm.isVisible():
                    self.aOSPISAVUSubjectFrm.hide()
                else:
                    self.aOSPISAVUSubjectFrm.show()

                if self.aOSPISAVUExamFrm.isVisible():
                    self.aOSPISAVUExamFrm.hide()
                else:
                    self.aOSPISAVUExamFrm.show()

            if sender_widget == self.aOSPISCourseTable:
                if self.aOSPISAVUUniversityFrm.isVisible():
                    self.aOSPISAVUUniversityFrm.hide()
                else:
                    self.aOSPISAVUUniversityFrm.show()

                if self.aOSPISAVUSubjectFrm.isVisible():
                    self.aOSPISAVUSubjectFrm.hide()
                else:
                    self.aOSPISAVUSubjectFrm.show()

                if self.aOSPISAVUExamFrm.isVisible():
                    self.aOSPISAVUExamFrm.hide()
                else:
                    self.aOSPISAVUExamFrm.show()

            if sender_widget == self.aOSPISSubjectTable:
                if self.aOSPISAVUUniversityFrm.isVisible():
                    self.aOSPISAVUUniversityFrm.hide()
                else:
                    self.aOSPISAVUUniversityFrm.show()

                if self.aOSPISAVUCourseFrm.isVisible():
                    self.aOSPISAVUCourseFrm.hide()
                else:
                    self.aOSPISAVUCourseFrm.show()

                if self.aOSPISAVUExamFrm.isVisible():
                    self.aOSPISAVUExamFrm.hide()
                else:
                    self.aOSPISAVUExamFrm.show()

            if sender_widget == self.aOSPISExamTable:
                if self.aOSPISAVUUniversityFrm.isVisible():
                    self.aOSPISAVUUniversityFrm.hide()
                else:
                    self.aOSPISAVUUniversityFrm.show()

                if self.aOSPISAVUCourseFrm.isVisible():
                    self.aOSPISAVUCourseFrm.hide()
                else:
                    self.aOSPISAVUCourseFrm.show()

                if self.aOSPISAVUSubjectFrm.isVisible():
                    self.aOSPISAVUSubjectFrm.hide()
                else:
                    self.aOSPISAVUSubjectFrm.show()

            if sender_widget == self.aOSPISAllotmentLBTable:
                if self.aOSPISAllotmentRightFrm.isVisible():
                    self.aOSPISAllotmentRightFrm.hide()
                else:
                    self.aOSPISAllotmentRightFrm.show()

                if self.aOSPISAllotmentLTopFrm.isVisible():
                    self.aOSPISAllotmentLTopFrm.hide()
                else:
                    self.aOSPISAllotmentLTopFrm.show()

            if sender_widget == self.aOSPISAllotmentRTTable:
                if self.aOSPISAllotmentLeftFrm.isVisible():
                    self.aOSPISAllotmentLeftFrm.hide()
                else:
                    self.aOSPISAllotmentLeftFrm.show()

                if self.aOSPISAllotmentRBottomFrm.isVisible():
                    self.aOSPISAllotmentRBottomFrm.hide()
                else:
                    self.aOSPISAllotmentRBottomFrm.show()

            if sender_widget == self.aOSPISAllotmentRBTable:
                if self.aOSPISAllotmentLeftFrm.isVisible():
                    self.aOSPISAllotmentLeftFrm.hide()
                else:
                    self.aOSPISAllotmentLeftFrm.show()

                if self.aOSPISAllotmentRTopFrm.isVisible():
                    self.aOSPISAllotmentRTopFrm.hide()
                else:
                    self.aOSPISAllotmentRTopFrm.show()

    # ----------------------inner stack widget implement-------------------------------

    # ----------------university implement---------------------
    class UniversityManagement:
        """Class for managing courses within the University management system."""

        def __init__(self, outer_instance):
            """
            Initialize UniversityManagement instance.

            Args:
                outer_instance: The outer instance of the application.
            """
            self.outer_instance = outer_instance

        def add_university(self):
            """
            Add a new university.
            """
            try:
                dialog = UniversityDialog()
                dialog.ui()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in opening university dialog", str(e))
            finally:
                self.refresh_university_view()

        def refresh_university_view(self):
            """
            Refresh the view of universities.
            """
            try:
                self.clear_selections()
                university = self.outer_instance.query.get_university_detail()
                if university:
                    self.populate_university_table(university)
                else:
                    self.outer_instance.aOSPISUniversityTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing university", str(e))
            finally:
                self.outer_instance.aOSPISUniversityTable.resizeColumnsToContents()

        def clear_selections(self):
            """
            Clear selections in the university table.
            """
            if self.outer_instance.aOSPISUniversityTable.selectedIndexes():
                self.outer_instance.aOSPISUniversityTable.clearSelection()
                self.outer_instance.aOSPISUniversityTable.selectionModel().clearCurrentIndex()

        def populate_university_table(self, university: list):
            """
            Populate the university table with given data.

            Args:
                university: List of tuples containing university data.
            """
            self.outer_instance.aOSPISUniversityTable.setRowCount(len(university))
            for row, university in enumerate(university):
                self.populate_university_row(row, university)

        def populate_university_row(self, row: int, university: tuple):
            """
            Populate a single row of the university table with given data.

            Args:
                row: Row index.
                university: Tuple containing university data.
            """
            for col, value in enumerate(university):
                if col != 6:
                    item = QTableWidgetItem(str(value))
                    self.outer_instance.aOSPISUniversityTable.setItem(row, col, item)
            self.add_controls(row, university[1])

        def add_controls(self, row: int, university_id):
            """
            Add control buttons to a row of the university table.

            Args:
                row: Row index.
                university_id: ID of the university.
            """
            widget = ThreeBtnWidget()
            widget.firstEditBtn.clicked.connect(lambda: self.update_university_detail(university_id))
            widget.secondDeleteBtn.clicked.connect(lambda: self.delete_university_detail(university_id))
            self.outer_instance.aOSPISUniversityTable.setCellWidget(row, 3, widget)

        def update_university_detail(self, university_id):
            """
            Update the details of a university.

            Args:
                university_id: ID of the university.
            """
            try:
                for row in range(self.outer_instance.aOSPISUniversityTable.rowCount()):
                    if self.outer_instance.aOSPISUniversityTable.item(row, 1).text() == str(university_id):
                        self.outer_instance.aOSPISUniversityTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISUniversityTable)
                if data:
                    dialog = UniversityDialog(use_type="update", university_code=data[0], university_short_name=data[1],
                                              university_name=data[2])
                    dialog.ui()
                    dialog.set_values()
                    dialog.exec()
                else:
                    Common.show_message("Select University item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in Updating University Detail", str(e))
                pass
            finally:
                self.refresh_university_view()

        def delete_university_detail(self, university_id):
            """
            Delete the details of a university.

            Args:
                university_id: ID of the university.
            """
            try:
                for row in range(self.outer_instance.aOSPISUniversityTable.rowCount()):
                    if self.outer_instance.aOSPISUniversityTable.item(row, 1).text() == str(university_id):
                        self.outer_instance.aOSPISUniversityTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISUniversityTable)
                if data:
                    output = Common.show_message(f"Are sure want to delete university '{data[2]}'.", "YN")
                    if output == QMessageBox.Yes:
                        success = self.outer_instance.query.delete_university_detail(data[0])
                        if success:
                            Common.show_message("Delete Successfully!", "I")
                        else:
                            Common.show_message("Failed to delete!", "C")
                    else:
                        Common.show_message("Delete Cancel!", "I")
                else:
                    Common.show_message("Select University item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in Deleting University Detail", str(e))
            finally:
                self.refresh_university_view()

    # ----------------End university implement---------------------

    # ------------------Course implement----------------------
    class CourseManagement:
        """Class for managing courses within the course management system."""

        def __init__(self, outer_instance):
            """Initialize the CourseManagement instance.

            Args:
                outer_instance: Reference to the outer instance.
            """
            self.outer_instance = outer_instance

        def add_course(self):
            """Open a dialog window to add a new course and refresh the course view."""
            try:
                dialog = CourseDialog()
                dialog.ui()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in opening course dialog", str(e))
            finally:
                self.refresh_course_view()

        def refresh_course_view(self):
            """Refresh the course view with the latest course details."""
            try:
                self.clear_selections()
                course = self.outer_instance.query.get_course_detail()
                if course:
                    self.populate_course_table(course)
                else:
                    self.outer_instance.aOSPISCourseTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing course", str(e))
            finally:
                self.outer_instance.aOSPISCourseTable.resizeColumnsToContents()

        def clear_selections(self):
            """Clear any selections made in the course table."""
            if self.outer_instance.aOSPISCourseTable.selectedIndexes():
                self.outer_instance.aOSPISCourseTable.clearSelection()
                self.outer_instance.aOSPISCourseTable.selectionModel().clearCurrentIndex()

        def populate_course_table(self, course: list):
            """Populate the course table with the given course data.

            Args:
                course: List containing course details.
            """
            self.outer_instance.aOSPISCourseTable.setRowCount(len(course))
            for row, course in enumerate(course):
                self.populate_course_row(row, course)

        def populate_course_row(self, row: int, course: tuple):
            """Populate a single row of the course table with course details.

            Args:
                row: Row index.
                course: Tuple containing course details.
            """
            for col, value in enumerate(course):
                item = QTableWidgetItem(str(value))
                self.outer_instance.aOSPISCourseTable.setItem(row, col, item)
            self.add_controls(row, course[1])

        def add_controls(self, row: int, course_id: str):
            """Add control buttons to a row in the course table.

            Args:
                row: Row index.
                course_id: ID of the course.
            """
            widget = ThreeBtnWidget()
            widget.firstEditBtn.clicked.connect(lambda: self.update_course_detail(course_id))
            widget.secondDeleteBtn.clicked.connect(lambda: self.delete_course_detail(course_id))
            self.outer_instance.aOSPISCourseTable.setCellWidget(row, 4, widget)

        def update_course_detail(self, course_id: str):
            """Update course details based on user input.

            Args:
                course_id: ID of the course to be updated.
            """
            try:
                for row in range(self.outer_instance.aOSPISCourseTable.rowCount()):
                    if self.outer_instance.aOSPISCourseTable.item(row, 1).text() == str(course_id):
                        self.outer_instance.aOSPISCourseTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISCourseTable)
                if data:
                    dialog = CourseDialog(use_type="update", course_code=data[0], course_short_name=data[1],
                                          course_name=data[2], year=data[3])
                    dialog.ui()
                    dialog.set_values()
                    dialog.exec()
                else:
                    Common.show_message("Select Course item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in updating course detail", str(e))
            finally:
                self.refresh_course_view()

        def delete_course_detail(self, course_id: str):
            """Delete course details based on user input.

            Args:
                course_id: ID of the course to be deleted.
            """
            try:
                for row in range(self.outer_instance.aOSPISCourseTable.rowCount()):
                    if self.outer_instance.aOSPISCourseTable.item(row, 1).text() == str(course_id):
                        self.outer_instance.aOSPISCourseTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISCourseTable)
                if data:
                    output = Common.show_message(f"Are sure want to delete Course '{data[2]}'.", "YN")
                    if output == QMessageBox.Yes:
                        success = self.outer_instance.query.delete_course_detail(data[0])
                        if success:
                            Common.show_message("Delete Successfully!", "I")
                        else:
                            Common.show_message("Failed to delete!", "C")
                    else:
                        Common.show_message("Delete Cancel!", "I")
                else:
                    Common.show_message("Select Course item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in deleting course detail", str(e))
            finally:
                self.refresh_course_view()

    # ----------------End Course Implement------------------

    # ------------------Subject Implement-------------------
    class SubjectManagement:
        """Class for managing subjects within the application."""

        def __init__(self, outer_instance):
            """
            Initialize an instance of SubjectManagement.

            Args:
                outer_instance: Reference to the outer instance.
            """
            self.outer_instance = outer_instance

        def add_subject(self):
            """
            Method to add a new subject.
            Initiates a dialog for adding a subject and refreshes the subject view afterward.
            """
            try:
                dialog = SubjectDialog()
                dialog.ui()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in opening subject dialog", str(e))
            finally:
                self.refresh_subject_view()

        def refresh_subject_view(self):
            """
            Refreshes the view of subjects.
            Clears selections, retrieves subject details from an outer instance,
            populates the subject table if there are subjects, or clears the table if there are none.
            """
            try:
                self.clear_selections()
                subject = self.outer_instance.query.get_subject_detail()
                if subject:
                    self.populate_subject_table(subject)
                else:
                    self.outer_instance.aOSPISSubjectTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing subject detail", str(e))
            finally:
                self.outer_instance.aOSPISSubjectTable.resizeColumnsToContents()

        def clear_selections(self):
            """
            Clears any selected rows in the subject table.
            """
            if self.outer_instance.aOSPISSubjectTable.selectedIndexes():
                self.outer_instance.aOSPISSubjectTable.clearSelection()
                self.outer_instance.aOSPISSubjectTable.selectionModel().clearCurrentIndex()

        def populate_subject_table(self, subjects: list):
            """
            Populates the subject table with data.

            Args:
                subjects: List of subjects to populate the table.
            """
            self.outer_instance.aOSPISSubjectTable.setRowCount(len(subjects))
            for row, subject in enumerate(subjects):
                self.populate_subject_row(row, subject)

        def populate_subject_row(self, row: int, subject: tuple):
            """
            Populates a single row of the subject table with data.

            Args:
                row: Row index to populate.
                subject: Tuple containing subject details.
            """
            for col, value in enumerate(subject):
                item = QTableWidgetItem(str(value))
                self.outer_instance.aOSPISSubjectTable.setItem(row, col, item)
            self.add_controls(row, subject[0])

        def add_controls(self, row: int, subject_id: str):
            """
            Adds control buttons to a specific row in the subject table.

            Args:
                row: Row index to add controls to.
                subject_id: ID of the subject.
            """
            widget = ThreeBtnWidget()
            widget.firstEditBtn.clicked.connect(lambda: self.update_subject_detail(subject_id))
            widget.secondDeleteBtn.clicked.connect(lambda: self.delete_subject_detail(subject_id))
            self.outer_instance.aOSPISSubjectTable.setCellWidget(row, 2, widget)

        def update_subject_detail(self, subject_id: str):
            """
            Updates the details of a selected subject.

            Args:
                subject_id: ID of the subject to be updated.
            """
            try:
                for row in range(self.outer_instance.aOSPISSubjectTable.rowCount()):
                    if self.outer_instance.aOSPISSubjectTable.item(row, 0).text() == str(subject_id):
                        self.outer_instance.aOSPISSubjectTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISSubjectTable)
                if data:
                    dialog = SubjectDialog(use_type="update", subject_code=data[0], subject_name=data[1])
                    dialog.ui()
                    dialog.set_values()
                    dialog.exec()
                else:
                    Common.show_message("Select Subject item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in updating subject detail", str(e))
            finally:
                self.refresh_subject_view()

        def delete_subject_detail(self, subject_id: str):
            """
            Deletes the selected subject after confirmation.

            Args:
                subject_id: ID of the subject to be deleted.
            """
            try:
                for row in range(self.outer_instance.aOSPISSubjectTable.rowCount()):
                    if self.outer_instance.aOSPISSubjectTable.item(row, 0).text() == str(subject_id):
                        self.outer_instance.aOSPISSubjectTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISSubjectTable)
                if data:
                    output = Common.show_message(f"Are sure want to delete Subject '{data[1]}'.", "YN")
                    if output == QMessageBox.Yes:
                        success = self.outer_instance.query.delete_subject_detail(data[0])
                        if success:
                            Common.show_message("Delete Successfully!", "I")
                        else:
                            Common.show_message("Failed to delete!", "C")
                    else:
                        Common.show_message("Delete Cancel!", "I")
                else:
                    Common.show_message("Select Subject item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in deleting subject detail", str(e))
            finally:
                self.refresh_subject_view()

    # -----------------End Subject Implement---------------------

    # -----------------Transport implement------------------
    class TransportPlaceFeeManagement:
        """Class for managing transport place fees."""

        def __init__(self, outer_instance):
            """Initialize TransportPlaceFeeManagement.

            Args:
                outer_instance: The instance of the main application.
            """
            self.outer_instance = outer_instance

        def add_transport_place_fee(self):
            """Add a transport place fee."""

            try:
                dialog = TransportPlaceFeeDialog()
                dialog.ui()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in opening", str(e))
            finally:
                self.refresh_transport_place_fee_view()

        def refresh_transport_place_fee_view(self):
            """Refresh the view of transport place fees."""
            try:
                self.clear_selections()
                transport = self.outer_instance.query.get_transport_place_fee_detail()
                if transport:
                    self.populate_transport_place_fee_table(transport)
                else:
                    self.outer_instance.aOSPISExamTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing place fee", str(e))
            finally:
                self.outer_instance.aOSPISExamTable.resizeColumnsToContents()

        def clear_selections(self):
            """Clear selections in the table."""
            if self.outer_instance.aOSPISExamTable.selectedIndexes():
                self.outer_instance.aOSPISExamTable.clearSelection()
                self.outer_instance.aOSPISExamTable.selectionModel().clearCurrentIndex()

        def populate_transport_place_fee_table(self, transports: list):
            """Populate the transport place fee table.

            Args:
                transports: List of transport details.
            """
            self.outer_instance.aOSPISExamTable.setRowCount(len(transports))
            for row, transport in enumerate(transports):
                self.populate_transport_place_fee_row(row, transport)

        def populate_transport_place_fee_row(self, row: int, transport: tuple):
            """Populate a single row in the transport place fee table.

            Args:
                row: The row index.
                transport: Tuple containing transport details.
            """
            for col, value in enumerate(transport):
                item = QTableWidgetItem(str(value))
                self.outer_instance.aOSPISExamTable.setItem(row, col, item)
            self.add_controls(row, transport[0])

        def add_controls(self, row: int, transport_id: str):
            """Add controls to a row in the transport place fee table.

            Args:
                row: The row index.
                transport_id: The transport ID.
            """
            widget = ThreeBtnWidget()
            widget.firstEditBtn.clicked.connect(lambda: self.update_transport_place_fee_detail(transport_id))
            widget.secondDeleteBtn.clicked.connect(lambda: self.delete_transport_place_fee_detail(transport_id))
            self.outer_instance.aOSPISExamTable.setCellWidget(row, 3, widget)

        def update_transport_place_fee_detail(self, transport_id: str):
            """Update a transport place fee detail.

            Args:
                transport_id: The ID of the transport fee to update.
            """
            try:
                for row in range(self.outer_instance.aOSPISExamTable.rowCount()):
                    if self.outer_instance.aOSPISExamTable.item(row, 0).text() == str(transport_id):
                        self.outer_instance.aOSPISExamTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISExamTable)
                if data:
                    dialog = TransportPlaceFeeDialog(use_type="update", center_code=data[0], center_name=data[1],
                                                     fee=data[2])
                    dialog.ui()
                    dialog.set_values()
                    dialog.exec()
                else:
                    Common.show_message("Select Center and Fee item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in updating place and fee", str(e))
            finally:
                self.refresh_transport_place_fee_view()

        def delete_transport_place_fee_detail(self, transport_id: str):
            """Delete a transport place fee detail.

            Args:
                transport_id: The ID of the transport fee to delete.
            """
            try:
                for row in range(self.outer_instance.aOSPISExamTable.rowCount()):
                    if self.outer_instance.aOSPISExamTable.item(row, 0).text() == str(transport_id):
                        self.outer_instance.aOSPISExamTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.aOSPISExamTable)
                if data:
                    output = Common.show_message(f"Are sure want to delete Center Code '{data[0]}'.", "YN")
                    if output == QMessageBox.Yes:
                        success = self.outer_instance.query.delete_transport_place_fee_detail(data[0])
                        if success:
                            Common.show_message("Delete Successfully!", "I")
                        else:
                            Common.show_message("Failed to delete!", "C")
                    else:
                        Common.show_message("Delete Cancel!", "I")
                else:
                    Common.show_message("Select Center and Fee item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in deleting place and fee", str(e))
            finally:
                self.refresh_transport_place_fee_view()

    # -----------------End Transport implement------------------

    # -----------------Allotment---------------------------
    class SubjectAllotmentManager:
        """A class to manage the subject allotments in a university, interfacing with a GUI for data handling."""

        def __init__(self, outer_instance):
            """
            Initializes the SubjectAllotmentManager with a reference to an outer instance that handles GUI and
            database interactions.

            Args:
                outer_instance: An instance of another class providing database access and GUI operations.
            """
            self.outer_instance = outer_instance

        def populate_combo_boxes(self):
            """
            Populates the combo_boxes in the GUI with data fetched from the database,
            such as university and course names.
            """
            try:
                university_short_name = self.outer_instance.query.get_university_short_name()
                if university_short_name is not None:
                    for i in university_short_name:
                        self.outer_instance.aOSPISALTUniversity.addItem(i[0])

                course_short_name = self.outer_instance.query.get_course_short_name()
                if course_short_name is not None:
                    for i in course_short_name:
                        self.outer_instance.aOSPISALTCourse.addItem(i[0])
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in populate combobox", str(e))

        def read_subject_allotment_detail(self, usn: str, csn: str, sem: str):
            """
            Fetches and returns the details of subject allotments based on university short name, course short name,
            and semester.

            Args:
                usn: University short name.
                csn: Course short name.
                sem: Semester.

            Returns:
                List of subject allotments or None if no data is found.
            """
            if usn != 'Select University' and csn != 'Select Course' and sem != "Select Semester":
                query = f"SELECT university_short_name, course_short_name, semester, subject_code, subject_name FROM allotment WHERE university_short_name='{usn}' AND course_short_name='{csn}' AND semester='{sem}';"

            elif usn != 'Select University' and csn != 'Select Course':
                query = f"SELECT university_short_name, course_short_name, semester, subject_code, subject_name FROM allotment WHERE university_short_name='{usn}' AND course_short_name='{csn}';"

            elif usn != 'Select University' and sem != 'Select Semester':
                query = f"SELECT university_short_name, course_short_name, semester, subject_code, subject_name FROM allotment WHERE university_short_name='{usn}' AND semester='{sem}';"

            elif csn != 'Select Course' and sem != "Select Semester":
                query = f"SELECT university_short_name, course_short_name, semester, subject_code, subject_name FROM allotment WHERE course_short_name='{csn}' AND semester='{sem}';"

            elif usn != 'Select University':
                query = f"SELECT university_short_name, course_short_name, semester, subject_code, subject_name FROM allotment WHERE university_short_name='{usn}';"

            elif csn != 'Select Course':
                query = f"SELECT university_short_name, course_short_name, semester, subject_code, subject_name FROM allotment WHERE course_short_name='{csn}';"

            elif sem != 'Select Semester':
                query = f"SELECT university_short_name, course_short_name, semester, subject_code, subject_name FROM allotment WHERE semester='{sem}';"

            else:
                query = None

            if query:
                read_allotment = self.outer_instance.query.get_usn_csn_sem_sc_sn(query)
                return read_allotment
            return

        def allot_subject(self):
            """
            Manages the addition of new subject allotments through the GUI,
            including data validation and interaction flow.
            """
            try:
                university_short_name = self.outer_instance.aOSPISALTUniversity.currentText()
                course_name = self.outer_instance.aOSPISALTCourse.currentText()
                semester = self.outer_instance.aOSPISALTSemester.currentText()

                if university_short_name != "Select University" and course_name != "Select Course" and semester != "Select Semester":
                    value = (university_short_name, course_name, semester)
                    success = self.outer_instance.query.get_is_active_from_exam_detail(value)
                    if success is None:
                        is_exam_is_active = 0
                    else:
                        is_exam_is_active = success[0]

                    if not is_exam_is_active:
                        dialog = AllotmentDialog(usn=university_short_name, csn=course_name, semester=semester)
                        dialog.ui()
                        dialog.populate_value_in_combobox()
                        dialog.aAUniversity.setCurrentIndex(1)
                        dialog.aAUniversity.setEnabled(False)
                        dialog.aACourse.setCurrentIndex(1)
                        dialog.aACourse.setEnabled(False)
                        dialog.aASemester.setCurrentIndex(1)
                        dialog.aASemester.setEnabled(False)
                        dialog.populate_subject_combo_box()
                        dialog.exec()
                    else:
                        Common.show_message("Exam is active. You can't add subjects.", "I")
                else:
                    Common.show_message("Select University, Course, and Semester!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in allotting subject", str(e))
            finally:
                self.refresh_subject_allotment_view()

        def refresh_subject_allotment_view(self):
            """
            Refreshes the view in the GUI that displays subject allotments, updating the information shown to the user.
            """
            university_short_name = self.outer_instance.aOSPISALTUniversity.currentText()
            course_name = self.outer_instance.aOSPISALTCourse.currentText()
            semester = self.outer_instance.aOSPISALTSemester.currentText()
            try:
                self.clear_selections()
                self.outer_instance.aOSPISAllotmentRTTable.setRowCount(0)
                self.outer_instance.aOSPISAllotmentRBTable.setRowCount(0)
                subject_allotment = self.read_subject_allotment_detail(university_short_name, course_name, semester)
                if subject_allotment:
                    self.populate_subject_allotment_table(subject_allotment)
                else:
                    self.outer_instance.aOSPISAllotmentLBTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing subject allot", str(e))
            finally:
                self.outer_instance.aOSPISAllotmentLBTable.resizeColumnsToContents()

        def clear_selections(self):
            """
            Clears any user selections in the GUI, typically used when resetting forms or refreshing data.
            """
            try:
                if self.outer_instance.aOSPISAllotmentLBTable.selectedIndexes():
                    self.outer_instance.aOSPISAllotmentLBTable.clearSelection()
                    self.outer_instance.aOSPISAllotmentLBTable.selectionModel().clearCurrentIndex()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in clearing selections", str(e))

        def populate_subject_allotment_table(self, allotments: list):
            """
            Fills the subject allotment table in the GUI with data.

            Args:
                allotments: A list of subject allotment data to be displayed in the table.
            """
            try:
                self.outer_instance.aOSPISAllotmentLBTable.setRowCount(len(allotments))
                for row, allotment in enumerate(allotments):
                    self.populate_subject_allotment_row(row, allotment)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error populating subject allotment table", str(e))

        def populate_subject_allotment_row(self, row: int, allotment: tuple):
            """
            Populates a specific row in the subject allotment table with data.

            Args:
                row: The row index in the table.
                allotment: The subject allotment data for the specific row.
            """
            try:
                for col, value in enumerate(allotment):
                    item = QTableWidgetItem(str(value))
                    self.outer_instance.aOSPISAllotmentLBTable.setItem(row, col, item)
                allotment_select_criteria = (allotment[0], allotment[1], str(allotment[2]), str(allotment[3]))
                self.add_controls(row, allotment_select_criteria)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error populating subject allotment row", str(e))

        def add_controls(self, row: int, allotment_select_criteria: tuple):
            """
            Adds interactive controls such as buttons for editing and deleting to a row in the subject allotment table.

            Args:
                row: The row index where controls will be added.
                allotment_select_criteria: Criteria used to select the allotment for modification or deletion.
            """
            try:
                widget = ThreeBtnWidget()
                widget.firstEditBtn.clicked.connect(
                    lambda: self.update_subject_allotment_detail(allotment_select_criteria))
                widget.secondDeleteBtn.clicked.connect(
                    lambda: self.delete_subject_allotment_detail(allotment_select_criteria))
                self.outer_instance.aOSPISAllotmentLBTable.setCellWidget(row, 5, widget)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in adding control in allotment", str(e))

        def update_allotment(self, update_detail: tuple):
            try:
                dialog = AllotmentDialog(use_type="update", usn=update_detail[0], csn=update_detail[1],
                                         semester=update_detail[2], subject_name=update_detail[3])
                dialog.ui()
                dialog.populate_value_in_combobox()
                dialog.aAUniversity.setCurrentIndex(1)
                dialog.aAUniversity.setEnabled(False)
                dialog.aACourse.setCurrentIndex(1)
                dialog.aACourse.setEnabled(False)
                dialog.aASemester.setCurrentIndex(1)
                dialog.aASemester.setEnabled(False)
                dialog.populate_subject_combo_box()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in updating subject allotment", str(e))
            finally:
                self.refresh_subject_allotment_view()

        def update_subject_allotment_detail(self, allotment_select_criteria: tuple):
            """
            Updates the details of a specific subject allotment based on the provided selection criteria.

            Args:
                allotment_select_criteria: Criteria used to identify the specific allotment to be updated.
            """
            try:
                success = Common().select_rows_based_on_criteria(self.outer_instance.aOSPISAllotmentLBTable,
                                                                 allotment_select_criteria)
                if not success:
                    return

                data = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentLBTable)
                if data:
                    value = (data[0], data[1], data[2])
                    success = self.outer_instance.query.get_is_active_from_exam_detail(value)
                    if success:
                        if not success[0]:
                            self.update_allotment(update_detail=(data[0], data[1], data[2], data[4]))
                        else:
                            Common.show_message("Exam is active you can't update it. Try Later!", "I")
                    else:
                        self.update_allotment(update_detail=(data[0], data[1], data[2], data[4]))
                else:
                    Common.show_message("Select Subject Allotment item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error updating subject allotment detail", str(e))
            finally:
                self.refresh_subject_allotment_view()

        def delete_allotment(self, delete_allotment: tuple):
            try:
                output = Common.show_message(f"Are sure want to delete selected allotment.", "YN")
                if output == QMessageBox.Yes:
                    success = self.outer_instance.query.delete_allotment_detail(
                        (delete_allotment[0], delete_allotment[1], delete_allotment[2], delete_allotment[3]))
                    if success:
                        Common.show_message("Delete Successfully!", "I")
                    else:
                        Common.show_message("Failed to delete!", "C")
                else:
                    Common.show_message("Delete Cancel!", "I")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in deleting subject allotment", str(e))
            finally:
                self.refresh_subject_allotment_view()

        def delete_subject_allotment_detail(self, allotment_select_criteria: tuple):
            """
            Deletes a specific subject allotment from the database based on the provided selection criteria.

            Args:
                allotment_select_criteria: Criteria used to identify the specific allotment to be deleted.
            """
            try:
                success = Common().select_rows_based_on_criteria(self.outer_instance.aOSPISAllotmentLBTable,
                                                                 allotment_select_criteria)
                if not success:
                    return

                data = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentLBTable)
                if data:
                    value = (data[0], data[1], data[2])
                    success = self.outer_instance.query.get_is_active_from_exam_detail(value)
                    if success:
                        if not success[0]:
                            self.delete_allotment(delete_allotment=(data[0], data[1], data[2], data[3]))
                        else:
                            Common.show_message("Exam is active you can't delete it. Try Later!", "I")
                    else:
                        self.delete_allotment(delete_allotment=(data[0], data[1], data[2], data[3]))
                else:
                    Common.show_message("Select Center and Fee item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in Deleting subject allotment", str(e))
            finally:
                self.refresh_subject_allotment_view()

    # ----------------end of subject allotment-----------

    # --------------------exam detail allotment----------------
    class ExamManagement:
        def __init__(self, outer_instance):
            """
            Initialize the ExamManagement instance with a reference to the outer instance.

            Args:
                outer_instance: The instance of the parent or associated class that holds shared resources and components.
            """
            self.outer_instance = outer_instance

        def allot_exam_detail(self):
            """
            Handles the process of allotting exam details. Retrieves the selected subject from the GUI,
            creates and configures an exam detail dialog for user input, and updates the exam details view.
            """
            read_subject = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentLBTable)
            if read_subject:
                try:
                    dialog = ExamDetailDialog(usn=read_subject[0], csn=read_subject[1], semester=read_subject[2])
                    dialog.ui()
                    dialog.aEDUniversity.setCurrentIndex(1)
                    dialog.aEDUniversity.setEnabled(False)
                    dialog.aEDCourse.setCurrentIndex(1)
                    dialog.aEDCourse.setEnabled(False)
                    dialog.aEDSemester.setCurrentIndex(1)
                    dialog.aEDSemester.setEnabled(False)
                    dialog.add_center_in_combobox()
                    dialog.exec()
                except Exception as e:
                    self.outer_instance.show_message_in_statusbar("Error in allotting exam detail", str(e))
                finally:
                    self.refresh_exam_detail_view()
            else:
                Common.show_message("Select Subject Allotment!.")

        def refresh_exam_detail_view(self):
            """
            Refreshes the exam detail view by fetching and displaying current details for the selected subject.
            Clears selections and updates the table with new data if available.
            """
            try:
                self.clear_selections()
                read_subject = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentLBTable)
                if read_subject:
                    exam_detail = self.outer_instance.query.get_exam_detail(
                        (read_subject[0], read_subject[1], read_subject[2]))
                    if exam_detail:
                        self.populate_exam_detail_table(exam_detail)
                    else:
                        self.outer_instance.aOSPISAllotmentRTTable.setRowCount(0)
                else:
                    Common.show_message("Select Subject Allotment!.")
                    self.outer_instance.aOSPISAllotmentRTTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing Exam detail", str(e))
            finally:
                self.outer_instance.aOSPISAllotmentRTTable.resizeColumnsToContents()
                self.outer_instance.aOSPISAllotmentRBTable.setRowCount(0)

        def clear_selections(self):
            """
            Clears all selections and the current index in the exam details table.
            """
            if self.outer_instance.aOSPISAllotmentRTTable.selectedIndexes():
                self.outer_instance.aOSPISAllotmentRTTable.clearSelection()
                self.outer_instance.aOSPISAllotmentRTTable.selectionModel().clearCurrentIndex()

        def populate_exam_detail_table(self, exam_detail: tuple):
            """
            Populates the exam detail table with the provided exam details.

            Args:
                exam_detail: A tuple containing the details of the exam to be displayed in the table.
            """
            self.outer_instance.aOSPISAllotmentRTTable.setRowCount(1)
            for col, value in enumerate(exam_detail):
                item = QTableWidgetItem(str(value))
                self.outer_instance.aOSPISAllotmentRTTable.setItem(0, col, item)
            exam_detail_select_criteria = (exam_detail[0], exam_detail[1], str(exam_detail[2]))
            self.add_controls(0, exam_detail_select_criteria)

        def add_controls(self, row: int, exam_detail_select_criteria: tuple):
            """
            Adds interactive buttons to the specified row in the table, allowing for operations like updating exam details.

            Args:
                row: The row index where the buttons will be added.
                exam_detail_select_criteria: The criteria used to select the exam details to be modified.
            """
            widget = ThreeBtnWidget()
            widget.firstEditBtn.clicked.connect(lambda: self.update_exam_detail(exam_detail_select_criteria))
            self.outer_instance.aOSPISAllotmentRTTable.setCellWidget(row, 6, widget)

        def update_exam_detail(self, exam_detail_select_criteria: tuple):
            """
            Handles the updating of exam details. Opens a dialog pre-filled with selected exam data for editing.

            Args:
                exam_detail_select_criteria: The criteria used to fetch the details to be updated.
            """
            try:
                success = Common().select_rows_based_on_criteria(self.outer_instance.aOSPISAllotmentRTTable,
                                                                 exam_detail_select_criteria)
                if not success:
                    return

                data = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentRTTable)
                if data:
                    exam_date = Common().get_table_data(self.outer_instance.aOSPISAllotmentRBTable, column=1)
                    dialog = ExamDetailDialog(use_type="update", usn=data[0], csn=data[1], semester=data[2],
                                              center=data[3],
                                              shift=data[4], exam_date=exam_date)
                    dialog.ui()
                    dialog.aEDUniversity.setCurrentIndex(1)
                    dialog.aEDUniversity.setEnabled(False)
                    dialog.aEDCourse.setCurrentIndex(1)
                    dialog.aEDCourse.setEnabled(False)
                    dialog.aEDSemester.setCurrentIndex(1)
                    dialog.aEDSemester.setEnabled(False)
                    dialog.add_center_in_combobox()
                    dialog.aEDCenter.setCurrentText(f"{data[3]}")
                    dialog.aEDShift.setCurrentText(f"{data[4]}")
                    dialog.exec()
                else:
                    Common.show_message("Select Exam detail item!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in updating exam detail", str(e))
            finally:
                self.refresh_exam_detail_view()

        """
        def delete_exam_detail(self, exam_detail_select_criteria: tuple):
            success = Common().select_rows_based_on_criteria(self.outer_instance.aOSPISAllotmentRTTable,
                                                             exam_detail_select_criteria)
            if not success:
                return
            data = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentRTTable)
            if data:
                output = Common.show_message(f"Are sure want to delete Exam '{data[2]}'.", "YN")
                if output == QMessageBox.Yes:
                    success = self.outer_instance.query.delete_university_detail(data[0])
                    if success:
                        Common.show_message("Delete Successfully!", "I")
                    else:
                        Common.show_message("Failed to delete!", "I")
                    self.refresh_exam_detail_view()
                else:
                    Common.show_message("Delete Cancel!", "I")
            else:
                Common.show_message("Select Exam item!")
        """

    # -----------------end exam center function-------------

    # -----------------exam date function-------------
    class DateSheetManagement:
        """
        Class for managing exam date sheet.
        """

        def __init__(self, outer_instance):
            """
            Initialize DateSheetManagement instance.

            Args:
                outer_instance: Instance of the outer class.
            """
            self.outer_instance = outer_instance

        def allot_exam_date(self):
            """
            Allot exam date for selected exam detail.
            """
            try:
                exam_detail = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentRTTable)
                if exam_detail:
                    value = (exam_detail[0], exam_detail[1], exam_detail[2])
                    subject_date = self.outer_instance.query.get_subject_name_exam_date(value)
                    if subject_date:
                        exam_date = Common().get_table_data(self.outer_instance.aOSPISAllotmentRBTable, column=1)
                        if exam_date:
                            dialog = DateSheetDialog(usn=exam_detail[0], csn=exam_detail[1], semester=exam_detail[2],
                                                     place=exam_detail[3], shift=exam_detail[4],
                                                     subject_date=subject_date)
                            dialog.ui()
                            dialog.exec()
                        else:
                            Common.show_message("No exam date found!")
                    else:
                        Common.show_message("Subject date not available! Please allocate subject first.")
                else:
                    Common.show_message("Please select exam detail!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error while allotting exam date", str(e))
            finally:
                self.refresh_date_sheet_view()
                self.outer_instance.exam_allotment_manager.refresh_exam_detail_view()

        def refresh_date_sheet_view(self):
            """
            Refresh the date sheet view.
            """
            try:
                self.clear_selections()
                read_exam_detail = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentRTTable)
                if read_exam_detail:
                    value = (read_exam_detail[0], read_exam_detail[1], read_exam_detail[2])
                    read_subject_exam = self.outer_instance.query.get_subject_name_exam_date(value)
                    if read_subject_exam:
                        self.populate_date_sheet_table(read_subject_exam)
                    else:
                        self.outer_instance.aOSPISAllotmentRBTable.setRowCount(0)
                        Common.show_message("Date sheet does not exist! Please create one.")
                else:
                    self.outer_instance.aOSPISAllotmentRBTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_error_in_statusbar("Error loading date sheet", str(e))
            finally:
                self.outer_instance.aOSPISAllotmentRBTable.resizeColumnsToContents()

        def clear_selections(self):
            """
            Clear selections in the date sheet table.
            """
            if self.outer_instance.aOSPISAllotmentRBTable.selectedIndexes():
                self.outer_instance.aOSPISAllotmentRBTable.clearSelection()
                self.outer_instance.aOSPISAllotmentRBTable.selectionModel().clearCurrentIndex()

        def populate_date_sheet_table(self, date_sheets: list):
            """
            Populate the date sheet table with provided data.

            Args:
                date_sheets: List of tuples containing date sheet data.
            """
            self.outer_instance.aOSPISAllotmentRBTable.setRowCount(len(date_sheets))
            for row, date_sheet in enumerate(date_sheets):
                self.populate_date_sheet_row(row, date_sheet)

        def populate_date_sheet_row(self, row: int, date_sheet: tuple):
            """
            Populate a single row of the date sheet table with provided data.

            Args:
                row: Row index to populate.
                date_sheet: Tuple containing date sheet row data.
            """
            try:
                for col, value in enumerate(date_sheet):
                    item = QTableWidgetItem(str(value))
                    self.outer_instance.aOSPISAllotmentRBTable.setItem(row, col, item)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error populating date sheet row", str(e))

        def delete_exam_date(self):
            """
            Delete the selected exam date.
            """
            try:
                exam_detail = Common.get_selected_row_data(self.outer_instance.aOSPISAllotmentRTTable)
                if exam_detail:
                    exam_date = Common().get_table_data(self.outer_instance.aOSPISAllotmentRBTable, column=1)
                    if exam_date:
                        if exam_date[0][0] != "None":
                            output = Common.show_message(
                                f"Are you sure you want to delete the exam for '{exam_detail[0]}, {exam_detail[1]}, {exam_detail[2]}'?",
                                "YN")
                            if output == QMessageBox.Yes:
                                exam_detail_tup = (exam_detail[0], exam_detail[1], exam_detail[2])
                                # exam_detail_lst = [(exam_detail[3], item[0], exam_detail[4]) for item in exam_date]
                                success = self.outer_instance.query.delete_exam_date_detail(exam_detail_tup)
                                if success:
                                    Common.show_message("Exam date sheet and Journey deleted successfully!.")
                                else:
                                    Common.show_message("Failed to delete!", "C")
                            else:
                                Common.show_message("Deletion canceled!", "I")
                        else:
                            Common.show_message("No exam date to delete!", "I")
                    else:
                        Common.show_message("No data found!", "I")
                else:
                    Common.show_message("Please select an exam detail.")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in deleting exam date", str(e))
            finally:
                self.refresh_date_sheet_view()
                self.outer_instance.exam_allotment_manager.refresh_exam_detail_view()

    # -------------end exam date allotment----------------------

    # ---------------------Journey_detail---------------------
    class JourneyManagement:
        """Manages the journey-related operations within a GUI application.

        This class handles the creation, display, update, and deletion of journeys in a table view,
        Interfacing with the main application components through the `outer_instance`.

        Attributes:
            outer_instance (object): A reference to the main application window containing UI components and data access layers.
        """

        def __init__(self, outer_instance):
            """Initializes the JourneyManager with a reference to the outer application instance.

            Args:
                outer_instance: The instance of the main or parent component of the application.
            """
            self.outer_instance = outer_instance

        def create_other_journey(self):
            """Creates a new journey entry via a dialog and refreshes the journey view."""
            try:
                dialog = NewJourney()
                dialog.ui()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in opening", str(e))
            finally:
                self.refresh_journey_view()

        def refresh_journey_view(self):
            """Refreshes the journey view by clearing selections and updating the table data."""
            try:
                self.clear_selections()
                journeys = self.outer_instance.query.get_journey_detail()
                if journeys:
                    self.populate_journey_table(journeys)
                else:
                    self.outer_instance.aOSPISJViewTable.setRowCount(0)
                    self.outer_instance.show_message_in_statusbar("Journey not exist", str(""))
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing journeys: " + str(e))
            finally:
                self.outer_instance.aOSPISJViewTable.resizeColumnsToContents()

        def clear_selections(self):
            """Clears any selected rows and the current index in the journey view table."""
            if self.outer_instance.aOSPISJViewTable.selectedIndexes():
                self.outer_instance.aOSPISJViewTable.clearSelection()
                self.outer_instance.aOSPISJViewTable.selectionModel().clearCurrentIndex()

        def populate_journey_table(self, journeys: list):
            """Populates the journey table with the given list of journeys.

            Args:
                journeys (list): A list of journey tuples to display in the table.
            """
            self.outer_instance.aOSPISJViewTable.setRowCount(len(journeys))
            for row, journey in enumerate(journeys):
                self.populate_journey_row(row, journey)

        def populate_journey_row(self, row: int, journey: tuple):
            """Fills in a row in the journey table with details from a journey tuple.

            Args:
                row (int): The row index in the table where the journey details will be set.
                journey (tuple): A tuple containing journey data for one entry.
            """
            for col, value in enumerate(journey):
                if col != 6:
                    item = QTableWidgetItem(str(value))
                    self.outer_instance.aOSPISJViewTable.setItem(row, col, item)
            self.add_controls(row, journey[0])

        def add_controls(self, row, journey_id: int):
            """Adds control buttons to a row in the journey table for editing and deleting the journey.

            Args:
                row (int): The row index to which the buttons are added.
                journey_id (int): The ID of the journey corresponding to the row.
            """
            widget = ThreeBtnWidget()
            if self.outer_instance.aOSPISJViewTable.item(row, 5).text() == "exam":
                widget.firstEditBtn.setVisible(False)
                widget.secondDeleteBtn.setVisible(False)
            else:
                widget.firstEditBtn.clicked.connect(lambda: self.update_journey_detail(journey_id))
                widget.secondDeleteBtn.clicked.connect(lambda: self.delete_journey_detail(journey_id))
            self.outer_instance.aOSPISJViewTable.setCellWidget(row, 6, widget)

        def update_journey_detail(self, journey_id: int):
            """Initiates the process to update details of a specific journey.

            Args:
                journey_id (int): The ID of the journey to be updated.
            """
            try:
                for row in range(self.outer_instance.aOSPISJViewTable.rowCount()):
                    if self.outer_instance.aOSPISJViewTable.item(row, 0).text() == str(journey_id):
                        self.outer_instance.aOSPISJViewTable.selectRow(row)
                        break
                dialog = NewJourney(use_type="update", journey_id=journey_id)
                dialog.ui()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in updating journey", str(e))
            finally:
                self.refresh_journey_view()

        def delete_journey_detail(self, journey_id: int):
            """Initiates the deletion of a journey based on its ID, with user confirmation.

            Args:
                journey_id (int): The ID of the journey to be deleted.
            """
            try:
                for row in range(self.outer_instance.aOSPISJViewTable.rowCount()):
                    if self.outer_instance.aOSPISJViewTable.item(row, 0).text() == str(journey_id):
                        self.outer_instance.aOSPISJViewTable.selectRow(row)
                        break
                data = Common.get_selected_row_data(self.outer_instance.aOSPISJViewTable)
                if data:
                    output = Common.show_message(
                        f"Are sure want to delete Journey of '{data[0]}, {data[1]}, {data[2]}'.",
                        "YN")
                    if output == QMessageBox.Yes:
                        if self.outer_instance.query.delete_journey_detail_j_id(journey_id):
                            Common.show_message("Journey Deleted Successfully!")
                    else:
                        Common.show_message("Delete Cancel", "I")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in Deleting Journey", str(e))
            finally:
                self.refresh_journey_view()

    # ---------------------Journey_detail---------------------
    # ------------------End inner stack widget implement------------

    # --------------End of admin---------------------------
    # ------------------------user/staff-----------------------
    class StudentManagement:
        """
        Class for managing student data and interacting with the GUI.
        """

        def __init__(self, outer_instance):
            """
            Initialize the StudentManagement instance.

            Args:
                outer_instance: The outer instance (presumably the main application window).
            """
            self.outer_instance = outer_instance
            self.preview_dialog = None

        def print_table(self):
            self.preview_dialog = PrintPreviewDialog(self.outer_instance.uOSPMIStudentViewTable)
            self.preview_dialog.print_preview()

        def add_in_combobox(self):
            """
            Add items to combo boxes for university and course selection.
            """
            # Fetch university and course data from queries
            try:
                university = self.outer_instance.query.get_university_short_name()
                course = self.outer_instance.query.get_course_short_name()

                # Clear existing items and add default item to combo boxes
                self.outer_instance.uOSPMISSFUniversity.clear()
                self.outer_instance.uOSPMISSFUniversity.addItem("Select University")
                self.outer_instance.uOSPMISSFCourse.clear()
                self.outer_instance.uOSPMISSFCourse.addItem("Select Course")

                # Add fetched data to combo boxes if available
                if university:
                    self.outer_instance.uOSPMISSFUniversity.addItems([str(i[0]) for i in university])
                if course:
                    self.outer_instance.uOSPMISSFCourse.addItems([str(i[0]) for i in course])
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in populating combobox", str(e))

        def clear_filter(self):
            """
            Clear the selection filters.
            """
            # Reset combo box selections and date to current date
            try:
                self.outer_instance.uOSPMISSFUniversity.setCurrentIndex(0)
                self.outer_instance.uOSPMISSFCourse.setCurrentIndex(0)
                self.outer_instance.uOSPMISSFSemester.setCurrentIndex(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in Clearing filter", str(e))

        def filter_table(self, index):
            """
            Filter the table data based on the selected options in the combo boxes and the selected date.

            Args:
                index: The index of the selected item in the combo box.
            """
            try:
                item1 = self.outer_instance.uOSPMISSFUniversity.currentText()
                item2 = self.outer_instance.uOSPMISSFCourse.currentText()
                item3 = self.outer_instance.uOSPMISSFSemester.currentText()

                for row in range(self.outer_instance.uOSPMIStudentViewTable.rowCount()):
                    item_texts = [self.outer_instance.uOSPMIStudentViewTable.item(row, i).text() for i in
                                  range(4, 7)]

                    match1 = item1 == "Select University" or item_texts[0] == item1
                    match2 = item2 == "Select Course" or item_texts[1] == item2
                    match3 = item3 == "Select Semester" or item_texts[2] == item3

                    self.outer_instance.uOSPMIStudentViewTable.setRowHidden(row, not (match1 and match2 and match3))
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in Filtering", str(e))

        def add_student(self):
            """
            Add a new student record.

            Opens a dialog for adding a new student, then refreshes the student view.
            """
            try:
                dialog = StudentDialog()
                dialog.ui()
                dialog.exec()
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in opening add student dialog", str(e))
            finally:
                self.refresh_student_view()

        def refresh_student_view(self):
            """
            Refreshes the student view table with the latest data.

            Retrieves student details, populates the table if data exists,
            and handles exceptions.
            """
            try:
                self.clear_selections()
                read_student = self.outer_instance.query.get_student_detail()
                if read_student:
                    self.populate_student_table(read_student)
                else:
                    self.outer_instance.uOSPMIStudentViewTable.setRowCount(0)
                    self.outer_instance.show_message_in_statusbar("Student detail not exist, Create one!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing Student: " + str(e))
            finally:
                self.outer_instance.uOSPMIStudentViewTable.resizeColumnsToContents()

        def clear_selections(self):
            """
            Clears any selected rows and the current index in the student view table.
            """
            if self.outer_instance.uOSPMIStudentViewTable.selectedIndexes():
                self.outer_instance.uOSPMIStudentViewTable.clearSelection()
                self.outer_instance.uOSPMIStudentViewTable.selectionModel().clearCurrentIndex()

        def populate_student_table(self, students: list):
            """
            Populates the student view table with the provided list of students.

            Args:
                students: A list of student details.
            """
            self.outer_instance.uOSPMIStudentViewTable.setRowCount(len(students))
            for row, student in enumerate(students):
                self.populate_student_row(row, student)

        def populate_student_row(self, row: int, student: tuple):
            """
            Populates a single row in the student view table with the data from a student tuple.

            Args:
                row: The row index.
                student: A tuple containing student details.
            """
            for col, value in enumerate(student):
                item = QTableWidgetItem(str(value))
                self.outer_instance.uOSPMIStudentViewTable.setItem(row, col, item)
            self.add_controls(row, student[0])

        def add_controls(self, row, student_roll_no: str):
            """
            Adds control widgets (buttons) for each student row in the table.

            Args:
                row: The row index.
                student_roll_no: The roll number of the student.
            """
            widget = ThreeBtnWidget()
            widget.firstEditBtn.clicked.connect(lambda: self.update_student_detail(student_roll_no))
            widget.secondDeleteBtn.clicked.connect(lambda: self.delete_student_detail(student_roll_no))
            self.outer_instance.uOSPMIStudentViewTable.setCellWidget(row, 7, widget)

        def update_student_detail(self, student_roll_no: str):
            """
            Update the details of a student with the provided roll number.

            Args:
                student_roll_no: The roll number of the student.
            """
            try:
                for row in range(self.outer_instance.uOSPMIStudentViewTable.rowCount()):
                    if self.outer_instance.uOSPMIStudentViewTable.item(row, 0).text() == str(student_roll_no):
                        self.outer_instance.uOSPMIStudentViewTable.selectRow(row)
                        break
                data = Common.get_selected_row_data(self.outer_instance.uOSPMIStudentViewTable)
                if data:
                    dialog = StudentDialog(use_type="update", roll_no=data[0])
                    dialog.ui()
                    dialog.set_values(data[1], data[2], data[3], data[4], data[5], data[6])
                    dialog.exec()
                else:
                    Common.show_message("Select Student!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar(f"Error in Updating student", str(e))
            finally:
                self.refresh_student_view()

        def delete_student_detail(self, student_roll_no: str):
            """
            Delete the details of a student with the provided roll number.

            Args:
                student_roll_no: The roll number of the student.
            """
            try:
                for row in range(self.outer_instance.uOSPMIStudentViewTable.rowCount()):
                    if self.outer_instance.uOSPMIStudentViewTable.item(row, 0).text() == str(student_roll_no):
                        self.outer_instance.uOSPMIStudentViewTable.selectRow(row)
                        break

                data = Common.get_selected_row_data(self.outer_instance.uOSPMIStudentViewTable)
                if data:
                    output = Common.show_message(f"Are sure want to delete Student, Roll Number:-'{data[0]}'.", "YN")
                    if output == QMessageBox.Yes:
                        success = self.outer_instance.query.delete_student_detail(data[0])
                        if success:
                            Common.show_message("Delete Successfully!", "I")
                        else:
                            Common.show_message("Failed to delete!", "C")
                    else:
                        Common.show_message("Delete Cancel!", "I")
                else:
                    Common.show_message("Select Student!")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in Deleting student detail", str(e))
            finally:
                self.refresh_student_view()

    class StudentFeeReceiptManagement:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def refresh_student_fee_receipt(self):
            try:
                success = self.outer_instance.query.get_receipt_detail()
                if success:
                    self.populate_student_fee_table(success)
                else:
                    self.outer_instance.uOSPMIFeeDetailViewTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing receipt", str(e))
            finally:
                self.outer_instance.uOSPMIFeeDetailViewTable.resizeColumnsToContents()

        def populate_student_fee_table(self, fee_receipts: list):
            self.outer_instance.uOSPMIFeeDetailViewTable.setRowCount(len(fee_receipts))
            for row, fee_receipt in enumerate(fee_receipts):
                self.populate_student_fee_row(row, fee_receipt)

        def populate_student_fee_row(self, row: int, fee_receipt: tuple):
            for col, value in enumerate(fee_receipt):
                item = QTableWidgetItem(str(value))
                self.outer_instance.uOSPMIFeeDetailViewTable.setItem(row, col, item)
            self.add_controls(row, fee_receipt[0])

        def add_controls(self, row, receipt_no: str):
            widget = ThreeBtnWidget()
            widget.firstEditBtn.hide()
            widget.firstEditBtn.setDisabled(True)
            widget.secondDeleteBtn.clicked.connect(lambda: self.delete_fee_receipt(receipt_no))
            self.outer_instance.uOSPMIFeeDetailViewTable.setCellWidget(row, 5, widget)

        def delete_fee_receipt(self, receipt_no: str):
            try:
                for row in range(self.outer_instance.uOSPMIFeeDetailViewTable.rowCount()):
                    if self.outer_instance.uOSPMIFeeDetailViewTable.item(row, 0).text() == str(receipt_no):
                        self.outer_instance.uOSPMIFeeDetailViewTable.selectRow(row)
                        break
                data = Common.get_selected_row_data(self.outer_instance.uOSPMIFeeDetailViewTable)
                if data:
                    output = Common.show_message(f"Are sure want to delete fee of '{data[0]}, {data[1]}'.",
                                                 "YN")
                    if output == QMessageBox.Yes:
                        if self.outer_instance.query.delete_fee_journey_and_fee_detail(data[0]):
                            Common.show_message("Fee Deleted Successfully!", "I")
                        else:
                            Common.show_message("Error in deleting!", "C")
                    else:
                        Common.show_message("Delete Cancel", "I")
                else:
                    Common.show_message("Select item to delete")
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in deleting fee receipt", str(e))
            finally:
                self.refresh_student_fee_receipt()

    class StudentJourneyManagement:
        """
        Class to manage student journey data in a PyQt application.

        This class provides methods to handle various operations related to student journey management,
        including filtering data, reading fee receipts and roll numbers, populating tables, and more.
        """

        def __init__(self, outer_instance):
            """
            Initialize the StudentJourneyManagement class.

            Args:
                outer_instance: The instance of the outer class.
            """
            self.outer_instance = outer_instance
            self.preview_dialog = None

        def print_table(self):
            self.preview_dialog = PrintPreviewDialog(self.outer_instance.uOSPMIStudentJourneyViewTable)
            self.preview_dialog.print_preview()

        def add_in_combobox(self):
            """
            Add items to combo boxes for university and course selection.
            """
            # Fetch university and course data from queries
            try:
                university = self.outer_instance.query.get_university_short_name()
                course = self.outer_instance.query.get_course_short_name()

                # Clear existing items and add default item to combo boxes
                self.outer_instance.uOSPMISJFUniversity.clear()
                self.outer_instance.uOSPMISJFUniversity.addItem("Select University")
                self.outer_instance.uOSPMISJFCourse.clear()
                self.outer_instance.uOSPMISJFCourse.addItem("Select Course")

                # Add fetched data to combo boxes if available
                if university:
                    self.outer_instance.uOSPMISJFUniversity.addItems([str(i[0]) for i in university])
                if course:
                    self.outer_instance.uOSPMISJFCourse.addItems([str(i[0]) for i in course])
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in populating in combobox", str(e))

        def clear_filter(self):
            """
            Clear the selection filters.
            """
            # Reset combo box selections and date to current date
            try:
                self.outer_instance.uOSPMISJFUniversity.setCurrentIndex(0)
                self.outer_instance.uOSPMISJFCourse.setCurrentIndex(0)
                self.outer_instance.uOSPMISJFSemester.setCurrentIndex(0)
                self.outer_instance.uOSPMISJFDate.setDate(QDate.currentDate())
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in clearing filtering", str(e))

        def filter_table(self, index):
            """
            Filter the table data based on the selected options in the combo boxes and the selected date.

            Args:
                index: The index of the selected item in the combo box.
            """
            try:
                item1 = self.outer_instance.uOSPMISJFUniversity.currentText()
                item2 = self.outer_instance.uOSPMISJFCourse.currentText()
                item3 = self.outer_instance.uOSPMISJFSemester.currentText()
                selected_date = self.outer_instance.uOSPMISJFDate.date()
                current_date = QDate.currentDate()

                for row in range(self.outer_instance.uOSPMIStudentJourneyViewTable.rowCount()):
                    item_texts = [self.outer_instance.uOSPMIStudentJourneyViewTable.item(row, i).text() for i in
                                  range(2, 5)]

                    # Check if the date column exists
                    date_item = self.outer_instance.uOSPMIStudentJourneyViewTable.item(row, 6)
                    if date_item is not None:
                        row_date = QDate.fromString(date_item.text(), Qt.ISODate)
                        match_date = selected_date == row_date
                    else:
                        match_date = False

                    match1 = item1 == "Select University" or item_texts[0] == item1
                    match2 = item2 == "Select Course" or item_texts[1] == item2
                    match3 = item3 == "Select Semester" or item_texts[2] == item3

                    if selected_date == current_date:
                        self.outer_instance.uOSPMIStudentJourneyViewTable.setRowHidden(row,
                                                                                       not (
                                                                                                   match1 and match2 and match3))
                    else:
                        self.outer_instance.uOSPMIStudentJourneyViewTable.setRowHidden(row, not (
                                match1 and match2 and match3 and match_date))
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in filtering", str(e))

        def read_fee_receipt(self):
            """
            Read fee receipt data from the database.

            Returns:
                The fetched fee receipt data.
            """
            try:
                receipt_no = self.outer_instance.query.get_receipt_no()
                if receipt_no:
                    return receipt_no
                else:
                    self.outer_instance.uOSPMIStudentJourneyViewTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in fetching fee receipt", str(e))

        def read_roll_no(self):
            """
            Read roll number data from the database.

            Returns:
                The fetched roll number data.
            """
            try:
                roll_no = self.outer_instance.query.get_receipt_roll_no()
                if roll_no:
                    return roll_no
                else:
                    self.outer_instance.uOSPMIStudentJourneyViewTable.setRowCount(0)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in fetching student roll number", str(e))

        def read_journey_id_detail(self, fee_journey: tuple):
            """
            Read journey ID detail from the database based on a fee journey tuple.

            Args:
                fee_journey: A tuple containing fee journey details.

            Returns:
                The fetched journey ID detail.
            """
            try:
                data = []
                journey_id = self.outer_instance.query.get_fee_journey_id(fee_journey)
                for i in journey_id:
                    fee_journey_lst = [fee_journey[0], fee_journey[1]]
                    data.append(tuple(fee_journey_lst + self.read_to_date_shift(i[0])))
                return data
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in fetching journey id", str(e))

        def read_to_date_shift(self, journey_id: str):
            """
            Read journey to date shift from the database based on journey ID.

            Args:
                journey_id: The journey ID.

            Returns:
                The fetched journey to date shift.
            """
            try:
                journey_to_date_shift = self.outer_instance.query.get_journey_detail_j_id(journey_id)
                return list(journey_to_date_shift)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in fetching Journey detail", str(e))

        def read_university_course_semester(self, roll_no: str):
            """
            Read university, course, and semester data from the database based on roll number.

            Args:
                roll_no: The roll number.

            Returns:
                The fetched university, course, and semester data.
            """
            try:
                student_detail = self.outer_instance.query.get_student_ucs_of_roll_no(roll_no)
                return student_detail
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in fetching student detail", str(e))

        def refresh_student_journey_view(self):
            """
            Refresh the student journey view.

            This method fetches relevant data from various sources, populates the table accordingly, and adjusts column sizes.
            """
            try:
                journeys = []
                receipt_no = self.read_fee_receipt()
                roll_no = self.read_roll_no()
                receipt_no_roll_on = [(receipt_no[i][0], roll_no[i][0]) for i in range(len(receipt_no))]
                for i in receipt_no_roll_on:
                    j_detail = self.read_journey_id_detail(i)
                    for detail in j_detail:
                        student_detail = self.read_university_course_semester(detail[1])
                        detail = list(detail)
                        for k, value in enumerate(student_detail):
                            detail.insert(k + 2, value)
                        tuple(detail)
                        journeys.append(detail)
                if journeys:
                    self.populate_student_journey_table(journeys)
            except Exception as e:
                self.outer_instance.show_message_in_statusbar("Error in refreshing Student journey", str(e))
            finally:
                self.outer_instance.uOSPMIStudentJourneyViewTable.resizeColumnsToContents()

        def populate_student_journey_table(self, journeys: list):
            """
            Populate the student journey table with data.

            Args:
                journeys: A list of tuples containing journey data.
            """
            self.outer_instance.uOSPMIStudentJourneyViewTable.setRowCount(len(journeys))
            for row, journey in enumerate(journeys):
                self.populate_student_journey_row(row, journey)

        def populate_student_journey_row(self, row: int, journey: tuple):
            """
            Populate a single row of the student journey table with data.

            Args:
                row: The row index.
                journey: A tuple containing journey data.
            """
            for col, value in enumerate(journey):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.outer_instance.uOSPMIStudentJourneyViewTable.setItem(row, col, item)

    def book_transport(self):
        dialog = BookTransportUI(self)
        dialog.init_ui()
        dialog.exec()


class SplashScreen(QMainWindow):
    TIMER_INTERVAL = 500
    COMPLETION_THRESHOLD = 100

    def __init__(self):
        super().__init__()
        self.ui = splashScreen()
        self.ui.setupUi(self)

        self.ui.title.setText("<p><span style='font-weight:700; color:#9b9bff;'>Your</span> "
                              "Transport Management<br>System</p>")

        self.progress_value = 0
        self.update_progress_bar_value()
        self.internet_connected = False
        self.database_connected = False
        self.timer = QTimer(self)
        self.networkMonitor = NetworkMonitor(parent=self)

        self.setup_window_flags()
        self.setup_shadow_effect()

        self.setup_timer()

    def setup_window_flags(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def setup_shadow_effect(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(shadow)

    def setup_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(self.TIMER_INTERVAL)

    @Slot()
    def progress(self):
        self.check_internet_connection()

        if self.internet_connected:
            self.progress_value += 10
        else:
            self.progress_value = 0

        if self.progress_value == 50:
            self.check_database_connection()
            if not self.database_connected:
                Common.show_message("Incorrect Database credential!.")
                exit(1)
            else:
                _query = Query()
                _query.create_all_table()

        if self.progress_value > self.COMPLETION_THRESHOLD:
            self.timer.stop()
            self.close()
            self.open_main_app()

        self.update_progress_bar_value()

    def check_internet_connection(self):
        internet_connection = self.networkMonitor.check_connection()
        self.internet_connected = internet_connection

    def check_database_connection(self):
        _query = Query()
        # Check the database connection status again
        if _query.check_is_connected():
            self.database_connected = True
        else:
            self.database_connected = False

    def update_progress_bar_value(self):
        progress = (self.COMPLETION_THRESHOLD - self.progress_value) / 100.0
        stop1 = progress - 0.001
        stop2 = progress

        progress_style = """QFrame{
                border-radius: 150px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:%1 rgba(255, 0, 127, 0), stop:%2 rgba(85, 170, 255, 255));
                }
                """.replace("%1", str(stop1)).replace("%2", str(stop2))

        self.ui.circularProgress.setStyleSheet(progress_style)

        percentage_style = f"""
        <p><span style=" font-size:68pt;">{int(self.progress_value)}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>
        """
        self.ui.percentage.setText(percentage_style)

    @staticmethod
    def open_main_app():
        window = MainApp()
        window.show()


def main():
    import sys
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
