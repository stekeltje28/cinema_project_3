function initMarquees() {
    const marquees = document.querySelectorAll('.marquee');

    marquees.forEach((marquee) => {
        const root = document.documentElement;
        const marqueeContent = marquee.querySelector('.marquee-content');
        const marqueeItems = Array.from(marqueeContent.children);

        // Bepaal hoeveel items getoond moeten worden
        const marqueeElementsDisplayed = parseInt(getComputedStyle(root).getPropertyValue('--marquee-elements-displayed'), 20);
        const marqueeItemsCount = marqueeItems.length;

        // Herhaal de items tot er genoeg zijn voor een vloeiende beweging
        while (marqueeContent.children.length < marqueeElementsDisplayed * 3) {
            marqueeItems.forEach(item => {
                marqueeContent.appendChild(item.cloneNode(true));
            });
        }

        // Zorg ervoor dat de animatie precies past bij het aantal afbeeldingen
        const totalWidth = marqueeItemsCount * 150; // breedte per afbeelding (150px)
        const duration = (totalWidth / 100) * 10; // stel de duur in op basis van de breedte
        marquee.style.setProperty('--marquee-animation-duration', `${duration}s`);
    });
}

document.addEventListener('DOMContentLoaded', initMarquees);
