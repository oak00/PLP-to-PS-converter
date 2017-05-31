def determineCourseChanges(str):

    if 'bucktown' in str:
        changes = {
            'History 6' : '4910SS_06',
            'Math 6' : '4910Math_06',
            'English 6' : '4910Read_06',
            'Science 6' : '4910Science_06',
            'History 7' : '4910SS_07',
            'Math 7' : '4910Math_07',
            'English 7' : '4910Read_07',
            'Science 7' : '4910Science_07',
            'History 8' : '4910SS_08',
            'Math 8' : '4910Math_08',
            'English 8' : '4910Read_08',
            'Science 8' : '4910Science_08'
            }
        return changes
    elif 'irving park' in str:
        changes = {
            'History 6' : '4913CK_6',
            'Math 6' : '4913Math_6',
            'English 6' : '4913ELA_6',
            'Science 6' : '4913Sci_6',
            'History 7' : '4913CK_7',
            'Math 7' : '4913Math_7',
            'English 7' : '4913ELA_7',
            'Science 7' : '4913Sci_7',
            'History 8' : '4913CK_8',
            'Math 8' : '4913Math_8',
            'English 8' : '4913ELA_8',
            'Science 8' : '4913Sci_8'
            }
        return changes
    elif 'prairie' in str:
        changes = {
            'History 6' : '4220SS_06',
            'Math 6' : '4220Math_06',
            'English 6' : '4220Read_06',
            'Science 6' : '4220Sci_06',
            'History 7' : '4220SS_07',
            'Math 7' : '4220Math_07',
            'English 7' : '4220Read_07',
            'Science 7' : '4220Sci_07',
            'History 8' : '4220SS_08',
            'Math 8' : '4220Math_08',
            'English 8' : '4220Read_08',
            'Science 8' : '4220Sci_08'
            }
        return changes
    elif 'west belden' in str:
        changes = {
            'History 6' : '7120SS_06',
            'Math 6' : '7120Math_06',
            'English 6' : '7120Read_06',
            'Science 6' : '7120Sci_06',
            'History 7' : '7120SS_07',
            'Math 7' : '7120Math_07',
            'English 7' : '7120Read_07',
            'Science 7' : '7120Sci_07',
            'History 8' : '7120SS_08',
            'Math 8' : '7120Math_08',
            'English 8' : '7120Read_08',
            'Science 8' : '7120Sci_08'
            }
        return changes
    else:
        print("Changes were unable to be made")
        return changes


def returnCourseName(str):
    courseName = "";
    if 'SS' in str:
        courseName = 'History'
    elif 'CK' in str:
        courseName = 'History'
    elif 'Math' in str:
        courseName = 'Math'
    elif 'Read' in str:
        courseName = 'Language Arts'
    elif 'ELA' in str:
        courseName = 'Language Arts'
    elif 'Science' in str:
        courseName = 'Science'
    else:
        courseName = "Null"
        
    return courseName;


def returnGrade(str):
    grade = "";
    if int(str) >= 97:
        grade = "A+"
    elif int(str) >= 93 and int(str) <= 96:
        grade = "A"
    elif int(str) >= 90 and int(str) <= 92:
        grade = "A-"
    elif int(str) >= 87 and int(str) <= 89:
        grade = "B+"
    elif int(str) >= 83 and int(str) <= 86:
        grade = "B"
    elif int(str) >= 80 and int(str) <= 82:
        grade = "B-"
    elif int(str) >= 77 and int(str) <= 79:
        grade = "C+"
    elif int(str) >= 73 and int(str) <= 76:
        grade = "C"
    elif int(str) >= 70 and int(str) <= 72:
        grade = "C-"
    elif int(str) >= 60 and int(str) <= 69:
        grade = "D"
    else:
        grade = "F"
        
    return grade;

def returnTermId(str1, str2):
    prefix = "";
    suffix = "";

    if str1 == "2016":
        prefix = "26"
    elif str1 == "2017":
        prefix = "27"        
    elif str1 == "2018":
        prefix = "28"        
    elif str1 == "2019":
        prefix = "29"
    else:
        prefix = "Null"

    if str2 == "Q1":
        suffix = "01"
    elif str2 == "Q2":
        suffix = "02"
    elif str2 == "Q3":
        suffix = "03"        
    elif str2 == "Q4":
        suffix = "04"
    else:
        suffix = "Null"

    return prefix + suffix

def returnSchoolName(str):
    schoolName = "";
    if 'bucktown' in str:
        schoolName = "Bucktown"
    elif 'irving park' in str:
        schoolName = "Irving Park"
    elif 'prairie' in str:
        schoolName = "Prairie"
    elif 'west belden' in str:
        schoolName = "West Belden"
    else:
        schoolName = "Null"
        
    return schoolName

def returnSchoolId(str):
    schoolId = "";
    if 'bucktown' in str:
        schoolId = "4910"
    elif 'irving park' in str:
        schoolId = "4913"
    elif 'prairie' in str:
        schoolId = "4220"
    elif 'west belden' in str:
        schoolId = "7120"
    else:
        schoolId = "Null"
        
    return schoolId

def returnGradeLevel(str):
    gradeLevel = "";
    if "glt6" in str:
        gradeLevel = "6"
    elif "glt7" in str:
        gradeLevel = "7"
    elif "glt8" in str:
        gradeLevel = "8"
    else:
        gradeLevel = "Null"
        
    return gradeLevel
                    
