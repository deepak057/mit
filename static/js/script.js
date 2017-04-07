var app=angular.module("mitApp",['ngRoute']);


app.config(function($routeProvider){

$routeProvider

.when('/',{

	controller:'homeController',
	templateUrl:'static/pages/home.html'
})

.otherwise({'redirect':'/'})

});

app.controller('homeController',function($scope){

});