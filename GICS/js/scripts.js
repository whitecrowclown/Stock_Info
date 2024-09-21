function toggleDropdown() {
  var dropdown = document.getElementById("gicsDropdown");
  dropdown.classList.toggle("show");
}

// 클릭 시 드롭다운 외부를 클릭하면 닫히는 동작
window.onclick = function (event) {
  if (!event.target.matches(".dropdown button")) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};
