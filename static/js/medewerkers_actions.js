document.addEventListener('DOMContentLoaded', async function () {
    const ctx = document.getElementById('performanceChart').getContext('2d');

    try {
        const response = await fetch('/reservering-data/');
        if (!response.ok) throw new Error("Fout bij het ophalen van data");

        const jsonData = await response.json();

        if (!jsonData || jsonData.length === 0) {
            console.error("Geen geldige data ontvangen van de API");
            return;
        }

        const labels = jsonData.map(item => item.event__film__title || "Onbekend");
        const totalTickets = jsonData.map(item => item.total_tickets || 0);

        const gradient = ctx.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, 'rgba(0, 121, 255)');
        gradient.addColorStop(1, 'rgba(255, 255, 255)');

        // Chart aanmaken
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Aantal Reserveringen per Film',
                    data: totalTickets,
                    backgroundColor: gradient,
                    borderColor: 'rgba(0, 121, 255, 0.8)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

    } catch (error) {
        console.error("Er is een fout opgetreden:", error);
    }

    const locationSelect = document.getElementById('select_location');
    const roomSelect = document.getElementById('select_room');
    const rooms = roomSelect.querySelectorAll('option');

    locationSelect.addEventListener('change', function () {
        const selectedLocationId = locationSelect.value;

        rooms.forEach(function (option) {
            option.style.display = 'none';
        });

        rooms.forEach(function (option) {
            if (option.getAttribute('data-location-id') === selectedLocationId) {
                option.style.display = 'block';
            }
        });

        roomSelect.selectedIndex = 0;
    });

    zaalDropdown = document.getElementById('select_room');
    capaciteitInput = document.getElementById('beschikbare_plaatsen');

    zaalDropdown.addEventListener("change", function () {
        const selectedOption = zaalDropdown.options[zaalDropdown.selectedIndex];
        const capacity = selectedOption.getAttribute("data-capacity");
        capaciteitInput.value = capacity ? capacity : "";

        if (capacity) {
            const aantalPlaatsen = document.getElementById("aantal_reserveringen");

            aantalPlaatsen.addEventListener("input", function () {
                if (parseInt(aantalPlaatsen.value) > parseInt(capacity)) {
                    alert("Het aantal reserveringen kan niet groter zijn dan de zaalcapaciteit.");
                    aantalPlaatsen.value = capacity;
                }
            });
        }
    });

    function addDatum() {

        const container = document.getElementById('datums-container');
        const newDatumRow = document.createElement('div');
        newDatumRow.classList.add('datum-row');
        newDatumRow.style.marginBottom = '10px';
        print()
        newDatumRow.innerHTML = `
            <input type="date" name="datum[]" required style="padding: 8px; width: 48%; margin-right: 4%; border-radius: 4px;">
            <input type="time" name="tijd[]" required style="padding: 8px; width: 48%; border-radius: 4px;">
        `;
        container.appendChild(newDatumRow);
    }});

document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll('.edit-btn');  // De bewerkknoppen

    editButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Voorkom standaard formulierverzending
            const form = this.closest('form'); // Haal het bijbehorende formulier op
            const row = this.closest('tr'); // Vind de rij waar de knop op wordt geklikt
            const inputContainer = row.querySelector('.stoelen-input-container');
            const stoelenText = row.querySelector('.stoelen-tekst');
            const inputField = row.querySelector('.stoelen-input');

            const isEditing = inputContainer.style.display === 'block';
            stoelenText.style.display = isEditing ? 'block' : 'none';
            inputContainer.style.display = isEditing ? 'none' : 'block';

            if (!isEditing) {
                inputField.value = stoelenText.textContent.trim();
            } else {

                const aantalTickets = inputField.value.trim();
                if (aantalTickets) {
                    const hiddenInput = document.createElement('input');
                    hiddenInput.type = 'hidden';
                    hiddenInput.name = 'aantal_tickets';
                    hiddenInput.value = aantalTickets;
                    form.appendChild(hiddenInput);
                    form.submit();
                }
            }
        });
    });
});

function confirmDelete(reservationId) {
    if (confirm('Weet je zeker dat je deze reservering wilt verwijderen?')) {
        window.location.href = `/accounts/delete_reservation/${reservationId}/`;
    }
}
