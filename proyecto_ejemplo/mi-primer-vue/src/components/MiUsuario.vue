<template>
    <div>
        <p>Nombre: {{ persona.nombre}}</p>
        <p>Nombre: {{ persona.edad}}</p>
        <button @click="cumplirAnios">Cumplir Años</button>
    </div>
</template>

<script>
import {reactive} from 'vue';

export default {
    setup(){
        const persona = reactive({
            nombre:'juan',
            edad: 25
        });

        const cumplirAnios = () => {
            persona.edad++;
        };

        return {persona, cumplirAnios};
    }
}
</script>