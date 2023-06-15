<template>
  <div class="bg-gray-200 p-4">
    <h2 class="text-2xl font-bold mb-4">Liste des cocktails</h2>
    <ul>
      <li v-for="cocktail in cocktails" :key="cocktail.id" class="mb-4">
        <Cocktail
          :cocktail="cocktail"
          @quantity-updated="updateQuantity"
        ></Cocktail>
      </li>
    </ul>

    <button
      class="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
      @click="sendOrder"
    >
      Envoyer la commande
    </button>
  </div>
</template>

<script>
import { ref } from "vue";
import Drink from "./Drink.vue";

export default {
  components: {
    Drink,
  },
  setup() {
    const drinks = ref([
      { id: 1, name: "Drink 1", quantity: 0 },
      { id: 2, name: "Drink 2", quantity: 0 },
    ]);

    const updateQuantity = (updatedDrink) => {
      const index = drinks.value.findIndex(
        (drink) => drink.id === updatedDrink.id
      );
      if (index !== -1) {
        drinks.value[index].quantity = updatedDrink.quantity;
      }
    };

    const sendOrder = () => {};

    return {
      drinks,
      updateQuantity,
      sendOrder,
    };
  },
};
</script>
