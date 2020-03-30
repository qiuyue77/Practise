from django.db import connection
from django.db.models import Avg, Count, Sum, Q, F, Max, Min
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Teacher, Score, Course


# Create your views here.

def practise(request):
    # 1. 查询平均成绩大于60分的同学的id和平均成绩；
    # num =1
    # results = Student.objects.annotate(avg=Avg('score__number')).filter(avg__gte=60).values('id', 'avg')
    # for result in results:
    #     print(f'{num}:sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 2. 查询所有同学的id、姓名、选课的数量、总成绩；
    # num = 2
    # results = Student.objects.annotate(count=Count('score'), sum=Sum("score__number")).values('id', 'name', 'count', 'sum')
    # for result in results:
    #     print(f'{num}:sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 3. 查询姓“李”的老师的个数；
    # num = 3
    # results = Teacher.objects.filter(name__startswith='李').count()
    # print(f'{num}:sulosion:{results}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')


    # 4. 查询没学过“李老师”课的同学的id、姓名；
    # num =4
    # results = Student.objects.exclude(score__course__teacher__name = "李老师").values('id', 'name')
    # for result in results:
    #     print(f'{num}:sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 5. 查询学过课程id为1和2的所有同学的id、姓名；
    # num = 5
    # results = Student.objects.filter(score__course_id__in= [1,2]).distinct().values('id', 'name')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'{num}: Got it!')

    # 6. 查询学过“黄老师”所教的“所有课”的同学的id、姓名；
    num = 6
    # results = Student.objects.filter(score__course__teacher__name = "黄老师").distinct().values('id', 'name')
    results = Student.objects.annotate(
        nums=Count("score__course", filter=Q(score__course__teacher__name='黄老师'))).filter(
        nums=Course.objects.filter(teacher__name='黄老师').count()).values('id', 'name')
    for result in results:
        print(f'{num}.sulosion:{result}')
    print(connection.queries)
    return HttpResponse(f'第{num}题: Got it!')
    # ============================
    # "SELECT DISTINCT `student`.`id`, `student`.`name` FROM `student`
    # INNER JOIN `score` ON (`student`.`id` = `score`.`student_id`)
    # INNER JOIN `course` ON (`score`.`course_id` = `course`.`id`)
    # INNER JOIN `teacher` ON (`course`.`teacher_id` = `teacher`.`id`)
    # WHERE `teacher`.`name` = '黄老师'", 'time': '0.001'
    # ============================
    # SELECT `student`.`id`, `student`.`e` FROM `student`
    # LEFT OUTER JOIN `score` ON (`student`.`id` = `score`.`student_id`)
    # LEFT OUTER JOIN `course` ON (`score`.`course_id` = `course`.`id`)
    # LEFT OUTER JOIN `teacher` ON (`course`.`teacher_id` = `teacher`.`id`)
    # GROUP BY `student`.`id` HAVING COUNT(CASE WHEN (`teacher`.`name` = '黄老师')
    # THEN `score`.`course_id` ELSE NULL END

    # 7. 查询所有课程成绩小于60分的同学的id和姓名；
    # num = 7
    # results = Student.objects.exclude(score__number__gt=60).values('id', 'name')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 8. 查询没有学全所有课的同学的id、姓名；
    # num = 8
    # results = Student.objects.annotate(
    #     count=Count(F("score__course"))).filter(count__lt=Course.objects.all().count()).values('id', 'name')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 9. 查询所有学生的姓名、平均分，并且按照平均分从高到低排序；
    # num = 9
    # results = Student.objects.annotate(
    #     avg = Avg("score__number")).order_by('-avg').values('name', 'avg')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 10. 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分；
    # num = 10
    # results = Course.objects.annotate(
    #     max = Max("score__number"), min = Min("score__number")).values('id', 'name','max', 'min')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 11. 查询每门课程的平均成绩，按照平均成绩进行排序；
    # num = 11
    # results = Course.objects.annotate(
    #     avg = Avg("score__number")).order_by('avg').values('id', 'name','avg')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 12. 统计总共有多少女生，多少男生；
    # num = 12
    # results = Student.objects.aggregate(
    #     male_num=Count("gender", filter=Q(gender=1)), female_num=Count("gender", filter=Q(gender=2)))
    # print(f'{num}.sulosion:{results}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 13. 将“黄老师”的每一门课程都在原来的基础之上加5分；
    # num = 13
    # results = Score.objects.filter(course__teacher__name="黄老师").update(number = F("number")+5)
    # print(f'{num}.sulosion:{results}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 14. 查询两门以上不及格的同学的id、姓名、以及不及格课程数；
    # num = 14
    # results = Student.objects.annotate(count=Count("score__number", filter=Q(score__number__lt=60))).filter(
    #     count__gt=1).values('id', 'name', 'count')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')

    # 查询每门课的选课人数；
    # num = 15
    # results = Course.objects.annotate(count = Count('score__student')).values('name','count')
    # for result in results:
    #     print(f'{num}.sulosion:{result}')
    # print(connection.queries)
    # return HttpResponse(f'第{num}题: Got it!')
