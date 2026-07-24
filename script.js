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
    var frame = slider.querySelector('.ba-frame');
    if (!frame) return;
    var dragging = false;

    function setPos(pct) {
      pct = Math.max(0, Math.min(100, pct));
      slider.style.setProperty('--pos', pct + '%');
      frame.setAttribute('aria-valuenow', Math.round(pct));
    }

    function setFromClientX(clientX) {
      var rect = frame.getBoundingClientRect();
      setPos(((clientX - rect.left) / rect.width) * 100);
    }

    frame.addEventListener('pointerdown', function (event) {
      dragging = true;
      frame.setPointerCapture(event.pointerId);
      setFromClientX(event.clientX);
    });
    frame.addEventListener('pointermove', function (event) {
      if (dragging) setFromClientX(event.clientX);
    });
    function stop() { dragging = false; }
    frame.addEventListener('pointerup', stop);
    frame.addEventListener('pointercancel', stop);

    frame.addEventListener('keydown', function (event) {
      var cur = parseFloat(slider.style.getPropertyValue('--pos')) || 50;
      if (event.key === 'ArrowLeft') setPos(cur - 4);
      else if (event.key === 'ArrowRight') setPos(cur + 4);
      else return;
      event.preventDefault();
    });
  });
});
