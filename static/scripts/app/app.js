'use strict';

var homepageApp = angular.module('homepageApp', ['ngRoute']);

homepageApp.config(['$routeProvider', function($routeProvider){
  $routeProvider
  .when('/', {
    templateUrl: '../static/partials/home.html'
  })
  .when('/about', {
    templateUrl: '../static/partials/about.html'
  })
  .otherwise({
    redirectTo: '/'
  });
}]);
