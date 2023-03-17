#include "grade_school.h"

void init_roster(roster_t *roster)
{
    roster->count = 0;
    for (int i = 0; i < MAX_STUDENTS; i++)
    {
        roster->students[i].grade = 0;
    }
}

bool add_student(roster_t *roster, char name[MAX_NAME_LENGTH], uint8_t grade)
{
    // Copy grade to student struct
    student_t student = {.grade = grade};
    
    // Copy name to student struct
    for (int i = 0; i < MAX_NAME_LENGTH; i++)
    {
        student.name[i] = name[i];
    }
    
    // Check if valid
    for (size_t i = 0; i < roster->count; i++)
    {
        if (!strcasecmp(student.name, roster->students[i].name))
        {
            // Invalid if name already in roster
            return false;
        }
    }

    // Add students
    roster->students[roster->count] = student;
    roster->count++;

    sort(roster);

    return true;
}

roster_t get_grade(roster_t *roster, uint8_t grade)
{
    roster_t roster_grade;
    init_roster(&roster_grade);

    for (size_t i = 0; i < roster->count; i++)
    {
        if (roster->students[i].grade == grade)
        {
            roster_grade.students[roster_grade.count] = roster->students[i];
            roster_grade.count++;
        }
    }
    return roster_grade;
}

void sort(roster_t *roster)
{ 
    // Sort by grade
    int swap = -1;
    while (swap != 0)
    {
        swap = 0;
        for (size_t i = 0; i < roster->count - 1; i++)
        {    
            if (roster->students[i].grade > roster->students[i + 1].grade) 
            {
                roster_t temp;
                init_roster(&temp);
                temp.students[0] = roster->students[i];
                roster->students[i] = roster->students[i + 1];
                roster->students[i + 1] = temp.students[0];
                swap++;
            }
        }
    }

    // Sort by name
    swap = -1;
    while (swap != 0)
    {
        swap = 0;
        for (size_t i = 0; i < roster->count - 1; i++)
        {    
            if (roster->students[i + 1].grade == roster->students[i].grade && strcasecmp(roster->students[i + 1].name, roster->students[i].name) < 0 )
            {
                roster_t temp;
                init_roster(&temp);
                temp.students[0] = roster->students[i];
                roster->students[i] = roster->students[i + 1];
                roster->students[i + 1] = temp.students[0];
                swap++;
            }
        }
    }
}
