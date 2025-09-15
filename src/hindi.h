#ifndef HINDI_H
#define HINDI_H

// ------------------ Data Types ------------------
#define पूरा int
#define बड़ा long
#define छोटा short
#define अक्षर char
#define दायमिक float
#define दुगना double
#define शून्य void

// ------------------ Keywords ------------------
#define अगर if
#define अन्यथा else
#define जबतक while
#define के_लिए for
#define करो do
#define लौटाओ return
#define यथार्थ true
#define झूठ false
#define तोड़ break
#define जारी continue
#define अनुक्रम struct
#define स्थिर const
#define नया new
#define हटाओ delete
#define खाली NULL
#define बनाओ typedef

// ------------------ stdio.h replacements ------------------
#include <stdio.h>

#define लिखो printf
#define पढ़ो scanf
#define खोलो fopen
#define बंद_करो fclose
#define अक्षर_पढ़ getchar
#define अक्षर_लिखो putchar
#define पंक्ति_पढ़ gets
#define पंक्ति_लिखो puts

// ------------------ Misc ------------------
#define मुख्य main

// ------------------ stdlib ------------------
#include <stdlib.h>
#define आवंटित malloc
#define मुक्त free

#endif
