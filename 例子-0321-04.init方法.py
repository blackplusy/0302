#coding=utf-8
# class student:
# #     def __init__(self):
# #         self.boy=20
# #         self.girl=30
# #     def study(self):
# #             print('good good study')
# #
# # #实例化对象
# # simida=student()
# # print(simida.boy)
# # print(simida.girl)

class student:
    def __init__(self,boy,girl):
        self.badyboy=boy
        self.cutegirl=girl
    def study(self):
        print('study')
z=student(20,30)
print('班级中有男生%d'% z.badyboy)
print('班级中有女生%d'% z.cutegirl)
