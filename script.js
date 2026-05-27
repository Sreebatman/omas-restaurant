/* ============================================================
   OMA'S RESTAURANT — INTERACTIVE SCRIPTS
   Navbar, Scroll Animations, Testimonial Carousel, Counter
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ---- Dynamic Year ----
    const yearEl = document.getElementById('currentYear');
    if (yearEl) yearEl.textContent = new Date().getFullYear();


    // ============================================================
    // NAVBAR: Transparent → Solid on Scroll
    // ============================================================
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    let lastScrollY = 0;

    function handleNavScroll() {
        const scrollY = window.scrollY;
        if (scrollY > 60) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        lastScrollY = scrollY;
    }

    window.addEventListener('scroll', handleNavScroll, { passive: true });
    handleNavScroll();

    // Mobile toggle
    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('open');
        navLinks.classList.toggle('mobile-open');
        document.body.style.overflow = navLinks.classList.contains('mobile-open') ? 'hidden' : '';
    });

    // Close menu on link click
    navLinks.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('open');
            navLinks.classList.remove('mobile-open');
            document.body.style.overflow = '';
        });
    });


    // ============================================================
    // ACTIVE NAV LINK on Scroll
    // ============================================================
    const sections = document.querySelectorAll('section[id]');
    const navLinkElements = document.querySelectorAll('.nav-link');

    function updateActiveLink() {
        const scrollPos = window.scrollY + 120;

        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            const id = section.getAttribute('id');

            if (scrollPos >= top && scrollPos < top + height) {
                navLinkElements.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', updateActiveLink, { passive: true });


    // ============================================================
    // SCROLL ANIMATIONS (Intersection Observer)
    // ============================================================
    const animatedElements = document.querySelectorAll('[data-animate]');

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -60px 0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, parseInt(delay));
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animatedElements.forEach(el => observer.observe(el));


    // ============================================================
    // COUNTER ANIMATION (Hero Stats)
    // ============================================================
    const counters = document.querySelectorAll('.stat-number[data-count]');
    let countersAnimated = false;

    function animateCounters() {
        if (countersAnimated) return;

        counters.forEach(counter => {
            const target = parseInt(counter.dataset.count);
            const duration = 2000;
            const startTime = performance.now();

            function updateCount(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                // Ease-out cubic
                const eased = 1 - Math.pow(1 - progress, 3);
                const current = Math.floor(eased * target);

                counter.textContent = current;

                if (progress < 1) {
                    requestAnimationFrame(updateCount);
                } else {
                    counter.textContent = target;
                }
            }

            requestAnimationFrame(updateCount);
        });

        countersAnimated = true;
    }

    // Trigger when hero stats come into view
    const statsSection = document.querySelector('.hero-stats');
    if (statsSection) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounters();
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        statsObserver.observe(statsSection);
    }


    // ============================================================
    // TESTIMONIAL CAROUSEL
    // ============================================================
    const track = document.getElementById('testimonialsTrack');
    const prevBtn = document.getElementById('testimonialPrev');
    const nextBtn = document.getElementById('testimonialNext');
    const dots = document.querySelectorAll('#testimonialDots .dot');
    const cards = track ? track.querySelectorAll('.testimonial-card') : [];

    let currentSlide = 0;
    let slidesPerView = 3;
    let autoplayInterval;

    function getCardsPerView() {
        if (window.innerWidth <= 768) return 1;
        if (window.innerWidth <= 1024) return 2;
        return 3;
    }

    function getMaxSlide() {
        return Math.max(0, cards.length - slidesPerView);
    }

    function updateCarousel() {
        if (!track || cards.length === 0) return;

        const cardWidth = cards[0].offsetWidth;
        const gap = parseInt(getComputedStyle(track).gap) || 24;
        const offset = currentSlide * (cardWidth + gap);

        track.style.transform = `translateX(-${offset}px)`;

        // Update dots
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === currentSlide);
        });
    }

    function nextSlide() {
        currentSlide = currentSlide >= getMaxSlide() ? 0 : currentSlide + 1;
        updateCarousel();
    }

    function prevSlide() {
        currentSlide = currentSlide <= 0 ? getMaxSlide() : currentSlide - 1;
        updateCarousel();
    }

    if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetAutoplay(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetAutoplay(); });

    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
            currentSlide = Math.min(i, getMaxSlide());
            updateCarousel();
            resetAutoplay();
        });
    });

    function startAutoplay() {
        autoplayInterval = setInterval(nextSlide, 5000);
    }

    function resetAutoplay() {
        clearInterval(autoplayInterval);
        startAutoplay();
    }

    // Handle resize
    function handleResize() {
        slidesPerView = getCardsPerView();
        currentSlide = Math.min(currentSlide, getMaxSlide());
        updateCarousel();
    }

    window.addEventListener('resize', handleResize);
    handleResize();
    startAutoplay();


    // ============================================================
    // SMOOTH SCROLL for anchor links
    // ============================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const navHeight = navbar.offsetHeight;
                const targetPos = target.getBoundingClientRect().top + window.scrollY - navHeight;

                window.scrollTo({
                    top: targetPos,
                    behavior: 'smooth'
                });
            }
        });
    });


    // ============================================================
    // PARALLAX subtle effect on hero
    // ============================================================
    const heroBg = document.querySelector('.hero-bg img');
    if (heroBg && window.innerWidth > 768) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            if (scrollY < window.innerHeight) {
                heroBg.style.transform = `scale(${1.05 + scrollY * 0.0001}) translateY(${scrollY * 0.15}px)`;
            }
        }, { passive: true });
    }


    // ============================================================
    // LIVE RESTAURANT STATUS MONITOR
    // Hours: 8:00 AM – 1:00 AM (next day) IST
    // ============================================================
    function updateRestaurantStatus() {
        const statusText = document.getElementById('statusText');
        const statusDot = document.getElementById('statusDot');
        const navStatusText = document.getElementById('navStatusText');
        const navStatusDot = document.getElementById('navStatusDot');

        // Get current time in IST
        const now = new Date();
        const istOffset = 5.5 * 60; // IST is UTC+5:30
        const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
        const ist = new Date(utc + (istOffset * 60000));

        const hours = ist.getHours();
        const minutes = ist.getMinutes();
        const totalMinutes = hours * 60 + minutes;

        // Open: 8:00 AM (480 min) to 1:00 AM next day
        // Closed: 1:00 AM (60 min) to 8:00 AM (480 min)
        const openTime = 480;   // 8:00 AM
        const closeTime = 60;   // 1:00 AM

        const isOpen = totalMinutes >= openTime || totalMinutes < closeTime;

        let heroText = '';
        let navText = '';

        if (isOpen) {
            // Green dot for hero badge
            if (statusDot) {
                statusDot.style.background = '#4ade80';
                statusDot.style.animation = 'pulse 2s ease-in-out infinite';
            }
            // Green dot for navbar
            if (navStatusDot) {
                navStatusDot.classList.remove('closed');
            }

            if (totalMinutes >= openTime) {
                const minsUntilClose = (24 * 60 - totalMinutes) + closeTime;
                if (minsUntilClose <= 60) {
                    heroText = 'Open Now · Closing Soon at 1:00 AM';
                    navText = 'Closing Soon';
                } else {
                    heroText = 'Open Now · Until 1:00 AM';
                    navText = 'Open Now';
                }
            } else {
                const minsLeft = closeTime - totalMinutes;
                heroText = 'Open Now · Closing in ' + minsLeft + ' min';
                navText = 'Closes in ' + minsLeft + 'm';
            }
        } else {
            // Red dot for hero badge
            if (statusDot) {
                statusDot.style.background = '#f87171';
                statusDot.style.animation = 'none';
            }
            // Red dot for navbar
            if (navStatusDot) {
                navStatusDot.classList.add('closed');
            }

            const minsUntilOpen = openTime - totalMinutes;
            if (minsUntilOpen <= 60) {
                heroText = 'Closed · Opens in ' + minsUntilOpen + ' min';
                navText = 'Opens in ' + minsUntilOpen + 'm';
            } else {
                const hrsLeft = Math.floor(minsUntilOpen / 60);
                const minsLeft = minsUntilOpen % 60;
                heroText = 'Closed · Opens at 8:00 AM (' + hrsLeft + 'h ' + minsLeft + 'm)';
                navText = 'Closed';
            }
        }

        if (statusText) statusText.textContent = heroText;
        if (navStatusText) navStatusText.textContent = navText;
    }

    // Run immediately and then every 30 seconds
    updateRestaurantStatus();
    setInterval(updateRestaurantStatus, 30000);

});
