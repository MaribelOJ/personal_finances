<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card shadow-lg my-5">
                    <div class="card-body">
                        <h2 class="text-center">Ingresar Usuario</h2>
                        <form @submit.prevent="registerUser">
                            <div class="form-group">
                                <label for="fullName">Nombre Completo</label>
                                <input type="text" v-model="fullName" id="fullName" class="form-control"
                                    placeholder="Nombre completo" required />
                            </div>
                            <div class="form-group">
                                <label for="email">Correo Electrónico</label>
                                <input type="email" v-model="email" id="email" class="form-control"
                                    placeholder="Correo electrónico" required />
                            </div>
                            <div class="form-group">
                                <label for="userRole">Rol del Usuario</label>
                                <input type="text" v-model="userRole" id="userRole" class="form-control"
                                    placeholder="Cliente - Admin - SuperAdmin" />
                            </div>
                            <div class="form-group">
                                <label for="password">Contraseña</label>
                                <input type="password" v-model="password" id="password" class="form-control"
                                    placeholder="Contraseña" required />
                            </div>
                            <div class="form-group">
                                <label for="confirmPassword">Confirmar Contraseña</label>
                                <input type="password" v-model="confirmPassword" id="confirmPassword"
                                    class="form-control" placeholder="Confirmar contraseña" required />
                            </div>
                            <button type="submit" class="btn btn-primary btn-block">Ingresar</button>
                        </form>
                        <div v-if="error" class="mt-3 alert alert-danger">
                            {{ error }}
                        </div>
                        <div v-if="successMessage" class="mt-3 alert alert-success">
                            {{ successMessage }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import { useAuthStore } from '@/store';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { createUser } from '@/services/userService'; // Asegúrate de que este servicio esté definido

export default {
    setup() {
        const authStore = useAuthStore();

        const user = authStore.user;
        const permissions = authStore.permissions;

        const router = useRouter();
        const fullName = ref('');
        const email = ref('');
        const userRole = ref('');
        const password = ref('');
        const confirmPassword = ref('');
        const error = ref(null);
        const successMessage = ref(null);

        const insertUser = async () => {
            error.value = null; // Limpiar posibles mensajes de error
            successMessage.value = null; // Limpiar posibles mensajes de éxito
            if (password.value !== confirmPassword.value) {
                error.value = 'Las contraseñas no coinciden';
                return;
            }

            try {
                await createUser(fullName.value, email.value, userRole.value, password.value);
                successMessage.value = 'Usuario Ingresado exitosamente!';
            } catch (err) {
                error.value = 'Error al ingresar el usuario';
                console.error(err);
            }
        };

        const logout = () => {
            authStore.logout(); // Llama a la acción de logout del store
            router.push('/'); // Redirige a la ruta raíz
        };

        return {
            fullName,
            email,
            userRole,
            password,
            confirmPassword,
            error,
            successMessage,
            user,
            permissions,
            logout,
            insertUser
        };
    }
};
</script>