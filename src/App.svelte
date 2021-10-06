<script>
	import Product from "./Product.svelte";
	import { big_json } from "./stores.js";
</script>

<div class="products-catalog__list">
	<Product json_data={$big_json[0]} />
	<Product json_data={$big_json[1]} />
	<Product json_data={$big_json[2]} />
	<Product json_data={$big_json[3]} />
	<Product json_data={$big_json[4]} />

	<Product json_data={$big_json[5]} />
	<Product json_data={$big_json[6]} />
	<Product json_data={$big_json[7]} />
	<Product json_data={$big_json[8]} />
	<Product json_data={$big_json[9]} />
</div>
