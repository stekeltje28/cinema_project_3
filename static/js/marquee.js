function initMarquees() {
        const marquees = document.querySelectorAll('.marquee');
        const speeds = [12, 15, 18];

        marquees.forEach((marquee, index) => {
            const root = document.documentElement;
            const marqueeContent = marquee.querySelector('.marquee-content');
            const marqueeItems = Array.from(marqueeContent.children);

            const marqueeElementsDisplayed = parseInt(getComputedStyle(root).getPropertyValue('--marquee-elements-displayed'), 20);
            const marqueeItemsCount = marqueeItems.length;

            while (marqueeContent.children.length < marqueeElementsDisplayed * 3) {
                marqueeItems.forEach(item => {
                    marqueeContent.appendChild(item.cloneNode(true));
                });
            }


            const speed = speeds[index % speeds.length];
            marquee.style.setProperty('--marquee-animation-duration', `${speed}s`);
        });
    }

    document.addEventListener('DOMContentLoaded', initMarquees);
