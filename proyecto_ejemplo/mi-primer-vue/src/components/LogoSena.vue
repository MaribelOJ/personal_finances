<template>
    <img id="logoSena" :src="imagenUrl" :alt="imagenAlt">
</template>

<script>
export default{
    data(){
        return {
            imagenUrl:"https://sena.edu.co/Style%20Library/alayout/images/logoSena.png",
            imagenAlt: "Logo del SENA"
        };
    }
};
</script>

<style scoped>
 #logoSena{
    border-radius: 50%;
    border: 5px solid gray;
    padding: 1em;
    margin: 1em;
 }
</style>