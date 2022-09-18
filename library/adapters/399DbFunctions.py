import os
import sqlite3
import time

sqliteConnection = sqlite3.connect(os.path.abspath(os.getcwd()) + "\\data\\399courses.db")
cursor = sqliteConnection.cursor()

def return_all_courses():
    a = cursor.execute("select * from course")
    course = a.fetchall()
    newlist = []
    for x in course:
        newlist.append((x[0],x[1]))
    return newlist

def return_isolated_problems_with_course(course_subject, course_number):
    a = cursor.execute("select * from course where subject = ? and courseNumber = ?", (course_subject, course_number))
    if len(a.fetchall()) == 1:
        course = a.fetchall()[0]
        return course[8:]
    else:
        return "does not exist"

def return_course_desc(course_subject, course_number):
    a = cursor.execute("select * from course where subject = ? and courseNumber = ?", (course_subject, course_number))
    list_of_courses = a.fetchall()
    if len(list_of_courses) == 1:
        course = list_of_courses[0]
        return course[7]
    else:
        return "does not exist"

def return_course_points(course_subject, course_number):
    a = cursor.execute("select * from course where subject = ? and courseNumber = ?", (course_subject, course_number))
    if len(a.fetchall()) == 1:
        course = a.fetchall()[0]
        return course[3]
    else:
        return "does not exist"

def problems_with_timetable(timetable):
    #the timetable is given as a list of all subjects done in (y1S1, y1S2, y2s1, y2s2) 