'use strict';

angular.module('directives', [])
.directive("menuDirective", function() {
  function link(scope, el, attrs) {
    el.on('click', function() {
      console.log('test');
    });
  }
  return {
    link: link
  }
});
