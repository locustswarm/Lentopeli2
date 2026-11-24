function lähetä_viesti(saatuarvo = window.location.href) {
    $.ajax({
        url: '/viestikanava', type: 'POST', contentType: 'application/json',
        data: JSON.stringify({'lähetysarvo': saatuarvo}),
        success: function (response) {
            document.getElementById('vastausjuttu').innerHTML = response.result;
        },
        error: function (error) {
            console.log(error);
        }
    });
}
lähetä_viesti();