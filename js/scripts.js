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
