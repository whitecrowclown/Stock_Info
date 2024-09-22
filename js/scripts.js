function toggleDropdown() {
  document.getElementById("gicsDropdown").classList.toggle("show");
}

// 드롭다운 클릭 시 닫기
window.onclick = function (event) {
  if (!event.target.matches(".dropdown a")) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};
// analytics.js
function initGoogleAnalytics() {
  // Google Analytics tracking code
  (function (i, s, o, g, r, a, m) {
    i["GoogleAnalyticsObject"] = r;
    (i[r] =
      i[r] ||
      function () {
        (i[r].q = i[r].q || []).push(arguments);
      }),
      (i[r].l = 1 * new Date());
    (a = s.createElement(o)), (m = s.getElementsByTagName(o)[0]);
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m);
  })(
    window,
    document,
    "script",
    "https://www.googletagmanager.com/gtag/js?id=G-XZFRF94P2N",
    "ga"
  );

  ga("create", "G-XZFRF94P2N", "auto");
  ga("send", "pageview");
}
