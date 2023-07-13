# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:40:30 2022

@author: zw
"""
import pandas as pd
import jieba

'''分解问题，获取关键词'''


def question_cut(sent):
    # stop_word为停用词表，将问答中无关词过滤
    stop_word = ['有', '什么', '的', '都', '类型', '三只', '小店', '是', '苹果', '上衣', 'u', '多少', '钢笔', '泡面', ' ', '。', '盘']
    result = []#存储过滤停用词后的问题关键词

    try:
        result = list(jieba.cut(sent))  #问题分词
    except:
        print('该问题无法识别:{}'.format(sent))#输出异常问题，如无法分词的输入
        return []

    if result:
        aim_list = [word for word in result if word not in stop_word]  #过滤无关词，提取问题关键词
        return aim_list#返回关键词列表
    return []#如果什么都没有，返回空列表


'''问题解答'''


def answer_rule(question):
    data = pd.read_excel('./data.xlsx')  #读取答案对照表
    aim_list = question_cut(question)  #获得规则关键词

    if aim_list:  # 判断是否有关键词
        if len(aim_list) == 1:  #一个关键词的问题求解
            df1 = data.loc[data['问题'].str.contains(aim_list[0])]  #查询答案所在位置
            result = df1.iloc[0]['答案']  #提取答案
            print(result)
            return result

        if len(aim_list) == 2:  #两个个关键词的问题求解
            df1 = data.loc[data['问题'].str.contains(aim_list[0])]#查询答案所在位置
            df2 = df1.loc[data['问题'].str.contains(aim_list[1])]#在包含aim_list[0]的结果中继续查询答案所在位置
            result = df2.iloc[0]['答案']#提取答案
            print(result)
            return result#返回答案
    else:
        return "暂无结果"#如果没有关键词，表面问题不在研究范围，返回暂无结果


# def test():
#     # 验证判断结果是否正确
#     data = pd.read_excel('./data.xlsx')
#     for i in range(len(data)):
#         question = data.iloc[i]['问题']
#         if anser_rule(question) != data.iloc[i]['答案']:
#             print(question)
#             print(data.iloc[i]['答案'])
#             print(anser_rule(question))


if __name__ == "__main__":
    # test()#测试是否能回答全部问题
    print("***********您好，请输入您的查询问题:************")
    question = input()  # 输入问题，如： '电磁炉的价格是什么'
    # print(anser_rule(question))
