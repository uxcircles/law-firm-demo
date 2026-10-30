// Mobile navigation
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
}

// 中文 / English tabs
document.querySelectorAll('.lang-tabs').forEach((tabs) => {
  const scope = tabs.parentElement;
  tabs.querySelectorAll('button').forEach((btn) => {
    btn.addEventListener('click', () => {
      tabs.querySelectorAll('button').forEach((b) => b.setAttribute('aria-selected', String(b === btn)));
      scope.querySelectorAll('[data-lang-panel]').forEach((p) => {
        p.hidden = p.dataset.langPanel !== btn.dataset.lang;
      });
    });
  });
});

// Reveal on scroll
const els = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  els.forEach((el) => io.observe(el));
} else {
  els.forEach((el) => el.classList.add('in'));
}

const y = document.getElementById('year');
if (y) y.textContent = new Date().getFullYear();
