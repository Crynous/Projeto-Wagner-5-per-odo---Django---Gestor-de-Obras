//Script de JS para o Cep

document.addEventListener('DOMContentLoaded', function () {
    const cepInput = document.getElementById('cep-input');
    const logradouroInput = document.getElementById('id_logradouro');
    const bairroInput = document.getElementById('id_bairro');
    const municipioInput = document.getElementById('id_municipio');
    const estadoInput = document.getElementById('id_estado');

    cepInput.addEventListener('blur', function () {
        const cep = cepInput.value.replace(/\D/g, '');
        if (cep.length === 8) {
            fetch(`/obras/buscar-cep/?cep=${cep}`)
                .then(response => response.json())
                .then(data => {
                    if (data.erro) {
                        alert(data.erro);
                    } else {
                        logradouroInput.value = data.logradouro || '';
                        bairroInput.value = data.bairro || '';
                        municipioInput.value = data.localidade || '';
                        estadoInput.value = data.uf || '';
                    }
                })
                .catch(error => console.error('Erro ao buscar CEP:', error));
        } else {
            alert('CEP inválido! Insira um CEP no formato XXXXX-XXX.');
        }
    });
});
