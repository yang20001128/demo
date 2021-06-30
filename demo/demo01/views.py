from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from demo01.models import Author, Book
from demo01.myserializers import AuthorSerializer, BooklSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import json


# class AuthorView(ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# Create your views here.
class Author_Create_View(APIView):
    """作者信息增加"""

    def post(self, request):
        # 接收数据
        parameter_json = request.body
        # json转字典
        parameter = json.loads(parameter_json)
        get_Name = parameter["Name"]
        get_Gender = parameter["Gender"]
        get_Born_Date = parameter["Born_Date"]
        if get_Name == "" or get_Gender == "" or get_Born_Date == "":
            data = {'msg': '400', 'data': '缺少字段'}
            return Response(data)
        elif Author.objects.filter(Name=get_Name):
            data = {'msg': '400', 'data': '作者已经存在'}
            return Response(data)
        elif str(get_Gender) not in ["1", "2"]:
            data = {'msg': '400', 'data': '性别格式错误,请输入1或者2(1,"男性"),(2,"女性"),'}
            return Response(data)
        else:
            rs = Author.objects.create(Name=get_Name, Gender=get_Gender, Born_Date=get_Born_Date)
            data = {'msg': '200', 'data': '存入成功'}
            return Response(data)


class Book_Create_View(APIView):
    """作品信息增加"""

    def post(self, request):
        # 接收数据
        parameter_json = request.body
        # json转字典
        parameter = json.loads(parameter_json)
        get_Book_Name = parameter["Book_Name"]
        get_Publish_Date = parameter["Publish_Date"]
        get_Country = parameter["Country"]
        Author_name = parameter['Author']
        Author_ = Author.objects.filter(Name=Author_name)
        print(Author_)
        print('*' * 100)
        print(Author_.exists())
        if get_Book_Name == "" or get_Publish_Date == "" or get_Country == "" or Author_name == "":
            data = {'msg': '400', 'data': '缺少字段'}
            return Response(data)
        elif Book.objects.filter(Book_Name=get_Book_Name):
            data = {'msg': '400', 'data': '作品已经存在'}
            return Response(data)
        elif Author_.exists() == False:
            data = {'msg': '400', 'data': '该作品作者不存在'}
            return Response(data)
        else:
            get_Author_id = Author.objects.filter(Name=Author_name)[0].id
            rs = Book.objects.create(Book_Name=get_Book_Name, Publish_Date=get_Publish_Date, Country=get_Country,
                                     Author_id=get_Author_id)
            data = {'msg': '200', 'data': '存入成功'}
            return Response(data)


class Author_Retrieve_View(APIView):
    """作者信息查询"""

    def get(self, request):
        rs = Author.objects.all()
        if rs.exists():
            # 如果要被序列化的是包含多条数据的查询集QuerySet,可以通过many = true参数补充说明
            rs = AuthorSerializer(rs, many=True)
            data = {'msg': '200', "data": rs.data}
            return Response(data)
        else:
            data = {'msg': '400'}
            return Response(data)

    def post(self, request):
        # 接收数据
        parameter_json = request.body
        # json转字典
        parameter = json.loads(parameter_json)
        get_Name = parameter["Name"]
        rs = Author.objects.filter(Name=get_Name)
        # 判断QuerySet结果集是否为空
        if rs.exists():
            # 如果要被序列化的是包含多条数据的查询集QuerySet,可以通过many = true参数补充说明
            rs = AuthorSerializer(rs, many=True)
            data = {'msg': '200', "data": rs.data}
            return Response(data)
        else:
            data = {'msg': '400'}
            return Response(data)


class Book_Retrieve_View(APIView):
    """作品信息查询"""

    def get(self, request):
        rs = Book.objects.all()
        if rs.exists():
            # 如果要被序列化的是包含多条数据的查询集QuerySet,可以通过many = true参数补充说明
            rs = BooklSerializer(rs, many=True)
            data = {'msg': '200', "data": rs.data}
            return Response(data)
        else:
            data = {'msg': '400'}
            return Response(data)

    def post(self, request):
        # 接收数据
        parameter_json = request.body
        # json转字典
        parameter = json.loads(parameter_json)
        get_Name = parameter["Book_Name"]
        rs = Book.objects.filter(Book_Name=get_Name)
        # 判断QuerySet结果集是否为空
        if rs.exists():
            # 如果要被序列化的是包含多条数据的查询集QuerySet,可以通过many = true参数补充说明
            rs = BooklSerializer(rs, many=True)
            data = {'msg': '200', "data": rs.data}
            return Response(data)
        else:
            data = {'msg': '400'}
            return Response(data)
