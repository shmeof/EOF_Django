# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
 
# ���ݿ����
def testdb(request):
    # ��ʼ��
    response = ""
    response1 = ""
    
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
	
    # ͨ��objects���ģ�͹�������all()������������У��൱��SQL�е�SELECT * FROM
    list = Test.objects.all()
        
    # filter�൱��SQL�е�WHERE���������������˽��
    response2 = Test.objects.filter(id=1) 
    
    # ��ȡ��������
    response3 = Test.objects.get(id=1) 
    
    # ���Ʒ��ص����� �൱�� SQL �е� OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    
    #��������
    Test.objects.order_by("id")
    
    # ����ķ�����������ʹ��
    Test.objects.filter(name="runoob").order_by("id")
    
    # �����������
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
	