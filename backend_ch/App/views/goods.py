from flask import Blueprint, jsonify
# from ..extensions import db

goods = Blueprint("goods", __name__)

# 商品列表
@goods.route("/list")
def goods_list():
    print(1)
    # data = db.session.execute('select * from goods')
    # lis = []
    # for i in data:
    #     dic ={}
    #     for k,v in i.items():
    #         dic[k] = v
    #     lis.append(dic)
    # return jsonify(lis)
    return "ok"