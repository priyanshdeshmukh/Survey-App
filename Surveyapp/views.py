from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Employee, Survey, SurveyEmployee, Question, SurveyResponse
from django.core.mail import EmailMessage


def index(request):
    return render(request, 'Surveyapp/home.html')


def question_list(request, survey_id):
    m = request.session['username']

    emp_record = Question.objects.filter(surveyquestion__survey_id=survey_id)
    question_all = Question.objects.all()
    context = {'session': m, 'survey_id': survey_id, 'question_list': emp_record}

    return render(request, 'Surveyapp/question_list.html', context)


def employee(request):
    m = request.session['username']
    emp = Employee.objects.get(emp_username=m)

    emp_record = SurveyEmployee.objects.filter(employee=emp.id)

    Completed_survey = list()
    incomplete_survey = list()
    assign_survey = list()
    total_survey = list()

    for survey in emp_record:
        survey_count = SurveyResponse.objects.filter(employee_id=emp.id, survey_id=survey.survey_id).count()
        print("survey_count*****", survey_count)
        if survey_count:
            if SurveyResponse.objects.filter(survey_id=survey.survey_id, employee_id=emp.id, SaveStatus=True):
                Completed_survey.append(survey)
            else:
                incomplete_survey.append(survey)
        else:
            assign_survey.append(survey)

    incomplete_surveylen = len(incomplete_survey)
    Completed_surveylen = len(Completed_survey)

    context = {'session': m, 'total_survey': total_survey, 'survey_list': emp_record,
               'completed_survey': Completed_survey, 'incomplete_survey': incomplete_survey,
               'assign_survey': assign_survey, 'complete_count': Completed_surveylen,
               'incomplete_count': incomplete_surveylen}

    send_email(request)
    return render(request, "Surveyapp/survey.html", context)


def login(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if Employee.objects.get(emp_username=username, emp_password=password):
            m = request.session['username'] = username

            print("Session Name = "+m)
            return redirect('employee')
        return render(request, "Surveyapp/login.html", context)

    return render(request, "Surveyapp/login.html", context)


def save(request, survey_id):
    m = request.session['username']
    emp = Employee.objects.get(emp_username=m)

    for name in request.POST:
        print("question id: ", name)
        if name != "csrfmiddlewaretoken" and name != "submitform":
            isRecord = SurveyResponse.objects.filter(survey=Survey.objects.get(id=survey_id),
                                                     employee=Employee.objects.get(id=emp.id),
                                                     question=Question.objects.get(id=name))

            if not isRecord:
                if request.POST[name]:
                    surveyResponseObj = SurveyResponse()
                    surveyResponseObj.survey = Survey.objects.get(id=survey_id)
                    surveyResponseObj.employee = Employee.objects.get(id=emp.id)
                    surveyResponseObj.question = Question.objects.get(id=name)
                    surveyResponseObj.response = request.POST[name]
                    if request.POST['submitform'] == "Save":
                        surveyResponseObj.SaveStatus = False
                    else:
                        surveyResponseObj.SaveStatus = True
                    surveyResponseObj.save()

    return redirect("employee")


def send_email(request):
    try:
        name = request.session['username']
        email = EmailMessage('Survey Link', 'http://127.0.0.1:8000/employee/', to=['shitalraut708@gmail.com'])
        print("---------------mail sent---------------")
    except Exception as e:
        print(e)

    return redirect('employee')


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('login')
