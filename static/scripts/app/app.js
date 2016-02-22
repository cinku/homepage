'use strict';

var homepageApp = angular.module('homepageApp', ['ngRoute', 'ngAnimate', 'directives']);

homepageApp.config(['$routeProvider', function($routeProvider){
  $routeProvider
  .when('/', {
    templateUrl: '../static/partials/home.html'
  })
  .when('/about', {
    templateUrl: '../static/partials/about.html'
  })
  .when('/blog', {
    templateUrl: '../static/partials/blog.html'
  })
  .when('/contact', {
    templateUrl: '../static/partials/contact.html'
  })
  .otherwise({
    redirectTo: '/'
  });
}]);
