<template>
    <div class="bg-gray-200 p-4">
        <h2 class="text-2xl font-bold mb-4">Liste des cocktails</h2>
        <ul>
            <li v-for="drink in drinks" :key="drink.id" class="mb-4">
                <DrinkCard :drink="drink" @quantity-updated="updateQuantity"></DrinkCard>
            </li>
        </ul>

        <button
            v-if="filteredDrinks.length > 0"
            class="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
            @click="sendOrder"
        >
            Envoyer la commande
        </button>
    </div>
</template>

<script>
import { ref } from 'vue';
import DrinkCard from './DrinkCard.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        DrinkCard,
    },
    setup() {
        const drinks = ref([
            { id: 1, name: 'Margarita', quantity: 0, price: 5 },
            { id: 2, name: 'Cosmopolitan', quantity: 0, price: 10 },
            { id: 3, name: 'Gimlet', quantity: 0, price: 8 },
            { id: 4, name: 'Manhattan', quantity: 0, price: 7 },
        ]);

        const updateQuantity = (updatedDrink) => {
            const index = drinks.value.findIndex((drink) => drink.id === updatedDrink.id);
            if (index !== -1) {
                drinks.value[index].quantity = updatedDrink.quantity;
            }
        };

        return {
            drinks,
            updateQuantity,
        };
    },
    computed: {
        filteredDrinks() {
            return this.drinks.filter((drink) => drink.quantity > 0);
        },
        totalPrice() {
            return this.filteredDrinks.reduce((accumulator, drink) => accumulator + drink.price * drink.quantity, 0);
        },
    },
    methods: {
        sendOrder() {
            const formattedOrder = this.filteredDrinks.map(
                (drink) => `${drink.name} : ${drink.quantity} -> ${drink.name * drink.quantity} €`,
            );
            this.$swal(`Commande bien envoyée \n\n ${formattedOrder.join('\n')}\n\n Prix Total : ${this.totalPrice} €`);
            this.drinks = this.drinks.map((value) => ({
                ...value,
                quantity: 0,
            }));
        },
    },
});
</script>
