'use strict';

var homepageApp = angular.module('homepageApp', ['ngRoute', 'ngAnimate', 'directives', 'controllers']);

homepageApp.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
  $routeProvider
  .when('/', {
    templateUrl: '../static/partials/home.html'
  })
  .when('/about', {
    templateUrl: '../static/partials/about.html'
  })
  .when('/blog', {
    templateUrl: '../static/partials/blog.html',
    controller: 'BlogController'
  })
  .when('/contact', {
    templateUrl: '../static/partials/contact.html'
  })
  .otherwise({
    redirectTo: '/'
  });

  $locationProvider.html5Mode({
    enabled: true,
    requireBase: false
  });
}]);
