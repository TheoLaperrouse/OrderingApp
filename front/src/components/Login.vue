<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="max-w-md p-6 bg-white rounded shadow">
            <h2 class="text-2xl font-bold mb-4">Connexion</h2>
            <form @submit.prevent="login" class="space-y-4">
                <div>
                    <label for="username" class="block font-medium">Nom d'utilisateur</label>
                    <input
                        type="text"
                        id="username"
                        v-model="username"
                        class="w-full px-4 py-2 rounded border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                    />
                </div>
                <div>
                    <label for="password" class="block font-medium">Mot de passe</label>
                    <input
                        type="password"
                        id="password"
                        v-model="password"
                        class="w-full px-4 py-2 rounded border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                    />
                </div>
                <button type="submit" class="w-full px-4 py-2 bg-blue-500 text-white rounded">Se connecter</button>
            </form>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    setup() {
        const username = ref('');
        const password = ref('');

        const login = () => {};

        return {
            username,
            password,
            login,
        };
    },
};
</script>

<style></style>
