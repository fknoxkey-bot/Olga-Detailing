document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('siteNav');

  toggle.addEventListener('click', function () {
    var isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  nav.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });

  var contactToggles = document.querySelectorAll('.contact-toggle');

  function closeAllContactMenus(except) {
    document.querySelectorAll('.contact-menu.open').forEach(function (menu) {
      if (menu !== except) menu.classList.remove('open');
    });
  }

  contactToggles.forEach(function (btn) {
    var menu = btn.nextElementSibling;
    btn.addEventListener('click', function (event) {
      event.stopPropagation();
      var isOpen = menu.classList.contains('open');
      closeAllContactMenus();
      menu.classList.toggle('open', !isOpen);
    });
  });

  document.addEventListener('click', function () {
    closeAllContactMenus();
  });

  document.querySelectorAll('.toggle-pricing').forEach(function (btn) {
    var panel = btn.dataset.target ? document.getElementById(btn.dataset.target) : btn.nextElementSibling;
    var label = btn.querySelector('.toggle-label');
    var openLabel = btn.dataset.openLabel || 'Hide Pricing';
    var closedLabel = btn.dataset.closedLabel || 'See Pricing';
    btn.addEventListener('click', function () {
      var isOpen = panel.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      label.textContent = isOpen ? openLabel : closedLabel;
    });
  });

  document.querySelectorAll('.ba-slider').forEach(function (slider) {
    var range = slider.querySelector('.ba-range');
    if (!range) return;
    var setPos = function () {
      slider.style.setProperty('--pos', range.value + '%');
    };
    range.addEventListener('input', setPos);
    setPos();
  });
});
