from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from score.models import PlaceInfo
import pandas as pd


# Create your views here.
class IndexView(View):
    def get(self, request):
        all_category = [item.category for item in PlaceInfo.objects.all()]

        final_dict = {}
        for category in set(all_category):
            all_item = PlaceInfo.objects.filter(category=category)
            all_subcategory = [item.sub_category for item in all_item]
            all_tags = set()
            for tag_str in all_subcategory:
                tags = tag_str.split(",")
                for tag in tags:
                    all_tags.add(tag)
            final_dict[category] = all_tags
        # print("此时的字典为:", final_dict)
        return render(request, 'index.html', {"final_dict": final_dict})

    def post(self, request):
        check_box_list = request.POST.getlist("check_box_list")
        category = request.POST.get("category")
        total_lis = PlaceInfo.objects.filter(category=category).order_by("-score")
        final_lis = []
        for item in total_lis:
            if len(final_lis) >= 3:
                break
            for tag in check_box_list:
                if tag in item.sub_category:
                    final_lis.append(item)
                    break

        # print("选择前3个分数最高的地点。", final_lis)
        # print("socore", [item.socre for item in final_lis])
        # print("列表结果为：", check_box_list, category)
        return render(request, 'result.html', locals())


class ReusltView(View):
    def get(self, request):
        return render(request, 'result.html')

    def post(self, request):
        # print("评分完毕了。")
        # data = request.POST.getlist()

        data = request.POST
        try:
            for k in data:
                if k.startswith("data--"):
                    place_info = k.split("--")
                    place = PlaceInfo.objects.filter(id=int(place_info[2])).first()
                    new_score = float(data[k][0])
                    print("此时评分为：", place.score)
                    place.score_people_num = place.score_people_num + 1
                    place.score = (place.score + new_score) / 2
                    place.save()
                    print("修改评分成功了。", place.id, place.score)

            print(data)
            return HttpResponseRedirect("/index")
        except Exception as e:
            print("此时出错了。", e)
            # return render()

            # print("第一个data",data)
            # print("第2个data", data2)
            return HttpResponseRedirect("/index")


class InserDataView(View):
    def get(self, request):
        import os
        print(os.getcwd())
        df = pd.read_csv("data/data.csv")

        row_num = df.shape[0]
        for i in range(row_num):
            # print(df.iloc[i,:])
            place = PlaceInfo()
            place.score_people_num = df.iloc[i, :].commented_people
            place.score = df.iloc[i, :].score
            place.introduction = df.iloc[i, :].introduction
            place.place_name = df.iloc[i, :].names
            place.category = df.iloc[i, :].category
            place.sub_category = df.iloc[i, :].tags
            place.image = "place/" + df.iloc[i, :].image
            place.save()
        print("导入数据成功！")
        return render(request, 'index.html')
