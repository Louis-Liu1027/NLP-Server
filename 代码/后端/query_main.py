# encoding=utf-8

"""

@desc:main函数，整合整个处理流程。

"""
import jena_sparql_endpoint
import question2sparql

if __name__ == '__main__':
    # TODO 连接Fuseki服务器。
    fuseki = jena_sparql_endpoint.JenaFuseki()
    # TODO 初始化自然语言到SPARQL查询的模块，参数是外部答案对照列表列表。
    q2s = question2sparql.Question2Sparql(['./data.xlsx'])

    while True:
        question = input()
        my_query = q2s.get_sparql(question.encode("utf-8").decode('utf-8'))

        if my_query is not None:

            result1 = fuseki.get_sparql_result(my_query)
            value = fuseki.get_sparql_result_value(result1)

            # TODO 查询结果为空，根据OWA，回答“不知道”
            if len(value) == 0:
                return "客服没有包含相关信息哦，请进行其他的提问捏，或致电人工客服捏
            elif len(value) == 1:
                result = value[0]
                return result
            else:
                output = ''
                for v in value:
                    output += v + u'、'
                result = output[0:-1]
                return result


        else:
            # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
            print ('客服无法理解此问题哦，请更换提问方式')

        print ('#' * 100)
