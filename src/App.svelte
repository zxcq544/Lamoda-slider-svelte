<script>
	import Product from "./Product.svelte";
	import { big_json } from "./stores.js";
	let external_json_data = [
		{
			"data-brand": "Ferz",
			"data-category": "\u0428\u0430\u043f\u043a\u0438",
			"data-color-family": "\u0447\u0435\u0440\u043d\u044b\u0439",
			"data-discount": 189,
			"data-discount-percent": 15,
			"data-gallery": [
				"./img236x341/F/E/FE913CMCLMM1_7110810_1_v1.jpg",
				"./img236x341/F/E/FE913CMCLMM1_7110811_2_v1.jpg",
				"./img236x341/F/E/FE913CMCLMM1_7110812_3_v1.jpg",
				"./img236x341/F/E/FE913CMCLMM1_7110813_4_v1.jpg",
				"./img236x341/F/E/FE913CMCLMM1_7113609_9_v1.jpg",
			],
			"data-gender": "men",
			"data-href": "https://www.lamoda.ru/p/fe913cmclmm1/hats-ferz-shapka/",
			"data-is-new": "false",
			"data-is-premium": "false",
			"data-is-sport": "false",
			"data-name": "\u0428\u0430\u043f\u043a\u0430",
			"data-price": 1010,
			"data-price-origin": 1199,
			"data-season":
				"{5593:\u0437\u0438\u043c\u0430,5595:\u0434\u0435\u043c\u0438\u0441\u0435\u0437\u043e\u043d}",
			"data-sizes": ["56/58"],
			"data-sku": "FE913CMCLMM1",
			"data-src": "./img236x341/F/E/FE913CMCLMM1_7110810_1_v1.jpg",
		},
		{
			"data-brand": "The North Face",
			"data-category": "\u0428\u0430\u043f\u043a\u0438",
			"data-color-family": "\u0441\u0438\u043d\u0438\u0439",
			"data-gallery": [
				"./img236x341/R/T/RTLAAS700801_15379707_1_v1.jpg",
				"./img236x341/R/T/RTLAAS700801_15379708_2_v1.jpg",
				"./img236x341/R/T/RTLAAS700801_15391079_9_v1_2x.jpg",
				"./img236x341/R/T/RTLAAS700801_15391078_11_v1_2x.jpg",
			],
			"data-gender": "unisex",
			"data-href": "https://www.lamoda.ru/p/rtlaas700801/hats-thenorthface-shapka/",
			"data-is-new": "true",
			"data-is-premium": "false",
			"data-is-sport": "true",
			"data-name": "\u0428\u0430\u043f\u043a\u0430",
			"data-price-origin": 2499,
			"data-season":
				"{5593:\u0437\u0438\u043c\u0430,5595:\u0434\u0435\u043c\u0438\u0441\u0435\u0437\u043e\u043d}",
			"data-sizes": [],
			"data-sku": "RTLAAS700801",
			"data-src": "./img236x341/R/T/RTLAAS700801_15379707_1_v1.jpg",
		},
	];
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
