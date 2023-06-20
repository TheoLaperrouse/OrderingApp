<template>
    <div class="p-4 bg-white rounded shadow">
        <h3 class="text-lg font-semibold">{{ drink.name }}</h3>
        <div class="flex items-center mt-2">
            <button class="px-2 py-1 bg-blue-500 text-white rounded" @click="decrement">-</button>
            <span class="mx-2">{{ drink.quantity }}</span>
            <button class="px-2 py-1 bg-blue-500 text-white rounded" @click="increment">+</button>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    props: {
        drink: {
            type: Object,
            required: true,
        },
    },
    methods: {
        increment() {
            this.$emit('quantity-updated', { id: this.drink.id, quantity: this.drink.quantity + 1 });
        },
        decrement() {
            if (this.drink.quantity > 0) {
                this.$emit('quantity-updated', { id: this.drink.id, quantity: this.drink.quantity - 1 });
            }
        },
    },
});
</script>
