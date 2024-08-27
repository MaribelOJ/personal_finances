<template>
    <button @click="enviarMensaje">Haz clic aquí</button>
</template>

<script>
export default{
    methods: {
        enviarMensaje() {
            this.$emit('mensaje-enviado', 'Hola desde componente Hijo');
        }
    }
};
</script>