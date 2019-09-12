from django.http import HttpResponse
from django.shortcuts import render
from .models import *
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def listpic(request):
    return render(request,'listpic.html')
def newslistpic(request):
    return render(request,'newslistpic.html')

def add(request):
    # people=People()
    # people.name='吕断断'
    # people.age=30
    # people.save()
    # people=People(name='吕断瞎',age=50)
    # people.save()

    # People.objects.create(name='吕大胸',age=60)
    date=dict(name='张女士',people_id=7)
    Father.objects.create(**date)
    return HttpResponse('增加')

def select(request):
    # date=People.objects.all()
    # # print(date)
    # for i in date:
    #     print(i.name)
    #     print(i.age)

    # date=People.objects.filter(name='吕断断').first()
    # # print(date[0].age)
    # print(date.age)

    # date=People.objects.get(id=1)
    # print(date.name)

    # date=People.objects.all().order_by('age')
    # # print(date)
    # for i in date:
    #     print(i.name)

    # date=People.objects.order_by('-age')
    # for i in date:
    #     print(i.name)

    # date=People.objects.exclude(name='吕断瞎')
    # # print(date)
    # for i in date:
    #     print(i.name)

    # date=People.objects.filter(name='吕断瞎').count()
    # print(date)
    # date=People.objects.filter(name='吕断瞎').values()
    # print(date)

    # date=People.objects.filter(id__lte=4)#id__gt   大于
    # print(date)

    date=People.objects.filter(name__contains='j')
    print(date[0].name)

    return HttpResponse('查询')

def change(request):
    # date=People.objects.get(id=2)
    # date.name='python'
    # date.save()

    People.objects.filter(id=2).update(name='java')

    return HttpResponse('修改')

def yiadd(request):
    father=Father.objects.filter(name='黄先生',id=1).first()
    # father=Father.objects.get(id=2)
    father.people=People.objects.get(name='吕大屁股')
    father.save()
    return HttpResponse('一对多添加')

def manytomanyadd(request):
    # Person.objects.create(name='吕佳佳',age=20,height=150)
    # Person.objects.create(name='司扬眉',age=26,height=160)
    # Person.objects.create(name='黄佳豪',age=22,height=180)
    # Person.objects.create(name='李明磊',age=21,height=170)
    # Person.objects.create(name='张颖',age=24,height=150)

    # Teacher.objects.create(name='老张',gender='男')
    # Teacher.objects.create(name='老边',gender='男')
    # Teacher.objects.create(name='老刘',gender='女')
    # Teacher.objects.create(name='老王',gender='女')

    #新学员 欢欢  想学 老王的课  create 正向操作
    # teacher_obj=Teacher.objects.get(name='老王')
    # teacher_obj.person.create(name='欢欢',age=23,height=170)

    #老学员 黄佳豪  想学 老张的课 创建关系操作 正向操作
    # teacher_obj=Teacher.objects.filter(name='老张').first()
    # person_obj=Person.objects.filter(name='黄佳豪').first()
    # teacher_obj.person.add(person_obj)

    #老学员  张颖 想学  老边的课  创建关系操作 正向操作
    # teacher_obj=Teacher.objects.filter(name='老边').first()
    # person_obj=Person.objects.filter(name='张颖').first()
    # teacher_obj.person.add(person_obj)

    #新学员 冰冰 想学 老刘的课 正向操作
    # teacher_obj=Teacher.objects.filter(name='老刘').first()
    # teacher_obj.person.create(name='冰冰',age=18,height=160)

    ##反向操作
    teacher_obj=Teacher.objects.filter(name='老张').first()
    person_obj=Person.objects.filter(name='吕佳佳').first()
    person_obj.teacher_set.add(teacher_obj)

    return HttpResponse('多对多添加')


def manytomanysel(request):
    return HttpResponse('多对多查询')

def manytomanychange(request):
    #正向修改
    # teacher_obj=Teacher.objects.filter(name='老王').first()
    # person1=Person.objects.filter(name='司扬眉').first()
    # person2=Person.objects.filter(name='李明磊').first()
    # teacher_obj.person.set([person1,person2])
    #反向修改
    person_obj=Person.objects.filter(name='黄佳豪').first()
    teacher1=Teacher.objects.filter(name='老王').first()
    teacher2=Teacher.objects.filter(name='老张').first()
    person_obj.teacher_set.set([teacher1,teacher2])
    return HttpResponse('多对多修改')


def manytomanydelete(request):
    #remove  删除关系
    #正向删除
    # person1=Person.objects.filter(name='黄佳豪').first()
    # teacher1=Teacher.objects.filter(name='老张').first()
    # teacher1.person.remove(person1)

    #反向删除
    # person1=Person.objects.filter(name='黄佳豪').first()
    # teacher1=Teacher.objects.filter(name='老王').first()
    # person1.teacher_set.remove(teacher1)

    #delete  删除数据和关系
    #老张辞职了

    # Teacher.objects.filter(name='老张').first().delete()
    #张颖退学了
    Person.objects.filter(name='张颖').first().delete()
    return HttpResponse('多对多删除')


from django.db.models import Avg,Max,Sum,Min,Count,F,Q

def jttest(request):
    # data=Person.objects.all().aggregate(avg_age=Avg('age'))
    # print(data)
    #
    # data=Person.objects.all().aggregate(sum_age=Sum('age'))
    # print(data)



    return HttpResponse('集合查询')

