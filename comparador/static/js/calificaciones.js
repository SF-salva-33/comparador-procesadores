document.addEventListener('DOMContentLoaded', () => {
    // Asegúrate de que los valores de puntaje sean numéricos y sin comillas adicionales
    const procesadores = [
        { nombre: '{{ procesador1.nombre }}', puntaje: {{ puntaje1|safe }} }, // 'safe' para que no se escape
        { nombre: '{{ procesador2.nombre }}', puntaje: {{ puntaje2|safe }} }
    ];

    // Función para calcular las estrellas
    function calcularEstrellas(procesadores) {
        const puntajeMaximo = Math.max(...procesadores.map(p => p.puntaje));

        procesadores.forEach(p => {
            const estrellas = Math.round((p.puntaje / puntajeMaximo) * 5);
            p.estrellas = estrellas; // Asigna las estrellas al procesador
        });
    }

    // Llamar a la función para calcular las estrellas
    calcularEstrellas(procesadores);

    // Mostrar las estrellas en el HTML
    procesadores.forEach((p, index) => {
        const calificacionDiv = document.querySelectorAll('.calificacion')[index]; // Seleccionar el div de calificación correspondiente
        calificacionDiv.innerHTML = `<h3>Calificación:</h3>`; // Reinicia el contenido

        // Agregar estrellas llenas según el puntaje
        for (let i = 1; i <= p.estrellas; i++) {
            calificacionDiv.innerHTML += `<span class="star" data-value="${i}">&#9733;</span>`; // Estrella llena
        }

        // Agregar estrellas vacías hasta completar 5
        for (let i = p.estrellas + 1; i <= 5; i++) {
            calificacionDiv.innerHTML += `<span class="star" data-value="${i}">&#9734;</span>`; // Estrella vacía
        }
    });
});
