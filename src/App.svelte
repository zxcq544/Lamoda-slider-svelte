<script>
	import Product from "./Product.svelte";
	import { big_json } from "./stores.js";
</script>

<div class="products-catalog__list">
	{#each $big_json as json_data}
		<Product {json_data} />
	{/each}
</div>
