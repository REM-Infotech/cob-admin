window.addEventListener("DOMContentLoaded", (event) => {
  var ModalMessage = document.getElementById("ModalMessage");
  if (ModalMessage != null) {
    $(document).ready(function () {
      $("#ModalMessage").modal("show");
    });
  }

  // Toggle the side navigation
  const sidebarToggle = document.body.querySelector("#sidebarToggle");
  if (sidebarToggle) {
    // Uncomment Below to persist sidebar toggle between refreshes
    // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
    //     document.body.classList.toggle('sb-sidenav-toggled');
    // }
    sidebarToggle.addEventListener("click", (event) => {
      event.preventDefault();
      document.body.classList.toggle("sb-sidenav-toggled");
      localStorage.setItem(
        "sb|sidebar-toggle",
        document.body.classList.contains("sb-sidenav-toggled")
      );
    });
  }
});

window.addEventListener("DOMContentLoaded", (event) => {
  var datatablesSimple = document.querySelector('table[id="DataTable"]');
  if (datatablesSimple) {
    new DataTable(datatablesSimple, {
      searching: false,
      deferRender: true,
      deferLoading: 57,
      processing: true,
    });
  }
});
