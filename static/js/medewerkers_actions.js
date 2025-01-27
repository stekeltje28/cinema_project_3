document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('performanceChart').getContext('2d');
    const performanceChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Januari', 'Februari', 'Maart', 'April', 'Mei'],
            datasets: [{
                label: 'Prestaties per Maand',
                data: [65, 59, 80, 81, 56],
                backgroundColor: 'rgba(0, 121, 255, 0.8)',
                borderColor: 'rgba(0, 121, 255, 1)',
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
        newDatumRow.innerHTML = `
            <input type="date" name="datum[]" required style="padding: 8px; width: 48%; margin-right: 4%; border-radius: 4px;">
            <input type="time" name="tijd[]" required style="padding: 8px; width: 48%; border-radius: 4px;">
        `;
        container.appendChild(newDatumRow);
    }

    document.getElementById('addDatumButton').addEventListener('click', addDatum);
});

