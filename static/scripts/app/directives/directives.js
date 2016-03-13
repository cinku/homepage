'use strict';

angular.module('directives', [])
.directive('navMenu', function($location) {
  return function(scope, element, attrs) {
    var links = element.find('a'),
        onClass = 'active',
        routePattern,
        link,
        url,
        currentLink,
        urlMap = {},
        i;

    if (!$location.$$html5) {
      routePattern = /^#[^/]*/;
    }

    for (i = 0; i < links.length; i++) {
      link = angular.element(links[i]);
      url = link.attr('href');
      if ($location.$$html5) {
        urlMap[url] = link;
      } else {
        urlMap[url.replace(routePattern, '')] = link;
      }
    }
    
    element.on('click', function() {
        $('#navbar').collapse('hide');
    });

    scope.$on('$routeChangeStart', function() {
      var pathLink = urlMap[$location.path()];
      if (pathLink) {
        if (currentLink) {
          currentLink.removeClass(onClass);
        }
        currentLink = pathLink;
        currentLink.addClass(onClass);
      }
    });
  };
});
