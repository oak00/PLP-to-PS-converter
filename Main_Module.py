import csv
import os
import Module_Methods

#Global Data Structures
newRows = []
finalRows = []
changes = {}
files = os.listdir()

#User Input
storeCode = input("Please enter the term (Q1, T2, etc):")
year = input("Please enter the school year (2016-2017 would just be 2016 for example):")


def determineFile(list):

    csvName = ""
    if 'glt6-cics bucktown-by_course.csv' in files:
        csvName = 'glt6-cics bucktown-by_course.csv'
    elif 'glt7-cics bucktown-by_course.csv' in files:
        csvName = 'glt7-cics bucktown-by_course.csv'
    elif 'glt8-cics bucktown-by_course.csv' in files:
        csvName = 'glt8-cics bucktown-by_course.csv'
    elif 'glt6-cics irving park-by_course.csv' in files:
        csvName = 'glt6-cics irving park-by_course.csv'
    elif 'glt7-cics irving park-by_course.csv' in files:
        csvName = 'glt7-cics irving park-by_course.csv'
    elif 'glt8-cics irving park-by_course.csv' in files:
        csvName = 'glt8-cics irving park-by_course.csv'
    elif 'glt6-cics prairie-by_course.csv' in files:
        csvName = 'glt6-cics prairie-by_course.csv'
    elif 'glt7-cics prairie-by_course.csv' in files:
        csvName = 'glt7-cics prairie-by_course.csv'
    elif 'glt8-cics prairie-by_course.csv' in files:
        csvName = 'glt8-cics prairie-by_course.csv'
    elif 'glt6-cics west belden-by_course.csv' in files:
        csvName = 'glt6-cics west belden-by_course.csv'
    elif 'glt7-cics west belden-by_course.csv' in files:
        csvName = 'glt7-cics west belden-by_course.csv'
    elif 'glt8-cics west belden-by_course.csv' in files:
        csvName = 'glt8-cics west belden-by_course.csv'
    else:
        print("File Not Found")
    return csvName



def formatRow(list):
    newRow = []

    studentId = list.pop(0)
    course = list.pop(4)
    percent = list.pop(21)
    
    newRow.append(studentId)
    newRow.append(Module_Methods.returnCourseName(course))
    newRow.append(course)
    newRow.append("0")
    newRow.append(Module_Methods.returnGrade(percent))
    newRow.append("0")
    newRow.append(storeCode)
    newRow.append(Module_Methods.returnTermId(year, storeCode))
    newRow.append("0")
    newRow.append(percent)
    newRow.append(Module_Methods.returnSchoolName(csvName))
    newRow.append(Module_Methods.returnGradeLevel(csvName))
    newRow.append("")
    newRow.append("")
    newRow.append(Module_Methods.returnSchoolId(csvName))
    
    return newRow



#csv file
csvName = determineFile(files);


with open(csvName) as csvfile:
    
    changes = Module_Methods.determineCourseChanges(csvName) #Determine which school the data is from and change course numbers accordingly
    reader = csv.reader(csvfile) #Start reading the csv
    next(reader, None) #Skip header
    for row in reader:

        newRow = row
        
        for key, value in changes.items():
            newRow = [x.replace(key, value) for x in newRow]
        
        finalRows.append(formatRow(newRow))
        

with open('grade_import.csv','w') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerow(["Student Number", "Course Name", "Course Number", "EarnedCrHrs", "Grade", "PotentialCrHrs", "Storecode", "Termid", "GPA Points", "Percent", "SchoolName", "Grade_Level", "Credit Type", "Teacher Name", "Schoolid", "ExcludeFromGPA", "ExcludeFromClassRank", "ExcludeFromHonorRoll"])							
    writer.writerows(finalRows)



    
    
