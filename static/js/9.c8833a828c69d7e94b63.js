webpackJsonp([9],{GCmG:function(t,s,e){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var d={render:function(){var t=this,s=t.$createElement,e=t._self._c||s;return e("div",{staticClass:"contacts"},[e("van-nav-bar",{attrs:{title:"联系人地址","left-arrow":""}}),t._v(" "),e("van-address-list",{attrs:{list:t.list,"disabled-list":t.disabledList,"disabled-text":"以下地址超出配送范围"},on:{add:t.onAdd,edit:t.onEdit},model:{value:t.chosenAddressId,callback:function(s){t.chosenAddressId=s},expression:"chosenAddressId"}})],1)},staticRenderFns:[]},n=e("VU/8")({data:function(){return{chosenAddressId:"1",list:[{id:"1",name:"张三",tel:"13000000000",address:"浙江省杭州市西湖区文三路 138 号东方通信大厦 7 楼 501 室"},{id:"2",name:"李四",tel:"1310000000",address:"浙江省杭州市拱墅区莫干山路 50 号"}],disabledList:[{id:"3",name:"王五",tel:"1320000000",address:"浙江省杭州市滨江区江南大道 15 号"}]}},methods:{onAdd:function(){this.$toast("新增地址"),this.$router.push({path:"./editContacts"})},onEdit:function(t,s){this.$toast("编辑地址:"+s),this.$router.push({path:"./editContacts"})}}},d,!1,null,null,null);s.default=n.exports}});
//# sourceMappingURL=9.c8833a828c69d7e94b63.js.map