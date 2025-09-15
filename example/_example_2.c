#include "hindi.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME 50
#define MAX_STUDENTS 5
#define MAX_SUBJECTS 4

बनाओ अनुक्रम
{
    अक्षर name[MAX_NAME];
    पूरा marks[MAX_SUBJECTS];
    दायमिक average;
}
Student;

दायमिक calculate_average(पूरा marks[], पूरा n)
{
    पूरा sum = 0;
    के_लिए(पूरा i = 0; i < n; i++)
    {
        sum += marks[i];
    }
    लौटाओ sum / (दायमिक)n;
}

पूरा मुख्य()
{
    Student students[MAX_STUDENTS];

    के_लिए(पूरा i = 0; i < MAX_STUDENTS; i++)
    {
        लिखो("Enter name of student %d: ", i + 1);
        fgets(students[i].name, MAX_NAME, stdin);

        के_लिए(पूरा j = 0; j < MAX_SUBJECTS; j++)
        {
            लिखो("Enter marks for subject %d: ", j + 1);
            पढ़ो("%d", &students[i].marks[j]);
        }
        अक्षर_पढ़();
        students[i].average = calculate_average(students[i].marks, MAX_SUBJECTS);
    }

    दायमिक max_avg = -1;
    पूरा top_index = -1;
    के_लिए(पूरा i = 0; i < MAX_STUDENTS; i++)
    {
        अगर(students[i].average > max_avg)
        {
            max_avg = students[i].average;
            top_index = i;
        }
    }

    लिखो("\nTop scorer: %s with average %.2f\n", students[top_index].name, students[top_index].average);
    लिखो("\nStudent averages:\n");
    के_लिए(पूरा i = 0; i < MAX_STUDENTS; i++)
    {
        लिखो("%s: %.2f\n", students[i].name, students[i].average);
    }

    लौटाओ 0;
}
