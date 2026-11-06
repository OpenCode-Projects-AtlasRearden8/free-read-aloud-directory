(function () {
  "use strict";

  var buttons = Array.prototype.slice.call(
    document.querySelectorAll("#category-filters .filter")
  );
  var offlineOnly = document.getElementById("offline-only");
  var countEl = document.getElementById("result-count");
  var entries = Array.prototype.slice.call(document.querySelectorAll(".entry"));

  var currentCategory = "*";

  function apply() {
    var shown = 0;
    entries.forEach(function (entry) {
      var catOk =
        currentCategory === "*" ||
        entry.getAttribute("data-category") === currentCategory;
      var offlineOk =
        !offlineOnly.checked || entry.getAttribute("data-offline") !== "no";
      var visible = catOk && offlineOk;
      entry.hidden = !visible;
      if (visible) shown++;
    });

    // Hide a section heading/note when no entry in that category is visible
    var catIds = ["browser", "phone", "tts", "reader", "listen"];
    catIds.forEach(function (cat) {
      var any = entries.some(function (entry) {
        return (
          entry.getAttribute("data-category") === cat &&
          entry.hidden === false
        );
      });
      var heading = document.getElementById(cat);
      if (heading) heading.hidden = !any;
      var note = heading ? heading.nextElementSibling : null;
      if (note && note.classList.contains("section-note")) {
        note.hidden = !any;
      }
    });

    countEl.textContent = shown + " of " + entries.length + " entries shown";
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      buttons.forEach(function (b) {
        b.classList.remove("active");
        b.setAttribute("aria-pressed", "false");
      });
      btn.classList.add("active");
      btn.setAttribute("aria-pressed", "true");
      currentCategory = btn.getAttribute("data-filter");
      apply();
    });
  });

  offlineOnly.addEventListener("change", apply);
  apply();
})();
