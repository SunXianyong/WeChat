webpackJsonp([5],{Qq6M:function(t,e){},wSL0:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var c={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"shoppingCar"},[n("van-nav-bar",{attrs:{title:"购物车"}}),t._v(" "),n("div",{staticClass:"shoppingCard"},[n("van-checkbox-group",{model:{value:t.result,callback:function(e){t.result=e},expression:"result"}},[n("van-cell-group",t._l(t.list,function(e,c){return n("van-cell",{key:e,attrs:{clickable:""},on:{click:function(e){t.toggle(c)}}},[n("van-checkbox",{ref:"checkboxes",refInFor:!0,attrs:{name:e}}),t._v(" "),n("van-card",{attrs:{num:"2",price:"2.00",desc:"描述信息",title:"商品标题",thumb:t.imageURL}})],1)}),1)],1)],1),t._v(" "),n("div",{staticClass:"shoppingSubmit"},[n("van-submit-bar",{attrs:{price:3050,"button-text":"提交订单"},on:{submit:t.onSubmit}},[n("van-checkbox",{model:{value:t.checked,callback:function(e){t.checked=e},expression:"checked"}},[t._v("全选")])],1)],1)],1)},staticRenderFns:[]};var a=n("VU/8")({data:function(){return{imageURL:"https://img.yzcdn.cn/2.jpg",result:[],list:["a","b","c"],checked:""}},methods:{toggle:function(t){this.$refs.checkboxes[t].toggle()},onSubmit:function(){this.$router.push({path:"./toBePaid"})}}},c,!1,function(t){n("Qq6M")},"data-v-29896f7e",null);e.default=a.exports}});
//# sourceMappingURL=5.7ecf6861857ccd2bfcd5.js.map