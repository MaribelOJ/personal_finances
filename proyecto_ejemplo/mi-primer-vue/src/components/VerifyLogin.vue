<template>
    <div>
        <button @click="toggleLogin">
            {{ isLoggedIn ? 'Cerrar Sesión' : 'Iniciar Sesion' }}
        </button>
        <p v-if="isLoggedIn"> Has Iniciado Sesión</p>
        <p v-else> Has Cerrado Sesión</p>
    </div>
</template>

<script>
export default{
    data(){
        return {
            isLoggedIn: false
        }
    },
    methods: {
        toggleLogin(){
            this.isLoggedIn = !this.isLoggedIn;
        }
    }
};
</script>