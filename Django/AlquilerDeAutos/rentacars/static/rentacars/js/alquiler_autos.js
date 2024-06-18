document.addEventListener('DOMContentLoaded', function () {
    const fechaInicioInput = document.getElementById('id_fecha_inicio');
    const fechaFinInput = document.getElementById('id_fecha_fin');
    const autoId = document.getElementById('id_auto').value;
    const precioTotal = document.getElementById('id_precio_total');

    async function getPrecioDiario (autoId){
        const response = await fetch(`/rentacars/get_precio_diario/${autoId}/`);
        const data = await response.json();
        return parseFloat(data.precio_diario);
    }

    async function calculatePrice() {
        const fechaInicio = new Date(fechaInicioInput.value);
        const fechaFin = new Date(fechaFinInput.value);
        const precioDiario = await getPrecioDiario(autoId);


        if (!isNaN(fechaInicio) && !isNaN(fechaFin) && !isNaN(precioDiario)) {
            const delta = fechaFin - fechaInicio;
            const dias = (delta / (1000 * 60 * 60 * 24)) + 1;
            const total = dias * precioDiario;
            precioTotal.value = `${total.toFixed(2)}`;
        } else {
            precioTotal.value = 0.0;
            console.log(precioDiario)
        }
    }

    // autoInput.addEventListener('change', calculatePrice);
    fechaInicioInput.addEventListener('change', calculatePrice);
    fechaFinInput.addEventListener('change', calculatePrice);


});
