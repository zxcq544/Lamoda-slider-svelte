<script>
	import Product from "./Product.svelte";
	import { big_json } from "./stores.js";
	//TODO: ADD Money type and size type depending on country
	//TODO: ADD Discount element and "New" element
</script>

<div class="products-catalog__list">
	{#each $big_json as json_data}
		<Product {json_data} />
	{/each}
</div>
