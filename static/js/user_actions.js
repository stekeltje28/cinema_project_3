function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('show');
    }
}

function closeModal() {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        modal.classList.remove('show');
    });
}

function openLoginModal() {
    closeModal()
    openModal('loginModal');
}

function openRegisterModal() {
    closeModal()
    openModal('registerModal');
}

window.addEventListener('click', function(event) {
    const loginModal = document.getElementById("loginModal");
    const registerModal = document.getElementById("registerModal");

    if (event.target === loginModal || event.target === registerModal) {
        closeModal();
    }
});

const urlParams = new URLSearchParams(window.location.search);
if (urlParams.has('show_modal') && urlParams.get('show_modal') === 'true') {
    openModal('loginModal');
}

function login(event) {
    event.preventDefault();

    let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const data = {
        email: email,
        password: password,
    };

    fetch('/accounts/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.is_logged_in) {
            alert(data.message);
            window.location.href = '/account/dashboard';
        } else {
            alert(data.message || 'Inlogfout!');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Er is een fout opgetreden: ' + error);
    });
}

function create_user(event) {
    event.preventDefault();

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const email = document.getElementById("reg_email").value;
    const password1 = document.getElementById("reg_password").value;
    const password2 = document.getElementById("reg_password2").value;
    const name = document.getElementById('reg_first_name').value + " " + document.getElementById('reg_last_name').value;
    const leeftijd = document.getElementById('reg_leeftijd').value;

    const data = {
        name: name,
        email: email,
        password1: password1,
        password2: password2,
        leeftijd: leeftijd
    };

    if (password1 !== password2) {
        alert("Wachtwoorden komen niet overeen!");
        return;
    }

    fetch('/accounts/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/account/dashboard';
            alert('Welkom op je persoonlijke dashboard');
        } else {
            alert(data.error || 'Er ging iets mis. Probeer opnieuw.');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Er ging iets mis bij het verzenden van de aanvraag.');
    });
}

function checkUserLoggedIn(url = null) {
    fetch('/accounts/check-logged-in/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.is_logged_in) {
            if(url != null) {
                window.location.href = url;
                console.log('naar de url')
            } else {
                console.log('de user is al ingelogd')
                closeModal()
                openModal('loggedInModal');
            }
        } else {
            closeModal()
            console.log('user is gechecked en niet ingelogd, de modal login word geopend')
            openModal('loginModal');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function logout() {
    fetch('/accounts/logout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            localStorage.removeItem('userSession');
            sessionStorage.removeItem('userSession');
            window.location.href = '/';
        } else {
            alert('Er is iets misgegaan tijdens het uitloggen!');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Er is een probleem opgetreden bij het uitloggen. Probeer het opnieuw.');
    });
}

const queryParams = new URLSearchParams(window.location.search);
let modalstatus = parseInt(queryParams.get('openLoginModal'));

if(modalstatus) {
    openLoginModal()
}
