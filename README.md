# Survey-App

1. Admin:
  a. Users – 
    a.i. CRUD
      a.i.1. Create employees for respective organization
  b. Question Library
    b.i. Create and Manage Questions – 
      b.i.1. CRUD
      b.i.2. Should be able to Create Survey using following types of questions: (https://www.questionpro.com/tour/sample-questions.html ) : 
        b.i.2.a. Open Ended Questions - Questionnaire: Open ended questions which are in the form of Comment Box / Single Row Text / Numeric Input / Email Address questions are designed to collect narrative responses. Assign open-ended text as custom variables for data pre-population within the survey.
  c. Setup surveys
    c.i. Create and Manage Survey - CRUD
    c.ii. Assign questions to survey
  d. Assign Surveys to Employees
    d.i. Bulk Assignment
  e. Send email notification to user on – survey assignment, survey completion

2. Employee:
  a. Take surveys      
    a.i. Survey Renderer – Implement pagination considering 5 questions each page.
    a.ii. Continue survey in case user lefts in between
  b. Landing page for Employee – welcome message, display survey assignment link to start/continue survey
