webpackJsonp([7],{BiQG:function(t,i){},hCiV:function(t,i,s){"use strict";Object.defineProperty(i,"__esModule",{value:!0});var e={data:function(){var t=this;return{showBase:!1,goodsId:"",quota:0,quotaUsed:2,customStepperConfig:{handleOverLimit:function(i){var s=i.action,e=i.limitType,n=i.quota,o=i.quotaUsed;if("minus"===s)t.$toast("至少选择一件商品");else if("plus"===s)if(e===LIMIT_TYPE.QUOTA_LIMIT){var a="单次限购"+n+"件";o>0&&(a+="，你已购买"+o),t.$toast(a)}else t.$toast("库存不够了")}},sku:{tree:[{k:"颜色",v:[{id:"1193",name:"红色",imgUrl:"https://img.yzcdn.cn/2.jpg"},{id:"1215",name:"蓝色",imgUrl:"https://img.yzcdn.cn/2.jpg"}],k_s:"s2"},{k:"尺寸",v:[{id:"1193",name:"1"},{id:"1215",name:"1"}],k_s:"s1"}],list:[{id:2259,price:100,s1:"1215",s2:"1193",stock_num:110}],price:"1.00",stock_num:227,collection_id:2261,none_sku:!1,messages:[{datetime:"0",multiple:"1",name:"备注",type:"text",required:"1"}],hide_stock:!1},goods:{title:"测试商品",picture:"https://img.yzcdn.cn/2.jpg"}}},methods:{onClickMiniBtn:function(){this.showBase=!0},onClickBigBtn:function(){this.showBase=!0},onBuyClicked:function(){this.$router.push({path:"./shoppingCar"})},onAddCartClicked:function(){}}},n={render:function(){var t=this,i=t.$createElement,s=t._self._c||i;return s("div",{staticClass:"details"},[s("van-swipe",{attrs:{autoplay:3e3,"indicator-color":"white"}},[s("van-swipe-item",[t._v("1")]),t._v(" "),s("van-swipe-item",[t._v("2")]),t._v(" "),s("van-swipe-item",[t._v("3")]),t._v(" "),s("van-swipe-item",[t._v("4")])],1),t._v(" "),t._m(0),t._v(" "),s("div",{staticClass:"details-price"},[t._v("￥168")]),t._v(" "),t._m(1),t._v(" "),s("div",{staticClass:"recommend-content"},[s("div",{staticClass:"details-title"},[t._v("recommend-content")]),t._v(" "),s("ul",t._l(3,function(i,e){return s("li",{on:{click:function(i){t.goDetails(e)}}},[s("div",{staticClass:"commodity-img"}),t._v(" "),s("div",{staticClass:"commodity-introduce"},[t._m(2,!0),t._v(" "),s("div",{staticClass:"card-shopping"},[s("van-icon",{staticStyle:{"margin-top":"0.2rem"},attrs:{name:"shopping-cart-o",size:"1.2rem",color:"red"}})],1)])])}),0)]),t._v(" "),s("van-sku",{attrs:{sku:t.sku,goods:t.goods,"goods-id":t.goodsId,"hide-stock":t.sku.hide_stock,quota:t.quota,"quota-used":t.quotaUsed,"custom-stepper-config":t.customStepperConfig},on:{"buy-clicked":t.onBuyClicked,"add-cart":t.onAddCartClicked},model:{value:t.showBase,callback:function(i){t.showBase=i},expression:"showBase"}}),t._v(" "),s("van-goods-action",[s("van-goods-action-mini-btn",{attrs:{icon:"chat-o",text:"客服"},on:{click:t.onClickMiniBtn}}),t._v(" "),s("van-goods-action-mini-btn",{attrs:{icon:"cart-o",text:"购物车"},on:{click:t.onClickMiniBtn}}),t._v(" "),s("van-goods-action-big-btn",{attrs:{text:"加入购物车"},on:{click:t.onClickBigBtn}}),t._v(" "),s("van-goods-action-big-btn",{attrs:{primary:"",text:"立即购买"},on:{click:t.onClickBigBtn}})],1)],1)},staticRenderFns:[function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"commodity-introduce"},[i("div",{staticClass:"commodity-left"},[i("div",{staticClass:"commodity-name textOverFlow"},[i("span",{staticStyle:{"font-weight":"bold"}},[this._v("name")])]),this._v(" "),i("div",{staticStyle:{"font-size":"12px",color:"#666","margin-top":"1px"}},[this._v("\n        这里是......\n      ")])])])},function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"details-content"},[i("div",{staticClass:"details-title"},[this._v("details-title")]),this._v(" "),i("div",{staticClass:"details-introduce"},[this._v("\n      哈哈哈哈哈哈哈哈哈啊哈哈哈哈啊哈哈哈哈哈哈\n    ")])])},function(){var t=this.$createElement,i=this._self._c||t;return i("div",{staticClass:"commodity-left"},[i("div",{staticClass:"commodity-name textOverFlow"},[this._v("\n              name\n            ")]),this._v(" "),i("div",{staticStyle:{"font-size":"12px",color:"#666","margin-top":"1px"}},[this._v("\n              168元/斤\n            ")])])}]};var o=s("VU/8")(e,n,!1,function(t){s("BiQG")},"data-v-1719374a",null);i.default=o.exports}});
//# sourceMappingURL=7.406610816f60c0fde5dd.js.map