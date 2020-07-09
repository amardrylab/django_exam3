# Online examination in django

## 1) Create the user accounts of the students
    ./manage.py shell
    from bank.adduser import fromcsv
    fromcsv("user.csv")

## 2) Populate the Qbank model by your MCQ questions. A sample question paper can be loaded by executing the following commands

    ./manage.py shell
    from bank.qp import loadquestion
    loadquestion("qp.dat")

## 3) Generate questionpaper from the questions stored in the Qbank.

    from bank.qp import buildquestionpaper
    buildquestionpaper(title, list=[*range(1,11)])

## 4) Set the questions in random order for each student

    ./manage.py shell
    from exam.papersetting import set
    set(title, users)

Where title will be the string indicating the paper title.

## 5) Send the link to the users by executing the following commands

    ./manage.py shell
    from exam.papersetting import sendotlforexam
    sendotlforexam(title)

## 6) Student will then submit their response by visiting their respective link given in their mail delivered.

## 7) After receiving their response administrator will evaluate the response by excuting the following commands

    ./manage.py shell
    from exam.papersetting import evaluate
    evaluate(title)

Where the argument title will be the string indicating the paper title.

## 8) Send the result to the students by executing the following commands

    from exam.papersetting import sendresult
    sendresult(title)
