// Vue.config.delimiters = ["[[", "]]"] 2.0.55 之後 dosen't work

// var xhr= new XMLHttpRequest()
// xhr.open('GET','http://localhost:8000/api/recipes',true)
// xhr.send()
// xhr.onload= function(){
//   // console.log('response: ',xhr.responseText)
//   var data=JSON.parse(JSON.parse(xhr.responseText).data)
//   console.log('parse: ',data)
// }

var recipe_url="http://localhost:8000/recipe/api"

var vm = new Vue({
  el: "#app",
  data: {
    recipes: [],
    tags: "12345678"
  }
  ,
  mounted(){
    var vobj=this
    $.get(recipe_url).then(function(res){
      console.log("res:",res)
      vobj.recipes = JSON.parse(res.data)
      console.log("recipes: ",vobj.recipes)
    })
  
  }
  ,
  delimiters: ["[[", "]]"]
})



